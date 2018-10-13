import time

import requests
# 链式调用
from requests import RequestException


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


class Client(object):
    opendota_root = 'https://api.opendota.com/api'
    sec_count = 0
    mon_count = 0

    def check_request(self):
        # TODO use redis
        now = time.localtime(time.time())
        if now.tm_sec == 0:
            self.sec_count = 0
        if now.tm_mday == 1:
            self.mon_count = 0
        if self.sec_count == 60:
            return {'code': 403, 'message': 'please request 60 calls per minute'}
        elif self.mon_count == 50000:
            return {'code': 403, 'message': 'please request 50000 calls per month'}
        else:
            self.sec_count += 1
            self.mon_count += 1

    def get(self, url, params=None):
        self.check_request()
        try:
            response = requests.get(self.opendota_root + url, params=params, timeout=10)
            print(response.status_code)
            response.raise_for_status()
            print('url: %s' % response.url)
            return response.json()
        except RequestException as e:
            print('e: ', e)
            return {'code': 500, 'message': e.__str__()}

    def post(self, url, params=None):
        response = requests.post(self.opendota_root + url, params=params)
        print('url: %s' % response.url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'code': response.status_code, 'message': response.content.decode()}
