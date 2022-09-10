# -*- coding: utf-8 -*-

from common.abstract_model import AbstractModel


class Article(AbstractModel):
    """
    文章信息
    """

    def __init__(self):
        self.id = None
        self.user_id = None
        self.name = None
        self.status = None
        self.category = None
        self.last_sentence_line_num = None
        self.media_path = None
        self.create_time = None

    def deserialize(self, params):
        self.id = params.get('id')
        self.user_id = params.get('user_id')
        self.name = params.get('name')
        self.status = params.get('status')
        self.category = params.get('category')
        self.last_sentence_line_num = params.get('last_sentence_line_num')
        self.media_path = params.get('media_path')
        self.create_time = params.get('create_time')
