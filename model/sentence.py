# -*- coding: utf-8 -*-

from common.abstract_model import AbstractModel


class Sentence(AbstractModel):
    """
    句子信息
    """

    def __init__(self):
        self.id = None
        self.user_id = None
        self.article_id = None
        self.content = None
        self.line_num = None
        self.note = None
        self.translation = None

    def deserialize(self, params):
        self.id = params.get('id')
        self.user_id = params.get('user_id')
        self.article_id = params.get('article_id')
        self.content = params.get('content')
        self.line_num = params.get('line_num')
        self.note = params.get('note')
        self.translation = params.get('translation')
