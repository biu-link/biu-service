# -*- coding: utf-8 -*-
from common.singleton import Singleton
from model.article import Article
from model.sentence import Sentence
from model.word import Word
from util.sqlites import SqlLites
from util.times import Times
from util.web_exception import WebException

import json
import re


class StudyingService(metaclass=Singleton):

    def __init__(self):
        super(StudyingService, self).__init__()
        SqlLites.init()

    def get_article_list(self, user_id):
        article_list = []

        rows = SqlLites().select_all("select * from t_article where user_id = ?", (user_id,))
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

    def update_article(self, article):
        SqlLites().update('t_article', article, 'id,user_id')

    def delete_article(self, user_id, article_id):
        SqlLites().execute(f"delete from t_article where user_id=? and id=?", (user_id, article_id))

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
            last_sentence_line_num='',
            create_time=Times.current_datetime()
        )
        article_id = SqlLites().insert('t_article', article)

        lines = re.split('[\\r|\\n]', content)
        line_num = 100
        for line in lines:
            if not line:
                continue
            line_num += 1
            sentence = dict(
                user_id=user_id,
                article_id=article_id,
                content=line,
                line_num=str(line_num)
            )
            SqlLites().insert('t_sentence', sentence)

        return article_id

    def insert_word(self, user_id, word, sentence_id, article_id):

        rows = SqlLites().select_all(
            "select t_word.* from t_word join t_word_sentence on t_word.id = t_word_sentence.word_id"
            " where t_word.user_id = ?"
            " and t_word.content = ? "
            " and t_word_sentence.article_id = ? "
            " order by id", (user_id, word, article_id))

        if len(rows) > 0:
            raise WebException(code=400, msg=f'{word} 已存在')

        word = dict(
            user_id=user_id,
            content=word,
            status='new'
        )
        word_id = SqlLites().insert('t_word', word)

        word_sentence = dict(
            user_id=user_id,
            word_id=word_id,
            sentence_id=sentence_id,
            article_id=article_id
        )
        SqlLites().insert('t_word_sentence', word_sentence)
        return word_id

    def update_word(self, word):

        rows = SqlLites().select_all(
            "select t_word.* from t_word join t_word_sentence on t_word.id = t_word_sentence.word_id"
            " where t_word.user_id = ?"
            " and t_word.content = ? "
            " and t_word_sentence.article_id = ? "
            " and t_word.id != ? ", (word['user_id'], word['content'], word['article_id'], word['id']))

        if len(rows) > 0:
            raise WebException(code=400, msg=f"{word['content']} 已存在")

        del word['article_id']

        SqlLites().update('t_word', word, 'id,user_id')

    def get_word_list(self, user_id, article_id, status):
        word_list = []

        rows = SqlLites().select_all(
            "select t_word.* from t_word join t_word_sentence on t_word.id = t_word_sentence.word_id"
            " where t_word.user_id = ?"
            " and t_word_sentence.article_id = ? "
            " and t_word.status = ?"
            " order by id", (user_id, article_id, status))

        for row in rows:
            word = Word()
            word.deserialize(row)
            word_list.append(word)
        return word_list

    def delete_word(self, user_id, word_id):
        SqlLites().execute(f"delete from t_word where user_id=? and id=?", (user_id, word_id))
        SqlLites().execute(f"delete from t_word_sentence where user_id=? and word_id=?", (user_id, word_id))


if __name__ == '__main__':
    srv = StudyingService()

    # srv.insert_word(1001, 'word', 1, 1)

    word_list = srv.get_word_list(1001, 1, 'new')
    print(word_list)
