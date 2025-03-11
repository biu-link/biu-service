# -*- coding:utf-8 -*-

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
    'database': 39
}
redis = RedisDB(config)

# 产品套餐设置
code = 'system_config_public_product_setting_hs_code_member'
value = redis.get(code)
print(value)

titleStyle = {
    "font-weight": "bold",
    "font-size": "40rpx",
    "color": "#333333",
    "line-height": "56rpx",
    "padding": "30rpx 30rpx 5rpx 30rpx",
    "display": "block"
}

textStyle = {
    "font-size": "26rpx",
    "color": "#666666",
    "padding": "4rpx 30rpx 60rpx 30rpx",
    "display": "block"
}

imageStyle = {
    "padding": "0 0rpx",
    "display": "flex",
    "justify-content": "center",
    "width": "100%",
    "box-sizing": "border-box",
}

value = {
    "title": "加入会员，享受更多权益",
    "details": [
        "每天 20 条智能分类搜索权限",
        "所查 HS CODE 详细信息查看权限",
        "客服答疑"
    ],
    "items": [
        {"product_id": 2001},
        {"product_id": 2003},
        {"product_id": 2002}
    ],
    "group_buy_product_id": 2001,
    "price_button": {
        "price": "¥{price}/月",
        "price_text": "直接购买",
        "group_price": "¥{group_price}/月",
        "group_price_text": "发起 {group_size} 人团",
    },
    "layout_items": [
        {
            "type": "image",
            "url": "https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/hs_code_member/banner%402x.png",
            "style": {
                "width": "100%",
                "height": "450rpx"
            }
        },
        {
            "type": "title",
            "text": "AI清关宝会员(月卡)",
            "style": titleStyle,
        },
        {
            "type": "text",
            "text": "AI商品智能归类 / 美国进口税金计算器",
            "style": textStyle,
        },
        {
            "type": "image",
            "url": "https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/hs_code_member/01%402x.png",
            "style": {
                **imageStyle,
                "height": "889rpx",
            }
        },
        {
            "type": "image",
            "url": "https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/hs_code_member/02%402x.png",
            "style": {
                **imageStyle,
                "height": "874rpx",
            }
        },
        {
            "type": "image",
            "url": "https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/hs_code_member/03_0306.png",
            "style": {
                **imageStyle,
                "height": "1115rpx",
            }
        }
    ],
}

redis.set(code, json.dumps(value, ensure_ascii=False))

value = redis.get(code)
print(value)

# A/B 监管类型字典
code = 'system_config_public_explanation_list'
value = open('../explanation_list.json', 'r', encoding='utf-8').read()
redis.set(code, value)
value = redis.get(code)
print(value)

# 评论选项
code = 'system_config_public_comment_type'
value = {
    "positive": [
        {
            "code": "P1",
            "value": "归类准确"
        },
        {
            "code": "P2",
            "value": "描述清晰"
        },
        {
            "code": "P0",
            "value": "自定义赞美"
        }
    ],
    "negative": [
        {
            "code": "N1",
            "value": "归类不准确"
        },
        {
            "code": "N2",
            "value": "描述不清晰"
        },
        {
            "code": "N0",
            "value": "自定义吐槽"
        }
    ]
}
redis.set(code, json.dumps(value, ensure_ascii=False))
value = redis.get(code)
print(value)

code = 'system_config_public_setting'
value = {
    'documents': {
        'privacy_html_url': 'https://custompdf.codeflagai.com/wechat/ai-qgb/mp/html/privacy_202412301738.html',
        'service_html_url': 'https://custompdf.codeflagai.com/wechat/ai-qgb/mp/html/service_202412301550.html'
    },
    'qrcode': {
        'contact_us': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/qrcode-xiaoqinglaoshi.png'
    },
    'share': {
        'image_url': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/share-default.png'
    },
    # 团购订阅消息模版id
    'group_buy_subscribe_template_ids': [
        'JapbzjBiuguW_ATwdrIl-OjbkwXjui-QMCmmbIrvdcU',
        'WGKGkp8r6M8JOzXZVvAtLadgwlJrImAp9LOgvGVxoVU',
        's6EButqdpl7BWD3xOc11WviHvR7Yx8XMwWMJkNk6MC8',
    ],
    'invite_join_group_text': '可邀请好友继续参与拼团',
    'join_now_text': '超实用!快来和我一起拼团吧!',
    'invite_join_group_promotion': '仅剩 <span style="color:#FF6600;">{remain_people}</span> 人,快呼唤小伙伴参加吧!',
    'special_tariff': {  # 对中加征税率
        'fix_rate': '20%',
        'exclude_pattern': '^980200(40|50|60|80)\\d+$',
        'special_code': '99030124',
        'describe_list': [
            {
                'specialDescribeCn': '<b>9903.01.24（加征）</b><br>除可归类为商品 9903.01.21、9903.01.22 和 9903.01.23 的商品外，所有进口的中国和香港商品，以及抵达美国的旅客随身行李中的个人自用商品除外，将额外征收 20% 的从价税率。',
                'specialDescribeEn': 'All imports of articles that are products of China and Hong Kong, other than products classifiable under headings 9903.01.21, 9903.01.22, and 9903.01.23, and other than products for personal use included in accompanied baggage of persons arriving in the United States, will be assessed an additional ad valorem rate of duty of 20%.',
                'effectiveDate': '20250304'
            },
            {
                'specialDescribeCn': '<b>9903.01.21（豁免）</b><br>来自中国和香港的物品，如果是美国管辖范围内的个人捐赠的物品，如食品、衣物和药品，旨在用于减轻人类痛苦，符合美国本章节附注2(t)的规定。',
                'specialDescribeEn': 'Articles the product of China and Hong Kong that are donations, by persons subject to the jurisdiction of the United States, of articles, such as food, clothing, and medicine, intended to be used to relieve human suffering, as provided for in U.S. note 2(t) to this subchapter',
                'effectiveDate': '20250204'
            },
            {
                'specialDescribeCn': '<b>9903.01.22（豁免）</b><br>来自中国和香港的信息材料，包括但不限于出版物、电影、海报、留声机唱片、照片、微缩胶片、微缩卡、磁带、光盘、CD-ROM、艺术作品和新闻电线传输。',
                'specialDescribeEn': 'Articles the product of China and Hong Kong that are informational materials, including but not limited to, publications, films, posters, phonograph records, photographs, microfilms, microfiche, tapes,compact disks, CD ROMs, artworks, and news wire feeds',
                'effectiveDate': '20250204'
            },
            {
                'specialDescribeCn': '<b>9903.01.23（豁免）</b><br>除第9903.01.21和9903.01.22项下描述的产品外，以及除用于个人使用并包含在进入美国的旅客随身行李中的产品外，来自中国和香港的物品符合以下条件：(1) 在2025年2月1日东部标准时间12:01 a.m.之前，已装载到装船港口的船只上，或在进入美国之前，已在最终运输方式上运输；(2) 在2025年2月4日东部标准时间12:01 a.m.或之后，并在2025年3月7日东部标准时间12:01 a.m.之前，进入美国消费或从仓库提取以供消费。',
                'specialDescribeEn': 'Except for products described in headings 9903.01.21 and 9903.01.22, and other than products for personal use included in accompanied baggage of persons arriving in the United States, articles the product of China and Hong Kong that: (1) were loaded onto a vessel at the port of loading, or in transit on the final mode of transport prior to entry into the United States, before 12:01 a.m. eastern standard time on February 1, 2025; and (2) are entered for consumption, or withdrawn from warehouse for consumption, on or after 12:01 a.m. eastern standard time on February 4, 2025, and before 12:01 a.m. eastern standard time on March 7, 2025.',
                'effectiveDate': '20250204'
            },
            {
                'specialDescribeCn': '<b>chapter 98</b><br>税号9903.01.20 所规定的额外关税不适用于依据美国海关与边境保护局（CBP）相关法规，在《协调关税表》第98章 特定条款下正确申报的商品，并且CBP 同意此类商品适用该条款的情况。<br>但以下商品除外：<br>（1）税号9802.00.80<br>（2）子目9802.00.40、9802.00.50 和 9802.00.60<br>注：（1）对于子目9802.00.40、9802.00.50 和 9802.00.60，额外关税将适用于在中国（PRC）进行的维修、改造或加工的增值部分，具体适用范围依照相关子目的描述。<br>（2）对于税号9802.00.80，额外关税适用于在中国（PRC）境外组装的商品的价值，但不包括其中源自美国的材料或部件的成本或价值，具体适用范围依照相关描述。',
                'specialDescribeEn': 'The additional duties imposed by heading 9903.01.20 shall not apply to goods for which entry is properly claimed under a provision of chapter 98 of the tariff schedule pursuant to applicable regulations of U.S. Customs and Border Protection (“CBP”), and whenever CBP agrees that entry under such a provision is appropriate, except for goods entered under heading 9802.00.80; and subheadings 9802.00.40, 9802.00.50, and 9802.00.60. For subheadings 9802.00.40, 9802.00.50, and 9802.00.60, the additional duties apply to the value of repairs, alterations, or processing performed (in the PRC), as described in the applicable subheading. For heading 9802.00.80, the additional duties apply to the value of the article assembled abroad (in the PRC), less the cost or value of such products of the United States, as described.',
                'effectiveDate': '20250204'
            },
        ],

    },
    'special_tariff_list': [
        {  # 墨西哥 加征 25%
            'fix_rate': '25%',
            'include_country_list': ['MX'],
            'rules': [
                {
                    'code_matchers': [
                        {
                            'patterns': ['^980200(40|50|60|80)\\d+$'],
                            'type': 'include',
                        },
                        {
                            'patterns': ['^98\\d+$'],
                            'type': 'exclude',
                        },
                        {
                            'patterns': ['^\\d+$'],
                            'type': 'include',
                        },
                    ],
                    'special_code': '99030101',
                }
            ],

            'special_describes': {
                '99030101': [
                    {
                        'specialDescribeCn': '<b>9903.01.01（加征）</b><br>除可归类为标题 9903.01.02 和 9903.01.03 的商品以及抵达美国的旅客随身行李中的个人使用商品外，所有进口的墨西哥商品均需额外缴纳 25% 的从价税。',
                        'specialDescribeEn': 'All imports of articles that are products of Mexico, other than products classifiable under headings 9903.01.02 and 9903.01.03 and other than products for personal use included in accompanied baggage of persons arriving in the United States will be assessed an additional ad valorem rate of duty of 25%.',
                        'effectiveDate': '20250304'
                    },
                    {
                        'specialDescribeCn': '<b>9903.01.02（豁免）</b><br>由受美国管辖的人捐赠用于减轻人类痛苦的物品，如食品、衣服和药品，属于墨西哥产品的物品。',
                        'specialDescribeEn': 'Articles the product of Mexico that are donations, by persons subject to the jurisdiction of the United States, of articles, such as food, clothing, and medicine, intended to be used to relieve human suffering.',
                        'effectiveDate': '20250304'
                    },
                    {
                        'specialDescribeCn': '<b>9903.01.03（豁免）</b><br>属于墨西哥商品且属于信息材料的物品，包括但不限于出版物、电影、海报、留声机唱片、照片、缩微胶卷、缩微胶片、磁带、光盘、CD ROM、插图和新闻馈送。',
                        'specialDescribeEn': 'Articles the product of Mexico that are informational materials, including but not limited to, publications, films, posters, phonograph records, photographs, microfilms, microfiche, tapes, compact disks, CD ROMs, artworks, and news wire feeds.',
                        'effectiveDate': '20250304'
                    },
                ]
            },

            'exclude_pattern': '^98\\d+$',
            'include_pattern': '^980200(40|50|60|80)\\d+$',
            'special_code': '99030101',
            'describe_list': [
                {
                    'specialDescribeCn': '<b>9903.01.01（加征）</b><br>除可归类为标题 9903.01.02 和 9903.01.03 的商品以及抵达美国的旅客随身行李中的个人使用商品外，所有进口的墨西哥商品均需额外缴纳 25% 的从价税。',
                    'specialDescribeEn': 'All imports of articles that are products of Mexico, other than products classifiable under headings 9903.01.02 and 9903.01.03 and other than products for personal use included in accompanied baggage of persons arriving in the United States will be assessed an additional ad valorem rate of duty of 25%.',
                    'effectiveDate': '20250304'
                },
                {
                    'specialDescribeCn': '<b>9903.01.02（豁免）</b><br>由受美国管辖的人捐赠用于减轻人类痛苦的物品，如食品、衣服和药品，属于墨西哥产品的物品。',
                    'specialDescribeEn': 'Articles the product of Mexico that are donations, by persons subject to the jurisdiction of the United States, of articles, such as food, clothing, and medicine, intended to be used to relieve human suffering.',
                    'effectiveDate': '20250304'
                },
                {
                    'specialDescribeCn': '<b>9903.01.03（豁免）</b><br>属于墨西哥商品且属于信息材料的物品，包括但不限于出版物、电影、海报、留声机唱片、照片、缩微胶卷、缩微胶片、磁带、光盘、CD ROM、插图和新闻馈送。',
                    'specialDescribeEn': 'Articles the product of Mexico that are informational materials, including but not limited to, publications, films, posters, phonograph records, photographs, microfilms, microfiche, tapes, compact disks, CD ROMs, artworks, and news wire feeds.',
                    'effectiveDate': '20250304'
                },
            ],
        },
        {  # 加拿大 加征 25%
            'fix_rate': '25%',
            'include_country_list': ['CA'],
            'rules': [
                {
                    'code_matchers': [
                        {
                            'patterns': ['^980200(40|50|60|80)\\d+$'],
                            'type': 'include',
                        },
                        {
                            'patterns': ['^98\\d+$'],
                            'type': 'exclude',
                        },
                        {
                            'patterns': ['^\\d+$'],
                            'type': 'include',
                        },
                    ],
                    'special_code': '99030110',
                }
            ],

            'special_describes': {
                '99030110': [
                    {
                        'specialDescribeCn': '<b>9903.01.10（加征）</b><br>除可归类为标题 9903.01.11、9903.01.12 和 9903.01.13 的商品外，所有进口的加拿大商品，以及抵达美国的旅客随身行李中的个人使用商品除外，将额外征收 25% 的从价税率。',
                        'specialDescribeEn': 'All imports of articles that are products of Canada, other than products classifiable under headings 9903.01.11, 9903.01.12, and 9903.01.13, and other than products for personal use included in accompanied baggage of persons arriving in the United States, will be assessed an additional ad valorem rate of duty of 25%.',
                        'effectiveDate': '20250304'
                    },
                    {
                        'specialDescribeCn': '<b>9903.01.11（豁免）</b><br>由受美国管辖的人捐赠的加拿大产品物品，用于减轻人类痛苦的物品，例如食品、衣服和药品。',
                        'specialDescribeEn': 'Articles the product of Canada that are donations, by persons subject to the jurisdiction of the United States, of articles, such as food, clothing, and medicine, intended to be used to relieve human suffering.',
                        'effectiveDate': '20250304'
                    },
                    {
                        'specialDescribeCn': '<b>9903.01.12（豁免）</b><br>属于加拿大商品且属于信息材料的物品，包括但不限于出版物、电影、海报、留声机唱片、照片、缩微胶卷、缩微胶片、磁带、光盘、CD ROM、艺术品和新闻馈送。',
                        'specialDescribeEn': 'Articles the product of Canada that are informational materials, including but not limited to, publications, films, posters, phonograph records, photographs, microfilms, microfiche, tapes, compact disks, CD ROMs, artworks, and news wire feeds.',
                        'effectiveDate': '20250304'
                    },
                ]
            },
            'exclude_pattern': '^98\\d+$',
            'include_pattern': '^980200(40|50|60|80)\\d+$',
            'special_code': '99030110',
            'describe_list': [
                {
                    'specialDescribeCn': '<b>9903.01.10（加征）</b><br>除可归类为标题 9903.01.11、9903.01.12 和 9903.01.13 的商品外，所有进口的加拿大商品，以及抵达美国的旅客随身行李中的个人使用商品除外，将额外征收 25% 的从价税率。',
                    'specialDescribeEn': 'All imports of articles that are products of Canada, other than products classifiable under headings 9903.01.11, 9903.01.12, and 9903.01.13, and other than products for personal use included in accompanied baggage of persons arriving in the United States, will be assessed an additional ad valorem rate of duty of 25%.',
                    'effectiveDate': '20250304'
                },
                {
                    'specialDescribeCn': '<b>9903.01.11（豁免）</b><br>由受美国管辖的人捐赠的加拿大产品物品，用于减轻人类痛苦的物品，例如食品、衣服和药品。',
                    'specialDescribeEn': 'Articles the product of Canada that are donations, by persons subject to the jurisdiction of the United States, of articles, such as food, clothing, and medicine, intended to be used to relieve human suffering.',
                    'effectiveDate': '20250304'
                },
                {
                    'specialDescribeCn': '<b>9903.01.12（豁免）</b><br>属于加拿大商品且属于信息材料的物品，包括但不限于出版物、电影、海报、留声机唱片、照片、缩微胶卷、缩微胶片、磁带、光盘、CD ROM、艺术品和新闻馈送。',
                    'specialDescribeEn': 'Articles the product of Canada that are informational materials, including but not limited to, publications, films, posters, phonograph records, photographs, microfilms, microfiche, tapes, compact disks, CD ROMs, artworks, and news wire feeds.',
                    'effectiveDate': '20250304'
                },
            ],
        }
    ],
    'calculator': {
        'mpf': {  # 商品加工费
            'rate': 0.003464,  # 费率
            'min': 32.71,  # 最低收费
            'max': 634.62  # 最高收费
        },
        'hmp': {  # 港口维护费
            'rate': 0.00125  # 费率
        },
        'tip': '* 本计算器根据 Formal Entry(T01) 清关模式进行计算。Inform Entry(T11) 税金计算器即将上线，敬请期待!',
    },
    # 弹窗海报
    'ad_popup_list': [
        {
            'enabled': 1,
            'poster_url': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/ad/ad-popup-20250306.png',
            'link': '/pages/product/product-buy?packageCode=hs_code_member&tid=1012',
            'quiet_second': 14400,
            'pages': [
                'pages/classification/home/home',
                'pages/classification/calculator/calculator',
                'pages/classification/calculator/calculator-page',
                'pages/classification/search-by-name/search-by-name',
                'pages/my/my/my',
            ]
        }
    ],
    'home_banner_list': [
        {
            'enabled': 1,
            'poster_url': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/ad/home-banner-01.png',
            'link': '/pages/product/product-buy?packageCode=hs_code_member&tid=1013',
        }
    ]
}

redis.set(code, json.dumps(value, ensure_ascii=False))
value = redis.get(code)
print(value)

code = 'system_config_public_import_country'
country_list = import_country
redis.set(code, json.dumps(country_list, ensure_ascii=False))
value = redis.get(code)
print(value)

code = 'system_config_general_rate_parse_rules'
value = rate_parse_rules
redis.set(code, json.dumps(value, ensure_ascii=False))
value = redis.get(code)
print(value)

# hs code 中英翻译
# code = 'system_config_hs_code_description_chs'
# description_list = get_json_file('WWWHTS_20250120.json')
# redis.set(code, json.dumps(description_list, ensure_ascii=False))


# 所有国家列表
# code = 'system_config_public_export_country'
# country_list = get_json_file('export_country.json')
# redis.set(code, json.dumps(country_list, ensure_ascii=False))
# value = redis.get(code)
# print(value)

# 出口国家的树形结构，用于显示出口国的二级联动选择输入
# code = 'system_config_public_export_country_tree'
# export_country = get_json_file('export_country.json')
#
# for item in all_country_list:
#     for i in range(len(item['country_list']) - 1, -1, -1):
#         country = item['country_list'][i]
#         name = country['name']
#
#         match_country = list(filter(lambda x: x['name'] == name, export_country['items']))
#         if len(match_country) == 0:
#             del item['country_list'][i]
#         else:
#             country['code'] = match_country[0]['code']
#
# redis.set(code, json.dumps(all_country_list, ensure_ascii=False))
# value = redis.get(code)
# print(json.dumps(value, ensure_ascii=False))
