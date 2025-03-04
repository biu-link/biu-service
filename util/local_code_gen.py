# -*- coding: utf-8 -*-

import os
import time

# 需要安装 pyyaml 模块
import yaml
from jinja2 import Environment, FileSystemLoader
from util.mysql_db import MysqlDB


def is_all_upper(word):
    return word.upper() == word


def camel_word(word=''):
    if word.__contains__('_') or is_all_upper(word):
        words = word.lower().split('_')
        for i in range(1, len(words)):
            w = words[i]
            words[i] = w[0].upper() + w[1:]
        return ''.join(words)

    return word[0].lower() + word[1:]


def pascal_word(word=''):
    word = camel_word(word)
    word = word[0].upper() + word[1:]
    return word


def hyphen_word(word=''):
    return word.replace('_', '-').lower()


def quote(str, q='\''):
    return q + str + q


def fmt(str, format='%s'):
    return format % str


class LocalCodeGen:

    def save_code(self, code, save_path, **kwargs):

        for var in kwargs:
            if kwargs[var] is not None and isinstance(kwargs[var], str):
                save_path = save_path.replace('${' + var + '}', kwargs[var])

        if os.path.exists(save_path):
            if kwargs.get('flag_once') == '1':
                return

            f = open(save_path, 'r', encoding='utf-8')
            old_content = f.read()
            f.close()

            flag = '以下内容在重新生成代码时会保留'
            if code.__contains__(flag) and old_content.__contains__(flag):
                code = code[0: code.index(flag)]
                code += old_content[old_content.index(flag):]

        dirname = os.path.dirname(save_path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        f = open(save_path, 'w', encoding='utf-8')
        f.write(code)
        f.close()

    def gen_code(self, template_root, source_root=None, table_names=None, db_schema=None, remove_table_prefix=None, vars=None):
        with open(template_root + r'\setting.yml', 'r', encoding='utf-8') as f:
            setting = yaml.load(f, Loader=yaml.CLoader)

        if table_names is None:
            table_names = []
            for item in setting['table_names']:
                table_names.append(item)

        template_list = setting['template_list']

        if source_root is None:
            source_root = setting['source_root']

        ignore_fields_name = setting.get('ignore_fields_name')
        insert_ignore_fields_name = setting.get('insert_ignore_fields_name')
        update_ignore_fields_name = setting.get('update_ignore_fields_name')
        where_ignore_fields_name = setting.get('where_ignore_fields_name')
        where_must_fields_name = setting.get('where_must_fields_name')

        env_vars = setting.get('env_vars')

        for table in table_names:
            origin_table_name = table[0]
            table_name_chinese = table[1]

            table_name = origin_table_name
            if remove_table_prefix and table_name.startswith(remove_table_prefix):
                table_name = table_name[len(remove_table_prefix):]

            args = {
                'origin_table_name': origin_table_name,
                'table_name': table_name,
                'table_name_minus': table_name.replace('_', '-'),
                'table_name_path': table_name.replace('_', '/'),
                'table_name_chinese': table_name_chinese,
                'table_name_pascal': pascal_word(table_name),
                'table_name_camel': camel_word(table_name),
                'parent_menu_name': setting.get('parent_menu_name'),
                'menu_name': setting.get('menu_name'),
            }

            if env_vars:
                args = dict(args, **env_vars)

            if vars:
                args = dict(args, **vars)

            print(args)

            table_setting_yml_path = template_root + rf'\model\{table_name}.yml'
            if os.path.exists(table_setting_yml_path):
                with open(table_setting_yml_path, 'r', encoding='utf-8') as f:
                    table_setting = yaml.load(f, Loader=yaml.CLoader)
            else:
                table_setting = get_db_fields(db_schema, origin_table_name)

            args['fields'] = self.load_fields(table_setting['fields'], ignore_fields_name)
            args['insert_fields'] = self.load_fields(table_setting['fields'], insert_ignore_fields_name)
            args['update_fields'] = self.load_fields(table_setting['fields'], update_ignore_fields_name)
            args['where_fields'] = self.load_fields(table_setting['fields'], where_ignore_fields_name)
            args['where_must_fields'] = self.load_fields(table_setting['fields'], None, where_must_fields_name)

            # 获取 tabel_name.yml 文件中设置的 table 级别的参数
            table_args = self.load_args(table_setting.get('args'))
            if table_args is None:
                table_args = {}

            for template in template_list:
                template_name = template[0]
                template_output = template[1]

                template_flag = template[2] if len(template) > 2 else ''
                template_flags = self.parse_flag(template_flag)
                if template_flags is None:
                    template_flags = {}

                result_file = source_root + '\\' + template_output

                env = Environment(loader=FileSystemLoader(template_root))
                env.filters["quote"] = quote
                env.filters["fmt"] = fmt

                jinja_template = env.get_template(template_name)

                final_args = {
                    **args,
                    **table_args,
                    **template_flags,
                }

                if final_args.get('pk_id') is None:
                    final_args['pk_id'] = 'id'

                code = jinja_template.render(**final_args)
                if template_output == 'console':
                    print(code)
                else:
                    self.save_code(code, result_file, **final_args)

                print(f'-- {template_name} -- {table_name}  completed')

    def gen_component(self, template_root):
        with open(template_root + r'\setting.yml', 'r', encoding='utf-8') as f:
            setting = yaml.load(f, Loader=yaml.CLoader)

        component_list = setting['component_list']
        source_root = setting['source_root']
        component_dir = setting['component_dir']
        component_model = setting['component_model']
        component_name = setting['component_name']

        args = {
            'component_dir': component_dir,
            'component_model': component_model,
            'component_name': component_name,
            'component_name_camel': camel_word(component_name),
            'component_name_pascal': pascal_word(component_name),
            'component_name_hyphen': hyphen_word(component_name),
        }

        for template in component_list:
            template_name = template[0]
            template_output = template[1]

            result_file = source_root + '\\' + template_output

            env = Environment(loader=FileSystemLoader(template_root))
            jinja_template = env.get_template(template_name)
            code = jinja_template.render(**args)
            self.save_code(code, result_file, **args)

            print(f'-- {template_name} -- {component_name}  completed')

    def load_fields(self, fields_setting, ignore_fields_name, just_fields_name=None):

        if ignore_fields_name is None:
            ignore_fields_name = []

        fields = []
        last_field_name = ''
        for field in fields_setting:
            field_name = field[0]

            if ignore_fields_name.__contains__(field_name):
                continue

            if just_fields_name is not None and just_fields_name.__contains__(field_name) is False:
                continue

            field_db_type = field[1] or ''
            comment = field[2]
            flag = field[3] if len(field) > 3 else ''
            default_value = field[4] if len(field) > 4 else None

            field_length = ''

            if field_db_type.__contains__('('):
                field_length = field_db_type[field_db_type.index('(') + 1:field_db_type.index(')')]
                field_type = field_db_type[0:field_db_type.index('(')].lower()
            else:
                field_type = field_db_type

            java_type = ''
            jdbc_type = ''
            ts_type = ''
            if field_type in ['varchar', 'text', 'mediumtext', 'longtext']:
                java_type = 'String'
                jdbc_type = 'VARCHAR'
                ts_type = 'string'
            elif field_type in ['int']:
                java_type = 'Integer'
                jdbc_type = 'INTEGER'
                ts_type = 'number'
            elif field_type in ['tinyint']:
                java_type = 'Integer'
                jdbc_type = 'TINYINT'
                ts_type = 'number'
            elif field_type == 'bigint':
                java_type = 'Long'
                jdbc_type = 'BIGINT'
                ts_type = 'string'
            elif field_type == 'decimal':
                java_type = 'Double'
                jdbc_type = 'DECIMAL'
                ts_type = 'number'
            elif field_type == 'date':
                java_type = 'Date'
                jdbc_type = 'DATE'
                ts_type = 'string'
            elif field_type == 'datetime':
                java_type = 'Date'
                jdbc_type = 'TIMESTAMP'
                ts_type = 'string'

            if field_type in ['text', 'mediumtext', 'longtext']:
                jdbc_type = 'LONGVARCHAR'

            if flag.__contains__('NOT_NULL'):
                null_default = f"NOT NULL"
            else:
                null_default = f"NULL"

            if default_value is not None:
                null_default = null_default + f" DEFAULT '{default_value}'"

            collate = ''
            if field_type == 'varchar':
                collate = "COLLATE 'utf8mb4_general_ci'"

            fields.append({
                'field_name': field_name,
                'field_name_with_prefix': 'prefix_' + field_name,
                'field_name_pascal': pascal_word(field_name),
                'field_name_camel': camel_word(field_name),
                'field_name_lower': field_name.lower(),
                'field_db_type': field_db_type,
                'field_type': field_type,
                'field_length': field_length,
                'java_type': java_type,
                'jdbc_type': jdbc_type,
                'ts_type': ts_type,
                'comment': comment,
                'flag': flag,
                'null_default': null_default,
                'collate': collate,
                'after_field_name': last_field_name
            })

            last_field_name = field_name

        # print(fields)
        # exit()
        return fields

    def load_args(self, args_setting):

        if args_setting is None:
            return None

        args = {}
        for arg in args_setting:
            args[arg[0]] = arg[1]

        return args

    @staticmethod
    def parse_flag(flag_string):
        args = {}
        if flag_string:
            flags = flag_string.split(',')
            if len(flags) > 0:
                for flag in flags:
                    kv = flag.split('=')
                    args[kv[0]] = kv[1]

        return args


def gen_code_by_var_list():
    var_list = 'secretId,secretToken,orderNo,companyName,supplierName,currency,systemFile,supplierFile,memo'

    for var in var_list.split(','):
        # print(f'@RequestParam("{var}") String {var},')
        print(f'{var}:{var}')


def get_db_table_names(db_name, table_names=None):
    mysql = MysqlDB()
    sql = f"""SELECT TABLE_NAME, TABLE_COMMENT
FROM information_schema.`TABLES`
WHERE TABLE_SCHEMA = '{db_name}'
and TABLE_NAME not like 'xxx%'
and TABLE_NAME not like '\\_%'"""

    if table_names:
        arr = table_names.split(',')
        if len(arr) > 0:
            tables = ','.join(f"'{table}'" for table in arr)
            sql = sql + f" and TABLE_NAME in ({tables})"

    print(sql)
    rows = mysql.select(sql)

    return list(map(lambda x: [x['TABLE_NAME'], x['TABLE_COMMENT']], rows))


def get_db_fields(db_schema, table_name):
    mysql = MysqlDB()
    sql = f"""SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_COMMENT
FROM information_schema.COLUMNS
WHERE TABLE_NAME = '{table_name}' and TABLE_SCHEMA = '{db_schema}'
order by ordinal_position"""

    rows = mysql.select(sql)

    fields = []
    for row in rows:
        fields.append([row['COLUMN_NAME'], row['COLUMN_TYPE'], row['COLUMN_COMMENT']])

    return {
        "fields": fields
    }


if __name__ == '__main__':
    # gen_code_by_table()

    # gen_code_by_var_list()

    # rpa-platform 模板
    # src = r'D:\project\rpa\template_file'

    codeGen = LocalCodeGen()

    # rpa-cloud 模板
    # src = r'D:\project\rpa\source\rpa-cloud-codegen\template_file'

    # 招商局融通模板
    # src = r'D:\project\zhuang\source\zsjrt-api-codegen\template_file'
    # codeGen.gen_code(src, False)  # for not console
    # codeGen.gen_code(src, True)  # for console

    # codeGen.gen_component(src)

    # 明材模板
    # src = r'D:\project\mingcai\source\template_file'
    # codeGen.gen_code(src)

    # 天文底片模板
    # src = r'D:\project\wang\legacyplate\legacyplate-sanic-server\template_file'
    # codeGen.gen_code(src)

    # 掩星模板
    # src = r'D:\project\wang\gnss\gnss-sanic-server\template_file'
    # codeGen.gen_code(src)

    # 碎片模板
    # src = r'D:\project\wang\satod-neas\satod-sanic-server\template_file'
    # codeGen.gen_code(src)

    # table_names = get_db_table_names('satod')
    # src = r'D:\project\mingcai\source\mint-admin-vue3\template_file'
    # source_root = r'D:\project\mingcai\source\mint-admin-vue3-gen-code'
    # codeGen.gen_code(src, source_root, table_names, 'satod')

    # 明材模板 前端
    # include_table_names = 'lesson'
    # table_names = get_db_table_names('mint', include_table_names)
    # src = r'D:\source\mint-admin\template_file'
    # source_root = r'D:\source\mint-admin-vue3-gen-code'
    # # source_root = r'D:\source\mint-admin'
    # codeGen.gen_code(src, source_root, table_names, 'mint')
    #
    # # 明材模板 后端
    # table_names = get_db_table_names('mint', include_table_names)
    # src = r'D:\source\template_file'
    # source_root = r'D:\source\mint-server\ser

    # 前端
    include_table_names = ''
    table_names = get_db_table_names('ai_qgb_dev', include_table_names)
    template_src = r'D:\source\code-template\web'
    source_root = r'D:\source\ai-qgb-mini-program'
    remove_table_prefix = 'aq_'
    codeGen.gen_code(template_src, source_root, table_names, 'ai_qgb_dev', remove_table_prefix)

    # 后端
    template_src = r'D:\source\code-template\java'
    remove_table_prefix = 'aq_'

    groups = [
        {
            'source_root': r'D:\source\ai-qgb-mini-program-api\commons\auth',
            'vars': {
                'module_name': 'auth'
            },
            'include_table_names': '-'  # 'aq_user,aq_sys_user'
        },
        {
            'source_root': r'D:\source\ai-qgb-mini-program-api\modules\ai-qgb-api',
            'vars': {
                'module_name': 'aiqgb'
            },
            'include_table_names': 'aq_product,aq_order,aq_group_buy_order,aq_message_template,aq_message_task,aq_message_history'
        },
    ]

    for item in groups:
        table_names = get_db_table_names('ai_qgb_dev', item['include_table_names'])
        codeGen.gen_code(template_src, item['source_root'], table_names, 'ai_qgb_dev', remove_table_prefix, item['vars'])

    # d:
    # cd D:\source\biu-service
    # set PYTHONPATH=%PYTHONPATH%;D:\source\biu-service
    # python util\local_code_gen.py

    # while True:
    #     codeGen.gen_code(src, source_root, table_names, 'mint')
    #     time.sleep(2)
