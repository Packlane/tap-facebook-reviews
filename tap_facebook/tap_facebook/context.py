from datetime import datetime, date
import pendulum
import singer
from singer import bookmarks as bks_
from .http import Client
from .schemas import stream_ids


class Context(object):
    """Represents a collection of global objects necessary for performing
    discovery or for running syncs. Notably, it contains

    - config  - The JSON structure from the config.json argument
    - state   - The mutable state dict that is shared among streams
    - client  - An HTTP client object for interacting with the API
    - catalog - A singer.catalog.Catalog. Note this will be None during
                discovery.
    """
    def __init__(self, config, state):
        self.config = config
        self.state = state
        self.client = Client(config)
        self._catalog = None
        self.selected_stream_ids = None
        self.now = datetime.utcnow()

    @property
    def catalog(self):
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        self._catalog = catalog
        self.selected_stream_ids = set(
            [s.tap_stream_id for s in catalog.streams
             if s.is_selected()]
        )

    @property
    def bookmarks(self):
        if "bookmarks" not in self.state:
            self.state["bookmarks"] = {}
        return self.state["bookmarks"]

    def get_bookmark(self, path):
        bookmark = self.bookmarks
        return bookmark.get(path, None)

    def set_bookmark(self, path, val):
        if isinstance(val, datetime):
            val = val.isoformat()
        self.bookmarks[path] = val

    def update_start_date_bookmark(self, path):
        val = self.get_bookmark(path)
        if not val:
            val = self.config["start_date"]
            self.set_bookmark(path, val)
        return pendulum.parse(val)

    def write_state(self):
        singer.write_state(self.state)
