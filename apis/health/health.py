from apis.client import Client, api_builder
from apis.entity import Entity


class HealthEntity(Entity):
    pass


class Health(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder().health()

    def get_health(self, params=None):
        uri = self.uri.path()
        result = self.client.get(uri, params=params)

        return result
