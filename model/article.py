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

    def deserialize(self, params):
        self.id = params.get('id')
        self.user_id = params.get('user_id')
        self.name = params.get('name')
        self.status = params.get('status')
