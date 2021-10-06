# -*- coding: utf-8 -*-
from common.abstract_model import AbstractModel


class User(AbstractModel):
    """
    项目信息
    """

    def __init__(self):
        self.id = None
        self.email = None

    def deserialize(self, params):
        self.id = params.get('id')
        self.email = params.get('email')

