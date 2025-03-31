# -*- coding: utf-8 -*-

import util.tools as tools
import redis
import json


class RedisDB:
    __pool = None

    def __init__(self, config=None):
        super(RedisDB, self).__init__()
        if config:
            pass
        else:
            config = tools.get_config_section('redis')

        host = config.get('host')
        port = config.get('port')
        password = config.get('password')
        database = config.get('database')

        self.__pool = redis.ConnectionPool(max_connections=10, host=host, port=port, password=password, db=database, decode_responses=True)
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

    def keys(self, pattern):
        return self.r.keys(pattern)

    def expire(self, key, seconds):
        self.r.expire(key, seconds)
