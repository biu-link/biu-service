# -*- coding: utf-8 -*-
from common.singleton import Singleton
from model.article import Article
from util.sqlites import SqlLites

import json


class StudyingService(metaclass=Singleton):

    def __init__(self):
        super(StudyingService, self).__init__()
        SqlLites.init()

    def get_article_list(self, user_id):
        article_list = []

        rows = SqlLites().select_all("select * from t_article where user_id = ?", (user_id))
        for row in rows:
            article = Article()
            article.deserialize(row)
            article_list.append(article)
        return article_list

    def get_article(self, user_id, article_id):
        article = Article()
        row = SqlLites().select_one("select * from t_article where user_id = ? and id = ?", (user_id, article_id))
        article.deserialize(row)
        return article

    def save_article(self, json_string):
        article = json.loads(json_string)
        return SqlLites().insert('t_article', article)

    def update_article(self, json_string):
        article = json.loads(json_string)
        SqlLites().update('t_article', article, 'id')


if __name__ == '__main__':
    srv = StudyingService()

    data = {
        'id': 1,
        'user_id': 1001,
        'name': 'name_003',
        'status': 'status_3'
    }

    row_id = srv.save_article(json.dumps(data))

    art = srv.get_article(1001, row_id)
    print(art)
