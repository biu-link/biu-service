# -*- coding: utf-8 -*-

import util.tools as tools

import pymysql
from dbutils.pooled_db import PooledDB


class Db:
    __pool = None
    __conn = None
    __cursor = None

    def __init__(self):
        self.__conn = Db.__get_conn()
        self.__cursor = self.__conn.cursor()

    @staticmethod
    def __get_conn():
        if Db.__pool is None:
            cfg = tools.get_config_section('mysql')
            Db.__pool = PooledDB(creator=pymysql,
                                 mincached=1,
                                 maxcached=20,
                                 host=cfg.get('host'),
                                 port=cfg.get('port'),
                                 user=cfg.get('user'),
                                 passwd=cfg.get('password'),
                                 db=cfg.get('db_name'),
                                 use_unicode=True,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 setsession=['SET AUTOCOMMIT = 1']
                                 )
        return Db.__pool.connection()

    def __execute(self, sql, param=None):
        """
        @summary: 执行增删改命令
        @param sql: sql
        @param param: 参数
        @return: count 受影响的行数
        """
        if param is None:
            count = self.__cursor.execute(sql)
        else:
            count = self.__cursor.execute(sql, param)
        return count

    def select(self, sql, param=None):
        """
        :param sql: 执行的sql 语句
        :param param: 执行语句需要的参数，可以为None
        :return: 返回的是列表 + 字典
        """
        if param is None:
            count = self.__cursor.execute(sql)
        else:
            count = self.__cursor.execute(sql, param)

        if count > 0:
            result = self.__cursor.fetchall()
        else:
            result = []

        return result

    def single(self, sql, param=None):
        """
        查询并返回第 0 个元素
        :param sql: 执行的sql 语句
        :param param: 执行语句需要的参数，可以为None
        :return: 返回的是字典
        """
        rows = self.select(sql, param)
        if len(rows) > 0:
            return rows[0]

        return None

    def delete(self, sql, param=None):
        self.__execute(sql, param)

    def insert_model(self, table_name, model):
        """
        将 model 插入数据库
        :param table_name:
        :param model:
        :return:
        """
        sql = "insert into " + table_name + "("
        for key in model:
            sql += (str(key) + ",")

        sql = sql[0:len(sql) - 1]
        sql += ") values ("
        params = {}
        for key in model:
            sql += f'%({key})s,'
            params[key] = model[key]

        sql = sql[0:len(sql) - 1]
        sql += ")"

        print(sql)
        print(params)
        count = self.__execute(sql, params)
        return count

    def update_model(self, table_name, model):
        """
        将 model 更新到数据库
        :param table_name:
        :param model:
        :return:
        """
        sql = "update " + table_name + " set "

        params = {}
        for key in model:
            if key != 'id':
                sql += f'{key}=%({key})s,'
                params[key] = model[key]

        sql = sql[0:len(sql) - 1]
        sql += ' where id = %(id)s'
        params['id'] = model['id']

        print(sql)
        print(params)
        count = self.__execute(sql, params)
        return count

    def begin(self):
        """
        @summary: 开启事务
        """
        self.__conn.begin()

    def commit(self):
        """
        @summary: 提交事务
        """
        self.__conn.commit()

    def rollback(self):
        """
        @summary: 回滚事务
        """
        self.__conn.rollback()
