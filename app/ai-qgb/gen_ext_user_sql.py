sql_template = '''
INSERT INTO `aq_ext_user` (`id`, `app_type`, `app_code`, `app_org_id`, `app_user_id`, `phone`, `username`, `status`, `ability_ids`, `expire_time`) 
VALUES ({primary_id}, 'codeflag_to_b', 'excel_import', '{app_code}', '{phone}', '{phone}', '{phone}', 'pending', '{ability_ids}', '{expire_time}');
'''


def gen_sql(primary_id, app_code, phone, ability_ids, expire_time):
    return sql_template.format(primary_id=primary_id, app_code=app_code, phone=phone, ability_ids=ability_ids, expire_time=expire_time)


def main():
    app_code = '环球捷讯'
    primary_id = 1183
    ability_ids = '1001,1003'
    expire_time = '2026-03-06 23:59:59'

    f = open('ext_user_list.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        line = line.strip().replace(' ', '')
        if line:
            phone = line
            sql = gen_sql(primary_id, app_code, phone, ability_ids, expire_time)
            primary_id += 1
            print(sql)


main()
