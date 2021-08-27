# -*- coding: utf-8 -*-

from util.db import Db


class TemplateService:
    db = None

    def __init__(self):
        self.db = Db()

    def get_template(self, lang, name):
        template = self.db.single(f"select * from ba_default_template where lang = %(lang)s and name = %(name)s",
                                  {
                                      'lang': lang,
                                      'name': name
                                  })
        return template
