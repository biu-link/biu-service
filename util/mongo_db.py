# -*- coding: utf-8 -*-

import util.tools as tools

import pymongo

from common.singleton import Singleton
from bson.objectid import ObjectId

class MongoDB(metaclass=Singleton):
    __db = None

    def __init__(self):
        super(MongoDB, self).__init__()
        self.__db = MongoDB.__get_db()

    @staticmethod
    def __get_db():
        cfg = tools.get_config_section('mongo')
        mongo_db = cfg.get('db_name')
        client = pymongo.MongoClient(cfg.get('host'), cfg.get('port'))
        db = client[mongo_db]
        db.authenticate(cfg.get('user'), cfg.get('password'), mechanism=cfg.get('mechanism'))
        return db

    def insert(self, collection, data):
        collection = self.__db[collection]
        ret = collection.insert_one(data)
        print(ret)

    def update(self, collection, data):
        collection = self.__db[collection]
        object_id = ObjectId(data['id'])
        del data['id']
        ret = collection.update_one({'_id': object_id}, {'$set': data})
        print(ret)

    def select_by_id(self, collection, object_id):
        collection = self.__db[collection]
        ret = collection.find_one(ObjectId(object_id))
        if ret:
            ret['id'] = str(ret['_id'])
            del ret['_id']
        return ret

    def select_one(self, collection, condition):
        collection = self.__db[collection]
        ret = collection.find_one(condition)
        if ret:
            ret['id'] = str(ret['_id'])
            del ret['_id']
        return ret

    def select_list(self, collection, condition):
        collection = self.__db[collection]
        cursor = collection.find(condition)
        rows = []
        if cursor:
            rows = list(cursor)
            for row in rows:
                row['id'] = str(row['_id'])
                del row['_id']
        return rows
