import requests


# 链式调用
class api_builder(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return api_builder('%s/%s' % (self._path, path))

    def __call__(self, param=''):
        return api_builder('%s/%s' % (self._path, param))

    def __str__(self):
        return self._path

    def path(self):
        return self._path

    __repr__ = __str__


class Client:
    opendota_root = 'https://api.opendota.com/api'

    def get(self, url, params=None):
        response = requests.get(self.opendota_root + url, params=params)
        print('url: %s' % response.url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'code': response.status_code, 'message': response.content.decode()}

    def post(self, url, params=None):
        response = requests.post(self.opendota_root + url, params=params)
        print('url: %s' % response.url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'code': response.status_code, 'message': response.content.decode()}