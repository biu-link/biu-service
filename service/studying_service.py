# -*- coding: utf-8 -*-
from common.singleton import Singleton
from model.article import Article
from model.sentence import Sentence
from util.sqlites import SqlLites
from util.times import Times

import json
import re


class StudyingService(metaclass=Singleton):

    def __init__(self):
        super(StudyingService, self).__init__()
        SqlLites.init()

    def get_article_list(self, user_id):
        article_list = []

        rows = SqlLites().select_all("select * from t_article where user_id = ?", (user_id, ))
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

    def insert_article(self, article):
        article['create_time'] = Times.current_datetime()
        return SqlLites().insert('t_article', article)

    def update_article(self, json_string):
        article = json.loads(json_string)
        SqlLites().update('t_article', article, 'id,user_id')

    def get_sentence_list(self, user_id, article_id):
        sentence_list = []

        rows = SqlLites().select_all("select * from t_sentence where user_id = ? and article_id = ? order by line_num", (user_id, article_id))
        for row in rows:
            sentence = Sentence()
            sentence.deserialize(row)
            sentence_list.append(sentence)
        return sentence_list

    def get_sentence(self, user_id, sentence_id):
        sentence = Sentence()
        row = SqlLites().select_one("select * from t_sentence where user_id = ? and id = ?", (user_id, sentence_id))
        sentence.deserialize(row)
        return sentence

    def insert_sentence(self, json_string):
        sentence = json.loads(json_string)
        return SqlLites().insert('t_sentence', sentence)

    def update_sentence(self, json_string):
        sentence = json.loads(json_string)
        SqlLites().update('t_sentence', sentence, 'id,user_id')

    def insert_article_and_sentence(self, user_id, article_name, content):
        article = dict(
            user_id=user_id,
            name=article_name,
            status='new',
            last_sentence_id=-1,
            create_time=Times.current_datetime()
        )
        article_id = SqlLites().insert('t_article', article)

        lines = re.split('[\\r|\\n]', content)
        line_num = 100
        for line in lines:
            line_num += 1
            sentence = dict(
                user_id=user_id,
                article_id=article_id,
                content=line,
                line_num=str(line_num)
            )
            SqlLites().insert('t_sentence', sentence)

        return article_id


if __name__ == '__main__':
    srv = StudyingService()

    srv.insert_article_and_sentence(1001, 'test', 'abc\n123\ndef\n789\nxyz')
