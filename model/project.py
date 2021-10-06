# -*- coding: utf-8 -*-
from common.abstract_model import AbstractModel


class Project(AbstractModel):
    """
    项目信息
    """

    def __init__(self):
        self.id = None
        self.name = None
        self.lang = None
        self.owner_id = None
        self.token = None

    def deserialize(self, params):
        self.id = params.get('id')
        self.name = params.get('name')
        self.lang = params.get('lang')
        self.owner_id = params.get('owner_id')

