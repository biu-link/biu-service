# -*- coding: utf-8 -*-
import os.path
import sqlite3
import re

DB_FILE = 'sqlite.db'

DB_SCRIPTS = [
    [1,
     """
     create table t_config(name TEXT PRIMARY KEY NOT NULL, value Text);
     insert into t_config(name, value) values('version', '1');
    """],

    [2,
     """
     create table t_article(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT);
    """],

    [3,
     """
     alter table t_article add column status TEXT;
    """],

    [4,
     """
     alter table t_article add column user_id INTEGER;
    """],

    [5,
     """
     alter table t_article add column category TEXT;
     alter table t_article add column last_sentence_id INTEGER;
     alter table t_article add column media_path INTEGER;
     alter table t_article add column create_time TEXT;
     
     create table t_sentence(
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     user_id INTEGER,
     article_id INTEGER,
     line_num TEXT, 
     content TEXT,
     note TEXT
     );
     
     create table t_word(
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     user_id INTEGER,
     content TEXT,
     note TEXT,
     status TEXT,
     category TEXT     
     );
     
     create table t_word_sentence(
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     user_id INTEGER,
     word_id INTEGER,
     sentence_id INTEGER
     );     
     
    """],

]


def get_connection():
    folder = os.path.dirname(__file__)
    conn = sqlite3.connect(f'{folder}/{DB_FILE}')
    conn.row_factory = row_factory
    return conn


def row_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class SqlLites:

    @staticmethod
    def execute(sql, params=None):
        conn = get_connection()
        c = conn.cursor()
        ret = 0
        if params:
            ret = c.execute(sql, params)
        else:
            ret = c.execute(sql)
        conn.commit()
        conn.close()
        return ret.rowcount

    @staticmethod
    def execute_insert(sql, params=None):

        conn = get_connection()
        c = conn.cursor()
        if params:
            c.execute(sql, params)
        else:
            c.execute(sql)
        ret = c.lastrowid
        conn.commit()
        conn.close()
        return ret

    @staticmethod
    def executescript(sql):
        conn = get_connection()
        c = conn.cursor()
        print(sql)
        c.executescript(sql)
        conn.commit()
        conn.close()

    @staticmethod
    def select_one(sql, params=None):
        conn = get_connection()
        c = conn.cursor()
        if params:
            c.execute(sql, params)
        else:
            c.execute(sql)
        row = c.fetchone()
        conn.commit()
        conn.close()
        return row

    @staticmethod
    def select_all(sql, params=None):
        print(sql)
        conn = get_connection()
        c = conn.cursor()
        if params:
            c.execute(sql, params)
        else:
            c.execute(sql)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    @staticmethod
    def init():
        tables = SqlLites.select_all("select name from sqlite_master where type='table'")
        version = 0
        if len(tables) > 0:
            row = SqlLites.select_one("select value as value from t_config where name='version'")
            version = int(row['value'])
        SqlLites.update_db(version)

    @staticmethod
    def update_db(current_version):

        has_error = False
        version = None

        for script in DB_SCRIPTS:
            version = script[0]
            if current_version < version:
                content = script[1]
                sqls = content.split(';')
                for sql in sqls:
                    try:
                        SqlLites.executescript(sql)
                    except Exception as e:
                        print(e)
                        error = str(e)
                        if not error.__contains__('already exists') \
                                and not error.__contains__('duplicate column name'):
                            has_error = True

        if not has_error:
            SqlLites.update_version(version)

    @staticmethod
    def update_version(version):
        SqlLites.execute("update t_config set value=? where name='version'", str(version))

    @staticmethod
    def insert(table_name, model):

        if isinstance(model, dict):
            keyValues = model
        else:
            keyValues = model.__dict__

        keys = list(filter(lambda x: x != 'id', keyValues.keys()))
        fields = ','.join(keys)

        values = list(map(lambda x: '?', keys))
        values = ','.join(values)

        params = ()
        for key in keys:
            params = params + (keyValues.get(key),)

        sql = f"insert into {table_name}({fields}) values({values})"
        new_id = SqlLites.execute_insert(sql, params)
        return new_id

    @staticmethod
    def update(table_name, model, where_fields='id'):

        if isinstance(model, dict):
            keyValues = model
        else:
            keyValues = model.__dict__

        where_fields = re.sub('\\s', '', where_fields)
        where_fields = where_fields.split(',')

        values = []
        params = ()

        for key in keyValues.keys():
            if key not in where_fields:
                values.append(f"{key} = ?")
                params = params + (keyValues.get(key),)
        values = ','.join(values)

        where = []
        for key in where_fields:
            where.append(f"{key} = ?")
            params = params + (keyValues.get(key),)
        where = ' and '.join(where)

        sql = f"update {table_name} set {values} where {where}"
        print(sql)
        SqlLites.execute(sql, params)


if __name__ == '__main__':
    # print(__file__)
    path = os.path.dirname(__file__)
    print(path)

    SqlLites.init()
    r = SqlLites.select_one('select * from t_config')
    print(r)
