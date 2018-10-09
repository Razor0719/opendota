import json


class Entity(object):
    def __init__(self, dict):
        self.__dict__.update(dict)

    def __getattr__(self, item):
        return self.__dict__.get(item)

    def __repr__(self):
        return json.dumps(self.__dict__)
