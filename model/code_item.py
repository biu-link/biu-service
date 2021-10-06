# -*- coding: utf-8 -*-
from common.abstract_model import AbstractModel


class CodeItem(AbstractModel):

    def __init__(self):
        self.name = None
        self.file = None
        self.code = None

    def deserialize(self, params):
        self.name = params.get('name')
        self.file = params.get('file')
        self.code = params.get('code')
