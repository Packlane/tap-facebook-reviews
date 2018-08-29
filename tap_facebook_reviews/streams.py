import singer
import dateutil

LOGGER = singer.get_logger()

# TODO:
# - add mechanism for bookmarking updated_at_min

class Stream(object):
    """Information about and functions for syncing streams for the Smile.io API.
    Important class properties:
    :var tap_stream_id:
    :var pk_fields: A list of primary key fields
    :var indirect_stream: If True, this indicates the stream cannot be synced
    directly, but instead has its data generated via a separate stream."""

    def __init__(self, tap_stream_id, pk_fields, direct_stream=True):
        self.tap_stream_id = tap_stream_id
        self.items_key = tap_stream_id
        self.pk_fields = pk_fields
        self.direct_stream = direct_stream

    def __repr__(self):
        return "<Stream(" + self.tap_stream_id + ")>"

    def metrics(self, records):
        with singer.metrics.record_counter(self.tap_stream_id) as counter:
            counter.increment(len(records))

    def write_records(self, records):
        singer.write_records(self.tap_stream_id, records)
        self.metrics(records)


class Ratings(Stream):
    def sync(self, ctx):
        path = "/ratings"
        ratings = ctx.client.GET(path, {}, tap_stream_id=self.tap_stream_id)
        rx = ratings.get("ratings")
        if rx is not None:
            for r in rx:
                # Lacking in core actitivity types
                r["channel_id"] = r.get("channel_id", None)
            self.write_records(rx)

all_streams = [
   Ratings("ratings", "id"),
]

all_stream_ids = ["ratings"]


def sync_lists(ctx):
    # Update Customers with updated_at_min then for
    # each customer get their activity by customer_id
    for stream in all_streams:
        if stream.direct_stream:
            stream.sync(ctx)

