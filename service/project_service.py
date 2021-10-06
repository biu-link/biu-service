# -*- coding: utf-8 -*-
import uuid

from common.singleton import Singleton
from model.project import Project
from util.mongo_db import MongoDB
from util.redis_db import RedisDB


class ProjectService(metaclass=Singleton):

    def __init__(self):
        super(ProjectService, self).__init__()

    def get_project_list(self, owner_id, user_id):
        project_list = []
        row_list = MongoDB().select_list('project', {'owner_id': owner_id})
        for row in row_list:
            project = Project()
            project.deserialize(row)
            project.token = self.get_project_token(project.id, user_id)
            project_list.append(project)
        return project_list

    def get_project_token(self, project_id, user_id):
        key = f'project_token_key_{project_id}_{user_id}'
        token = RedisDB().get(key)
        if not token:
            token = str(uuid.uuid1()).replace('-', '')
            RedisDB().set(key, token)
            token_key = f'project_token_key_{token}'
            RedisDB().set(token_key, project_id)
        return token

    def get_project(self, project_id):
        project = Project()
        item = MongoDB().select_by_id('project', project_id)
        project.deserialize(item)
        return project

    def save_project(self, json_string, owner_id):
        project = Project()
        project.from_json_string(json_string)
        project.owner_id = owner_id
        MongoDB().insert('project', project.serialize())

    def update_project(self, json_string):
        project = Project()
        project.from_json_string(json_string)
        MongoDB().update('project', project.serialize())
