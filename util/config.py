# -*- coding:utf-8 -*-

import os
import configparser


class Config(object):

    config_file_path = ''

    def __init__(self, work_dir, config_filename):
        file_path = os.path.join(work_dir, config_filename)
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path, encoding="utf-8-sig")
        self.config_file_path = file_path

    def get_sections(self):
        return self.cf.sections()

    def get_options(self, section):
        return self.cf.options(section)

    def get_content(self, section):
        result = {}
        for option in self.get_options(section):
            value = self.cf.get(section, option)
            result[option] = int(value) if value.isdigit() else value
        return result

    def set_content(self, section, option, value):
        self.cf.set(section, option, value)
        self.cf.write(open(self.config_file_path, 'w', encoding='utf-8-sig'))
