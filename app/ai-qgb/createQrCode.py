# -*- coding:utf-8 -*-
import io

# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/
from PIL import Image

import requests

from util.redis_db import RedisDB
from rate_parse_rules import rate_parse_rules
from import_country import import_country
from all_country_list import all_country_list
import json

from util.tools import get_json_file

config = {
    'host': 'r-uf6sok3p4wuz8ywvi6pd.redis.rds.aliyuncs.com',
    'port': 6379,
    'password': 'codeflag2021&',

    # 39:测试环境    40:生产环境
    'database': 40
}
redis = RedisDB(config)


def create_qrcode(channel_id, path, remark, page):
    access_token = redis.get('wechat_access_token_aiqgb')
    # print(access_token)
    url = f'https://api.weixin.qq.com/wxa/getwxacode?access_token={access_token}'
    # print(url)
    payload = {
        "path": path,
        "is_hyaline": True,
    }
    response = requests.post(url, json=payload, proxies={"no_proxy": "*"})
    ret = response.content
    if len(ret) < 500:
        print(ret.decode())
    else:
        save_file = f'{channel_id}-{remark}{page}.png'

        # 使用BytesIO将字节数据转换成文件对象
        byte_io = io.BytesIO(ret)

        # 打开图像文件
        image = Image.open(byte_io)

        # 保存图像为PNG格式
        image.save(save_file, format='PNG')
        print(save_file)


def create_sql(channel_id, name, remark):
    sql = (f"INSERT INTO `aq_channel` (`id`, `name`, `remark`) "
           f"VALUES ({channel_id}, '{name}', '{remark}');")
    print(sql)


def main():
    channels = [
        # {
        #     'channel_id': 1001,
        #     'path': 'pages/classification/home/home',
        #     'name': '推文',
        #     'remark': '最航运公众号推文-20250207'
        # },
        {
            'channel_id': 1002,
            'page': 'home',
            'path': 'pages/classification/home/home',
            'name': '个人推广',
            'remark': '庄叔专属'
        },
        {
            'channel_id': 1002,
            'page': 'calculator',
            'path': 'pages/classification/calculator/calculator',
            'name': '个人推广',
            'remark': '庄叔专属'
        },
        # {
        #     'channel_id': 1003,
        #     'path': 'pages/classification/home/home',
        #     'name': '公众号菜单',
        #     'remark': '关师兄公众号菜单(首页)'
        # },
        # {
        #     'channel_id': 1004,
        #     'path': 'pages/classification/home/home',
        #     'name': '公众号菜单',
        #     'remark': '关师兄公众号菜单(计算器)'
        # },
        # {
        #     'channel_id': 1005,
        #     'path': 'pages/classification/home/home',
        #     'name': '公众号菜单',
        #     'remark': '关师兄公众号菜单(联系我们)'
        # },
        # {
        #     'channel_id': 1006,
        #     'path': 'pages/classification/home/home',
        #     'name': '业务系统广告位',
        #     'remark': '货代广告位 - 横版智能归类'
        # },
        # {
        #     'channel_id': 1007,
        #     'path': 'pages/classification/home/home',
        #     'name': '业务系统广告位',
        #     'remark': '货代广告位 - 竖版税金计算器'
        # },
        # {
        #     'channel_id': 1008,
        #     'path': 'pages/classification/home/home',
        #     'name': '业务系统广告位',
        #     'remark': '货主广告位 - 横版智能归类'
        # },
        # {
        #     'channel_id': 1009,
        #     'path': 'pages/classification/home/home',
        #     'name': '业务系统广告位',
        #     'remark': '货主广告位 - 横版税金计算器'
        # },
        # {
        #     'channel_id': 1010,
        #     'path': 'pages/classification/home/home',
        #     'name': '个人推广',
        #     'remark': '货代广告位 - 横版税金计算器+大庄朋友圈分享'
        # },
        # {
        #     'channel_id': 1011,
        #     'path': 'pages/classification/home/home',
        #     'name': '个人推广',
        #     'remark': '美国关税计算器 -- 大庄朋友圈分享'
        # },
        # {
        #     'channel_id': 1012,
        #     'path': 'pages/classification/home/home',
        #     'name': '系统内广告',
        #     'remark': '小程序弹窗海报'
        # },
        # {
        #     'channel_id': 1013,
        #     'path': 'pages/classification/home/home',
        #     'name': '系统内广告',
        #     'remark': '小程序首页Banner'
        # },
        # {
        #     'channel_id': 1014,
        #     'path': 'pages/classification/home/home',
        #     'name': '推文',
        #     'remark': '最航运公众号推文(首页)-20250309'
        # },
        # {
        #     'channel_id': 1015,
        #     'path': 'pages/classification/calculator/calculator',
        #     'name': '推文',
        #     'remark': '最航运公众号推文(计算器)-20250309'
        # },
        # {
        #     'channel_id': 1016,
        #     'path': 'pages/classification/home/home',
        #     'name': '推文',
        #     'remark': '壹流龙媒(首页)-20250309'
        # },
        # {
        #     'channel_id': 1017,
        #     'path': 'pages/classification/calculator/calculator',
        #     'name': '推文',
        #     'remark': '壹流龙媒(计算器)-20250309'
        # },

        # {
        #     'channel_id': 1018,
        #     'path': 'pages/classification/home/home',
        #     'name': '名片',
        #     'remark': ''
        # },

        # {
        #     'channel_id': 1019,
        #     'path': 'pages/product/product-buy?packageCode=customs_clearance_query&tid=1013',
        #     'name': '名片',
        #     'remark': ''
        # },
    ]

    for channel in channels:
        channel_id = channel['channel_id']
        path = channel['path']
        name = channel['name']
        remark = channel['remark']
        page = channel['page'] or ''

        path = path + f'?tid={channel_id}'
        create_qrcode(channel_id, path, remark, page)
        create_sql(channel_id, name, remark)


main()
