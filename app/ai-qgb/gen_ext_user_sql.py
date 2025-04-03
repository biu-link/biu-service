from util.mysql_db import MysqlDB

sql_template = '''
INSERT INTO `aq_ext_user` (`id`, `app_type`, `app_code`, `app_org_id`, `app_user_id`, `phone`, `username`, `status`, `ability_ids`, `expire_time`) 
VALUES ({primary_id}, 'codeflag_to_b', 'excel_import', '{app_code}', '{phone}', '{phone}', '{name}', 'pending', '{ability_ids}', '{expire_time}');
'''


def gen_sql(primary_id, app_code, phone, name, ability_ids, expire_time):
    return sql_template.format(primary_id=primary_id, app_code=app_code, phone=phone, name=name, ability_ids=ability_ids, expire_time=expire_time)


def main():
    mysql = MysqlDB('mysql_prod')

    sql = 'select max(id) last_id from aq_ext_user'
    row = mysql.single(sql)
    primary_id = row['last_id'] + 1

    # app_code = '贰陆捌捌'
    # expire_time = '2026-04-02 23:59:59'

    app_code = '众包'
    expire_time = '2026-03-14 23:59:59'

    app_code = '美时美刻'
    expire_time = '2026-04-03 23:59:59'

    ability_ids = '1001,1003'

    f = open('ext_user_list.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line:
            arr = line.split()
            phone = arr[0].replace(' ', '')
            name = arr[1].replace(' ', '') if len(arr) > 1 else phone
            sql = gen_sql(primary_id, app_code, phone, name, ability_ids, expire_time)
            primary_id += 1
            print(sql)
            mysql.execute(sql)




main()
