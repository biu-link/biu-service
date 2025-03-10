import json

from util.mysql_db import MysqlDB


def load_table_message_template(db):
    mysql = MysqlDB(db)

    rows = [
        row1(db),
        row2(db),
        row3(db)
    ]

    for row in rows:
        mysql.insert_or_update_model('aq_message_template', row)


# 团购进度
def row1(db):
    miniprogram_state = 'formal' if db == 'mysql_prod' else 'trial'
    message_template = {
        'template_id': 'JapbzjBiuguW_ATwdrIl-OjbkwXjui-QMCmmbIrvdcU',
        'touser': '{{open_id}}',
        'page': '{{page}}',
        'miniprogram_state': miniprogram_state,
        'lang': 'zh_CN',
        'data': {
            'thing1': {
                'value': '{{title}}'
            },
            'thing8': {
                'value': '已有{{join_number}}人参与'
            },
            'thing4': {
                'value': '还差{{need_people}}人成团'
            },
            'thing10': {
                'value': '{{group_order_status}}'
            },
            'thing2': {
                'value': '团购结束还有{{remain_time}}！'
            }
        }
    }

    return {
        'id': 101,
        'alias_name': 'group_buy_progress',
        'message_type': 'wx_mini_template_message',
        'message_template': json.dumps(message_template, ensure_ascii=False),
        'memo': '团购进度通知'
    }


# 拼团成功通知
def row2(db):
    miniprogram_state = 'formal' if db == 'mysql_prod' else 'trial'
    message_template = {
        'template_id': 'WGKGkp8r6M8JOzXZVvAtLadgwlJrImAp9LOgvGVxoVU',
        'touser': '{{open_id}}',
        'page': '{{page}}',
        'miniprogram_state': miniprogram_state,
        'lang': 'zh_CN',
        'data': {
            'thing5': {
                'value': '{{title}}'
            },
            'character_string1': {
                'value': '{{order_no}}'
            },
            'thing7': {
                'value': '{{group_size}}'
            },
            'time8': {
                'value': '{{group_complete_time}}'
            }
        }
    }

    return {
        'id': 102,
        'alias_name': 'group_buy_complete',
        'message_type': 'wx_mini_template_message',
        'message_template': json.dumps(message_template, ensure_ascii=False),
        'memo': '拼团成功通知'
    }


# 拼团结果通知
def row3(db):
    miniprogram_state = 'formal' if db == 'mysql_prod' else 'trial'
    message_template = {
        'template_id': 's6EButqdpl7BWD3xOc11WviHvR7Yx8XMwWMJkNk6MC8',
        'touser': '{{open_id}}',
        'page': '{{page}}',
        'miniprogram_state': miniprogram_state,
        'lang': 'zh_CN',
        'data': {
            'thing1': {
                'value': '{{title}}'
            },
            'number3': {
                'value': '{{need_people}}'
            },
            'thing2': {
                'value': '快邀请你的伙伴参团吧!'
            },
        }
    }

    return {
        'id': 103,
        'alias_name': 'group_buy_result',
        'message_type': 'wx_mini_template_message',
        'message_template': json.dumps(message_template, ensure_ascii=False),
        'memo': '拼团结果通知'
    }
