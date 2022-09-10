# -*- coding: utf-8 -*-

from common.abstract_model import AbstractModel


class Word(AbstractModel):
    """
    句子信息
    """

    def __init__(self):
        self.id = None
        self.user_id = None
        self.content = None
        self.note = None
        self.status = None
        self.category = None

    def deserialize(self, params):
        self.id = params.get('id')
        self.user_id = params.get('user_id')
        self.content = params.get('content')
        self.note = params.get('note')
        self.status = params.get('status')
        self.category = params.get('category')
