# -*- coding: utf-8 -*-


import csv
import hashlib
import json


def calculate_md5(input_string):
    # 创建一个 md5 哈希对象
    md5_hash = hashlib.md5()

    # 更新哈希对象以包含输入字符串（需要先将字符串编码为字节）
    md5_hash.update(input_string.encode('utf-8'))

    # 获取十六进制格式的哈希值
    hex_dig = md5_hash.hexdigest()

    return hex_dig


items = []

"""

  对 hs_code 为空的行赋值，赋值逻辑为：
    如果有父级，则值为父hs_code_当前行en，如果值已存在，则在尾部加后缀 _01,_02
    如果没有父级，则值为当前行en,如果值已存在，则在尾部加后缀 _01,_02
    如果en长度大于32，则取en的md5 16进制字符串

  全部添加成功后，将数据导出为 csv，存档保存，便于下次进行比对差异
  
"""

hs_code_list = []


def load_csv():
    file_path = r'D:\doc\备忘信息\关税文件\WWWHTS_20250120.csv'
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        # 读取标题行（如果有）
        headers = next(reader, None)
        if headers:
            print(f"Headers: {headers}")

        # 逐行读取数据
        for row in reader:
            # print(row)  # 每行是一个列表，包含该行的所有字段
            hs_code = row[0]
            eng = row[1]
            chs = row[2]

            if hs_code and hs_code != '':
                hs_code_list.append(hs_code)

            indent = 0
            for c in eng:
                if c == '-':
                    indent += 1
                else:
                    break

            item = {
                'hs_code': hs_code,
                'indent': indent,
                'eng': eng,
                'chs': chs
            }
            items.append(item)
            # print(indent, hs_code, chs)


def format_hs_code(hs_code):
    if len(hs_code) > 32:
        hs_code = calculate_md5(hs_code)

    num = 2
    while hs_code_list.__contains__(hs_code):
        hs_code = hs_code + "_" + str(num)
        num += 1

    return hs_code


def fill_blank_hs_code():
    for i in range(0, len(items)):
        item = items[i]
        hs_code = item['hs_code']
        indent = item['indent']
        if indent == 0 and hs_code == '':
            hs_code = item['eng']
            item['hs_code'] = format_hs_code(hs_code)
            hs_code_list.append(item['hs_code'])


def find_item_parent(child_indent, before_index):
    last_indent = 0

    for i in range(before_index - 1, -1, -1):
        item = items[i]
        if item['indent'] < child_indent:
            return item

        # if item['indent'] > last_indent:
        #     break

        last_indent = item['indent']

    return None


def set_item_parent():
    for i in range(0, len(items)):
        item = items[i]
        if item['indent'] > 0:
            hs_code = item['hs_code']
            parent_item = find_item_parent(item['indent'], i)
            if parent_item:
                item['parent'] = parent_item['hs_code']

                if hs_code == '':
                    hs_code = f"{parent_item['hs_code']}_{item['eng']}"
                    item['hs_code'] = format_hs_code(hs_code)
                    hs_code_list.append(item['hs_code'])


def export_csv():
    rows = []

    for item in items:
        row = [item['hs_code'], item['eng'], item['chs']]
        rows.append(row)

    with open('WWWHTS_format_20250120.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # 写入多行数据
        writer.writerows(rows)


def export_json():
    obj = {}
    for item in items:
        obj[item['hs_code']] = {
            'chs': item['chs']
        }

        if item.get('parent'):
            obj[item['hs_code']]['parent'] = item['parent']

    with open('WWWHTS_20250120.json', mode='w', newline='', encoding='utf-8') as file:
        file.write(json.dumps(obj, ensure_ascii=False, indent=4))


load_csv()

fill_blank_hs_code()

set_item_parent()

export_csv()

export_json()
