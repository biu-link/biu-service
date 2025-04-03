import json

from util.mysql_db import MysqlDB


def load_product_setting(db):
    mysql = MysqlDB(db)

    rows = [
        row1(db),
        row2(db),
    ]

    for row in rows:
        mysql.insert_or_update_model('aq_product', row)


# 产品1设置
def row1(db):
    product_setting = {
        'small_image': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/2001-small-image.png',
        'share_image': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/group-buy-share.png',
        'sub_title': 'AI商品智能归类 / 美国进口税金计算器',
        'sale_count': 1578,
        'share_title': 'AI清关宝会员团购',
        'unit': '月',
    }

    desc = 'AI清关宝会员·月卡'
    if db == 'mysql_dev':
        desc = '测试-' + desc

    return {
        'id': 2001,
        '`desc`': desc,
        'setting': json.dumps(product_setting, ensure_ascii=False),
    }


# 产品2设置
def row2(db):
    product_setting = {
        'small_image': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/3001-small-image.png',
        'share_image': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/customs_clearance_query/share.png',
        'sub_title': '海关状态码详细说明 / 支持子舱单状态查询',
        'sale_count': 1578,
        'share_title': '美国清关状态查询团购',
        'group_owner_free': 1,
        'unit': '条',
    }

    desc = '美国清关状态查询(单条)'
    if db == 'mysql_dev':
        desc = '测试-' + desc

    return {
        'id': 3001,
        '`desc`': desc,
        'setting': json.dumps(product_setting, ensure_ascii=False),
    }
