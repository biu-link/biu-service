# -*- coding: utf-8 -*-

import os


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


def gen_code_by_table():
    obj = LocalCodeGen()

    table_names = [
        ('app', '第三方 App '),
        ('company', '公司'),
        ('supplier', '供应商'),
        ('template', '模板'),
        ('template_relation', '模板关联关系'),
        ('rules_relation', '规则关系'),
        ('special_relation', '特殊规则关系'),
        ('special_rules', '特殊规则'),
        ('corresponding_field', '字段对应'),
        ('reconciliation', '对账记录'),
        ('reconciliation_file', '对账文件'),
    ]
    template_root = r'D:\project\rpa\template_file'
    template_list = [
        ('controller.tpl', r'rpa-api\src\main\java\com\code\flag\controller\${table_name_pascal}Controller.java'),
        ('mapper.tpl', r'rpa-dao\src\main\java\com\code\flag\mapper\Rpa${table_name_pascal}Mapper.java'),
        ('service_interface.tpl', r'rpa-service\src\main\java\com\code\flag\base\${table_name_pascal}Service.java'),
        ('service_impl.tpl', r'rpa-service\src\main\java\com\code\flag\base\impl\${table_name_pascal}ServiceImpl.java'),
    ]
    source_root = r'D:\project\rpa\source\rpa-platform'

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


def gen_code_by_var_list():
    var_list = 'secretId,secretToken,orderNo,companyName,supplierName,currency,systemFile,supplierFile,memo'

    for var in var_list.split(','):
        # print(f'@RequestParam("{var}") String {var},')
        print(f'{var}:{var}')


if __name__ == '__main__':
    gen_code_by_table()

    # gen_code_by_var_list()
