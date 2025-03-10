import json

from util.mysql_db import MysqlDB


def load_product_setting(db):
    mysql = MysqlDB(db)

    rows = [
        row1(db),
    ]

    for row in rows:
        mysql.insert_or_update_model('aq_product', row)


# 产品1设置
def row1(db):
    product_setting = {
        'small_image': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/2001-small-image.png',
        'sub_title': 'AI商品智能归类 / 美国进口税金计算器',
        'sale_count': 1578,
        'share_title': 'AI清关宝会员团购',
    }

    desc = 'AI清关宝会员·月卡'
    if db == 'mysql_dev':
        desc = '测试-' + desc

    return {
        'id': 2001,
        '`desc`': desc,
        'setting': json.dumps(product_setting, ensure_ascii=False),
    }
