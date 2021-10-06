# -*- coding: utf-8 -*-
from common.abstract_model import AbstractModel
from model.code_item import CodeItem
from model.params import Param


class Template(AbstractModel):
    """
    模板信息
    """

    def __init__(self):
        self.id = None
        self.project_id = None
        self.name = None
        self.abbr = None
        self.setting = None
        self.params = None
        self.code_items = None

    def deserialize(self, params):
        self.id = params.get('id')
        self.project_id = params.get('project_id')
        self.name = params.get('name')
        self.abbr = params.get('abbr')
        self.setting = params.get('setting')
        self.params = []
        self.code_items = []
        if params.get('params') is not None:
            for item in params.get("params"):
                obj = Param()
                obj.deserialize(item)
                self.params.append(obj)

        if params.get('code_items') is not None:
            for item in params.get("code_items"):
                obj = CodeItem()
                obj.deserialize(item)
                self.code_items.append(obj)
