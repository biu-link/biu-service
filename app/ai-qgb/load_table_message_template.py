import json

from util.mysql_db import MysqlDB


def load_table_message_template(db):
    mysql = MysqlDB(db)

    rows = [
        row1(db),
        row2(db),
        row3(db),
        row4(db),
        row5(db),
        row6(db),
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


# 查询结果通知
def row4(db):
    miniprogram_state = 'formal' if db == 'mysql_prod' else 'trial'
    message_template = {
        'template_id': 'kMmemranbJIvbAtPfVSeJqP0wCO6dG0LrjlQ1Xeo7Q8',
        'touser': '{{open_id}}',
        'page': '{{page}}',
        'miniprogram_state': miniprogram_state,
        'lang': 'zh_CN',
        'data': {
            'thing14': {
                'value': '{{title}}'
            },
            'thing2': {
                'value': '{{result}}'
            },
            'thing7': {
                'value': '{{remark}}'
            },
        }
    }

    return {
        'id': 104,
        'alias_name': 'query_result_notify',
        'message_type': 'wx_mini_template_message',
        'message_template': json.dumps(message_template, ensure_ascii=False),
        'memo': '通用查询结果通知'
    }


# 清关状态查询通知2
def row5(db):
    miniprogram_state = 'formal' if db == 'mysql_prod' else 'trial'
    message_template = {
        'template_id': 'kGJJvsSQBogxmJ71sGBbqNC1VclhbTcxjAXQfWmrp80',
        'touser': '{{open_id}}',
        'page': '{{page}}',
        'miniprogram_state': miniprogram_state,
        'lang': 'zh_CN',
        'data': {
            'character_string1': {
                'value': '{{mbl_no}}'
            },
            'thing6': {
                'value': '{{mbl_type}}'
            },
            'phrase3': {
                'value': '{{status}}'
            },
        }
    }

    return {
        'id': 105,
        'alias_name': 'customs_clearance_status_notify',
        'message_type': 'wx_mini_template_message',
        'message_template': json.dumps(message_template, ensure_ascii=False),
        'memo': '清关提单状态变更通知'
    }


# 订单进度通知
def row6(db):
    miniprogram_state = 'formal' if db == 'mysql_prod' else 'trial'
    message_template = {
        'template_id': 'MmhfyLUJ1LgfLEUQBcUV-IZdCKL9MMjMj0u9tnogF7c',
        'touser': '{{open_id}}',
        'page': '{{page}}',
        'miniprogram_state': miniprogram_state,
        'lang': 'zh_CN',
        'data': {
            'short_thing15': {
                'value': '{{order_type}}'
            },
            'thing9': {
                'value': '{{order_no}}'
            },
            'phrase2': {
                'value': '{{status}}'
            },
            'thing10': {
                'value': '{{remark}}'
            },
        }
    }

    return {
        'id': 106,
        'alias_name': 'order_progress_notify',
        'message_type': 'wx_mini_template_message',
        'message_template': json.dumps(message_template, ensure_ascii=False),
        'memo': '订单进度通知'
    }
