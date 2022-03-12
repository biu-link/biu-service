# -*- coding: utf-8 -*-

import os

# 需要安装 pyyaml 模块
import yaml
from jinja2 import Environment, FileSystemLoader


def camel_word(word=''):
    words = word.lower().split('_')
    for i in range(1, len(words)):
        w = words[i]
        words[i] = w[0].upper() + w[1:]
    return ''.join(words)


def pascal_word(word=''):
    word = camel_word(word)
    word = word[0].upper() + word[1:]
    return word


class LocalCodeGen:

    def save_code(self, code, save_path, **kwargs):

        save_path = save_path.replace('${table_name}', kwargs['table_name'])
        save_path = save_path.replace('${table_name_pascal}', kwargs['table_name_pascal'])

        if os.path.exists(save_path):
            f = open(save_path, 'r', encoding='utf-8')
            old_content = f.read()
            f.close()

            flag = '以下内容在重新生成代码时会保留'
            if code.__contains__(flag) and old_content.__contains__(flag):
                code = code[0: code.index(flag)]
                code += old_content[old_content.index(flag):]

        f = open(save_path, 'w', encoding='utf-8')
        f.write(code)
        f.close()

    def gen_code(self, template_root):
        with open(template_root + r'\setting.yml', 'r', encoding='utf-8') as f:
            setting = yaml.load(f, Loader=yaml.CLoader)

        table_names = []
        for item in setting['table_names']:
            table_names.append((item[0], item[1]))

        template_list = []
        for item in setting['template_list']:
            template_list.append((item[0], item[1]))

        source_root = setting['source_root']

        for table in table_names:
            table_name = table[0]
            table_name_chinese = table[1]

            args = {
                'table_name': table_name,
                'table_name_chinese': table_name_chinese,
                'table_name_pascal': pascal_word(table_name),
                'table_name_camel': camel_word(table_name)
            }

            fields = self.load_fields(template_root + rf'\model\{table_name}.yml')
            args['fields'] = fields

            for template in template_list:
                template_name = template[0]
                result_file = source_root + '\\' + template[1]

                env = Environment(loader=FileSystemLoader(template_root))
                jinja_template = env.get_template(template_name)

                code = jinja_template.render(**args)
                # print(code)
                self.save_code(code, result_file, **args)

                print(f'{template_name} -- {table_name}  completed')

    def load_fields(self, yml_path):
        with open(yml_path, 'r', encoding='utf-8') as f:
            fields_setting = yaml.load(f, Loader=yaml.CLoader)

        fields = []
        for field in fields_setting['fields']:
            field_name = field[0]
            field_type = field[1] or ''
            comment = field[2]
            flag = field[3] if len(field) > 3 else ''

            if field_type.__contains__('('):
                field_type = field_type[0:field_type.index('(')]

            fields.append({
                'field_name': field_name,
                'field_name_pascal': pascal_word(field_name),
                'field_name_camel': camel_word(field_name),
                'field_type': field_type,
                'comment': comment,
                'flag': flag
            })

        return fields


def gen_code_by_var_list():
    var_list = 'secretId,secretToken,orderNo,companyName,supplierName,currency,systemFile,supplierFile,memo'

    for var in var_list.split(','):
        # print(f'@RequestParam("{var}") String {var},')
        print(f'{var}:{var}')


if __name__ == '__main__':
    # gen_code_by_table()

    # gen_code_by_var_list()

    # rpa-platform 模板
    # src = r'D:\project\rpa\template_file'

    codeGen = LocalCodeGen()

    # rpa-cloud 模板
    src = r'D:\project\rpa\source\rpa-cloud\template_file'
    codeGen.gen_code(src)
