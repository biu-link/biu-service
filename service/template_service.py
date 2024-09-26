# -*- coding: utf-8 -*-
from common.singleton import Singleton
from model.template import Template
from util.mongo_db import MongoDB


class TemplateService(metaclass=Singleton):

    def __init__(self):
        super(TemplateService, self).__init__()

    def get_template_list(self, project_id):
        template_list = []
        row_list = MongoDB().select_list('template', {'project_id': project_id})
        for row in row_list:
            template = Template()
            template.deserialize(row)
            template_list.append(template)
        return template_list

    def get_template(self, template_id):
        template = Template()
        item = MongoDB().select_by_id('template', template_id)
        template.deserialize(item)
        return template


    def save_template(self, json_string):
        template = Template()
        template.from_json_string(json_string)
        MongoDB().insert('template', template.serialize())


    def update_template(self, json_string):
        template = Template()
        template.from_json_string(json_string)
        MongoDB().update('template', template.serialize())


if __name__ == '__main__':
    srv = TemplateService()
    t = {
        'file': 'a.java',
        'code': 'public class'
    }
    srv.save_template('java', 'test', t)
