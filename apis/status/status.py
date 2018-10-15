from apis.client import Client, api_builder
from apis.entity import Entity


class StatusEntity(Entity):
    pass


class Status(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder()

    def get_status(self, params=None):
        uri = self.uri.status.path()
        result = self.client.get(uri, params=params)

        return result

    def get_apiMetrics(self, params=None):
        uri = self.uri.admin.apiMetrics.path()
        result = self.client.get(uri, params=params)

        return result
