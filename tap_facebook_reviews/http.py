import requests
import backoff
from singer import metrics
from datetime import datetime, timedelta
import time

BASE_URL = "https://graph.facebook.com/"


class RateLimitException(Exception):
    pass


def _join(a, b):
    return a.rstrip("/") + "/" + b.lstrip("/")


TIME_BETWEEN_REQUESTS = timedelta(microseconds=10e3)
# > 10ms can help avoid performance issues


class Client(object):
    def __init__(self, config):
        self.session = requests.Session()
        self.token = config["facebook_access_token"]
        self.next_request_at = datetime.now()
        self.user_agent = None

    def prepare_and_send(self, request):
        if self.user_agent:
            request.headers["User-Agent"] = self.user_agent
        return self.session.send(request.prepare())

    def url(self, path, user_id):
        path_with_user_id = _join(user_id, path)
        url = _join(BASE_URL, path_with_user_id)
        return "{0}?access_token={1}".format(url, self.token)

    def create_get_request(self, path, **kwargs):
        return requests.Request(method="GET",
                                # TODO(ian): replace the user_id below with something
                                url=self.url(path, "Packlane"),
                                **kwargs)

    @backoff.on_exception(backoff.expo,
                          RateLimitException,
                          max_tries=10,
                          factor=2)
    def request_with_handling(self, request, tap_stream_id):
        wait = (self.next_request_at - datetime.now()).total_seconds()
        if wait > 0:
            time.sleep(wait)

        with metrics.http_request_timer(tap_stream_id) as timer:
            response = self.prepare_and_send(request)
            self.next_request_at = datetime.now() + TIME_BETWEEN_REQUESTS
            timer.tags[metrics.Tag.http_status_code] = response.status_code
        if response.status_code in [429, 503]:
            raise RateLimitException()
        response.raise_for_status()
        return response.json()

    def GET(self, path, request_kwargs, *args, **kwargs):
        req = self.create_get_request(path, **request_kwargs)
        return self.request_with_handling(req, *args, **kwargs)
