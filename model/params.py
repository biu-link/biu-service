# -*- coding: utf-8 -*-
from common.abstract_model import AbstractModel


class Param(AbstractModel):

    def __init__(self):
        self.name = None
        self.desc = None

    def deserialize(self, params):
        self.name = params.get('name')
        self.desc = params.get('desc')
