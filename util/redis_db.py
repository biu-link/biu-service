# -*- coding: utf-8 -*-

import util.tools as tools
import redis
import json

from common.singleton import Singleton


class RedisDB(metaclass=Singleton):
    __pool = None

    def __init__(self):
        super(RedisDB, self).__init__()
        cfg = tools.get_config_section('redis')
        host = cfg.get('host')
        port = cfg.get('port')
        password = cfg.get('password')
        self.__pool = redis.ConnectionPool(max_connections=10, host=host, port=port, password=password, decode_responses=True)
        self.r = redis.Redis(connection_pool=self.__pool)

    def get(self, key):
        return self.r.get(key)

    def get_json(self, key):
        value = self.r.get(key)
        if value:
            return json.loads(value)

        return None

    def set(self, key, value, expire_seconds=None):
        self.r.set(key, value, ex=expire_seconds)
        return

    def delete(self, key):
        self.r.delete(key)
