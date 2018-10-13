from apis.client import Client, api_builder
from apis.entity import Entity


class Benchmark(Entity):
    pass


class Benchmarks(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder().benchmarks()

    def get_benchmarks(self, params=None):
        uri = self.uri.path()
        result = self.client.get(uri, params=params)
        print(uri)
        return result
