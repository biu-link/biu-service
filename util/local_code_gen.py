# -*- coding: utf-8 -*-

import os

# 需要安装 pyyaml 模块
import yaml
from jinja2 import Environment, PackageLoader

class LocalCodeGen:

    def gen_code(self, table_name, table_name_chinese, template, save_path):
        table_name_pascal = self.pascal_word(table_name)
        table_name_camel = self.camel_word(table_name)

        result = template.replace('${table_name}', table_name)
        result = result.replace('${table_name_chinese}', table_name_chinese)
        result = result.replace('${table_name_pascal}', table_name_pascal)
        result = result.replace('${table_name_camel}', table_name_camel)

        save_path = save_path.replace('${table_name}', table_name)
        save_path = save_path.replace('${table_name_pascal}', table_name_pascal)

        if os.path.exists(save_path):
            f = open(save_path, 'r', encoding='utf-8')
            old_content = f.read()
            f.close()

            flag = '以下内容在重新生成代码时会保留'
            if result.__contains__(flag) and old_content.__contains__(flag):
                result = result[0: result.index(flag)]
                result += old_content[old_content.index(flag):]

        f = open(save_path, 'w', encoding='utf-8')
        f.write(result)
        f.close()

    def camel_word(self, word=''):
        words = word.lower().split('_')
        for i in range(1, len(words)):
            w = words[i]
            words[i] = w[0].upper() + w[1:]
        return ''.join(words)

    def pascal_word(self, word=''):
        word = self.camel_word(word)
        word = word[0].upper() + word[1:]
        return word


def gen_code_by_var_list():
    var_list = 'secretId,secretToken,orderNo,companyName,supplierName,currency,systemFile,supplierFile,memo'

    for var in var_list.split(','):
        # print(f'@RequestParam("{var}") String {var},')
        print(f'{var}:{var}')


def gen_code(template_root):
    with open(template_root + r'\setting.yml', 'r', encoding='utf-8') as f:
        setting = yaml.load(f, Loader=yaml.CLoader)

    print(setting)

    table_names = []
    for item in setting['table_names']:
        table_names.append((item[0], item[1]))

    template_list = []
    for item in setting['template_list']:
        template_list.append((item[0], item[1]))

    source_root = setting['source_root']

    obj = LocalCodeGen()

    for template in template_list:
        template_name = template[0]
        result_file = source_root + '\\' + template[1]

        template_file = template_root + '\\' + template_name
        f = open(template_file, 'r', encoding='utf8')
        template_content = f.read()
        f.close()

        for table in table_names:
            table_name = table[0]
            table_name_chinese = table[1]
            obj.gen_code(table_name, table_name_chinese, template_content, result_file)
            print(f'{template_name} -- {table_name}  completed')


if __name__ == '__main__':
    # gen_code_by_table()

    # gen_code_by_var_list()

    # rpa-platform 模板
    # src = r'D:\project\rpa\template_file'

    # rpa-cloud 模板
    src = r'D:\project\rpa\source\rpa-cloud\template_file'
    gen_code(src)
