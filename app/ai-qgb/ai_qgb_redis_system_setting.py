# -*- coding:utf-8 -*-

from util.redis_db import RedisDB
from rate_parse_rules import rate_parse_rules
from import_country import import_country
from all_country_list import all_country_list
from ams_status import ams_status

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
        "unit": "月",
        "price": "{price}",
        "price_text": "直接购买",
        "group_price": "{group_price}",
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

# 清关状态产品购买页设置
code = 'system_config_public_product_setting_customs_clearance_query'
value = redis.get(code)
print(value)

value = {
    "title": "购买清关状态查询条数",
    "details": [
        "1. 查看详细的清关进度，查询状态信息",
        "2. 专业客服答疑"
    ],
    "items": [
        {"product_id": 3001, "title": "单条查询", "desc": "(单条查询)"},
        {"product_id": 3002, "title": "8.5折优惠", "desc": "(总共获得50条)", "title_class": "emphasis"},
        {"product_id": 3003, "title": "6折优惠", "desc": "(总共获得500条)", "title_class": "emphasis"}
    ],
    "buy_button": {
        "text": "立即购买",
        "save_text": "(已省¥{save_money})"
    },
    "group_buy_product_id": 3001,
    "price_button": {
        "unit": "条",
        "price": "{price}",
        "price_text": "直接购买",
        "group_price": "{group_price}",
        "group_price_text": "发起 {group_size} 人团",
        "group_buy_tag": "开团免费",
    },
    "layout_items": [
        {
            "type": "image",
            "url": "https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/customs_clearance_query/banner%402x.png",
            "style": {
                "width": "100%",
                "height": "450rpx"
            }
        },
        {
            "type": "title",
            "text": "美国清关状态查询",
            "style": titleStyle,
        },
        {
            "type": "text",
            "text": "海关状态码详细说明 / 支持子舱单状态查询",
            "style": textStyle,
        },
        {
            "type": "image",
            "url": "https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/customs_clearance_query/01%402x.png",
            "style": {
                **imageStyle,
                "height": "1534rpx",
            }
        },
        {
            "type": "image",
            "url": "https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/customs_clearance_query/02%402x.png",
            "style": {
                **imageStyle,
                "height": "874rpx",
            }
        },
        {
            "type": "image",
            "url": "https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/product/customs_clearance_query/03%402x.png",
            "style": {
                **imageStyle,
                "height": "1010rpx",
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
    # 清关查询状态通知订阅消息模版id
    'customs_clearance_query_subscribe_template_ids': [
        'kMmemranbJIvbAtPfVSeJqP0wCO6dG0LrjlQ1Xeo7Q8',
        'kGJJvsSQBogxmJ71sGBbqNC1VclhbTcxjAXQfWmrp80',
        'MmhfyLUJ1LgfLEUQBcUV-IZdCKL9MMjMj0u9tnogF7c',
    ],
    'invite_join_group_text': '可邀请好友继续参与拼团',
    'join_now_text': '超实用!快来和我一起拼团吧!',
    'invite_join_group_promotion': '仅剩 <span style="color:#FF6600;">{remain_people}</span> 人,快呼唤小伙伴参加吧!',

    'customs_clearance_query': {
        'example_mbl': 'HLCUSZX241DEMO',
        'no_quota_tip': '您还未购买查询条数',
        'quota_used_up_tip': '您的搜索条数已用完',
    },
    'special_tariff': {
        'fix_rate': '',  # 对中加征税率  已灌入后端数据，前端无需再使用该规则
        'exclude_search_by_name': 1,
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
        {
            'fix_rate': '25%',  # 墨西哥 加征 25%
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
                    'special_code': ['99030101/99030105', '99030102', '99030103'],
                }
            ],

            'special_describes': {
                '99030101/99030105': [
                    {
                        'specialDescribeCn': '<b>9903.01.01（加征）</b><br>除可归类为标题 9903.01.02 和 9903.01.03 的商品以及抵达美国的旅客随身行李中的个人使用商品外，所有进口的墨西哥商品均需额外缴纳 25% 的从价税。',
                        'specialDescribeEn': 'All imports of articles that are products of Mexico, other than products classifiable under headings 9903.01.02 and 9903.01.03 and other than products for personal use included in accompanied baggage of persons arriving in the United States will be assessed an additional ad valorem rate of duty of 25%.',
                        'effectiveDate': '20250304',
                        'specialInfo': '25%/10%'
                    },
                    {
                        'specialDescribeCn': '<b>9903.01.05（加征）</b><br>如美国本子章注释2(c)所规定，作为墨西哥产品的钾盐',
                        'specialDescribeEn': 'Potash that is a product of Mexico, as provided for in U.S. note 2(c) to this subchapter.',
                        'effectiveDate': '20250306',
                    },
                ],
                '99030102': [
                    {
                        'specialDescribeCn': '<b>9903.01.02（豁免）</b><br>由受美国管辖的人捐赠用于减轻人类痛苦的物品，如食品、衣服和药品，属于墨西哥产品的物品。',
                        'specialDescribeEn': 'Articles the product of Mexico that are donations, by persons subject to the jurisdiction of the United States, of articles, such as food, clothing, and medicine, intended to be used to relieve human suffering.',
                        'effectiveDate': '20250304',
                        'exempting': '有',
                        'specialInfo': '有'
                    },
                ],
                '99030103': [
                    {
                        'specialDescribeCn': '<b>9903.01.03（豁免）</b><br>属于墨西哥商品且属于信息材料的物品，包括但不限于出版物、电影、海报、留声机唱片、照片、缩微胶卷、缩微胶片、磁带、光盘、CD ROM、插图和新闻馈送。',
                        'specialDescribeEn': 'Articles the product of Mexico that are informational materials, including but not limited to, publications, films, posters, phonograph records, photographs, microfilms, microfiche, tapes, compact disks, CD ROMs, artworks, and news wire feeds.',
                        'effectiveDate': '20250304',
                        'exempting': '有',
                        'specialInfo': '有'
                    }
                ],
            },

        },
        {
            'fix_rate': '25%',  # 加拿大 加征 25%
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
                    'special_code': ['99030110/99030115', '99030111', '99030112'],
                }
            ],

            'special_describes': {
                '99030110/99030115': [
                    {
                        'specialDescribeCn': '<b>9903.01.10（加征）</b><br>除可归类为标题 9903.01.11、9903.01.12 和 9903.01.13 的商品外，所有进口的加拿大商品，以及抵达美国的旅客随身行李中的个人使用商品除外，将额外征收 25% 的从价税率。',
                        'specialDescribeEn': 'All imports of articles that are products of Canada, other than products classifiable under headings 9903.01.11, 9903.01.12, and 9903.01.13, and other than products for personal use included in accompanied baggage of persons arriving in the United States, will be assessed an additional ad valorem rate of duty of 25%.',
                        'effectiveDate': '20250304',
                        'specialInfo': '25%/10%',
                    },
                    {
                        'specialDescribeCn': '<b>9903.01.15（加征）</b><br>如美国本子章注释2(I)所规定，作为加拿大产品的钾盐',
                        'specialDescribeEn': 'Potash that is a product of Canada, as provided for in U.S. note 2(I) to this subchapter',
                        'effectiveDate': '20250306',
                        'specialInfo': '10%',
                    },
                ],
                '99030111': [
                    {
                        'specialDescribeCn': '<b>9903.01.11（豁免）</b><br>由受美国管辖的人捐赠的加拿大产品物品，用于减轻人类痛苦的物品，例如食品、衣服和药品。',
                        'specialDescribeEn': 'Articles the product of Canada that are donations, by persons subject to the jurisdiction of the United States, of articles, such as food, clothing, and medicine, intended to be used to relieve human suffering.',
                        'effectiveDate': '20250304',
                        'exempting': '有',
                        'specialInfo': '有'
                    },
                ],
                '99030112': [
                    {
                        'specialDescribeCn': '<b>9903.01.12（豁免）</b><br>属于加拿大商品且属于信息材料的物品，包括但不限于出版物、电影、海报、留声机唱片、照片、缩微胶卷、缩微胶片、磁带、光盘、CD ROM、艺术品和新闻馈送。',
                        'specialDescribeEn': 'Articles the product of Canada that are informational materials, including but not limited to, publications, films, posters, phonograph records, photographs, microfilms, microfiche, tapes, compact disks, CD ROMs, artworks, and news wire feeds.',
                        'effectiveDate': '20250304',
                        'exempting': '有',
                        'specialInfo': '有'
                    },
                ]
            },

        },

        {
            'fix_rate': '-',  # 墨西哥 美墨加协定进口关税FREE 用一个短横线表示不需要增加税率，但需要参与后续逻辑处理，此处是后面需要添加豁免规则
            'include_country_list': ['MX'],
            'rules': [
                {
                    'code_matchers': [
                        {
                            'custom': 'usmca',  # hscode 前 8 位存在于 usmca 中
                            'type': 'include',
                            'must_special_codes': ['99030101/99030105'],
                        }
                    ],
                    'special_code': ['99030104'],  # 豁免
                }
            ],

            'special_rate_of_duty': 'United States-Mexico-Canada-Agreement (USMCA)',
            'special_rate_of_duty_explanation': 'United States-Mexico-Canada-Agreement (USMCA)<br>美墨加协定进口关税FREE',

            'special_describes': {
                '99030104': [
                    {
                        'specialDescribeCn': '根据《协调关税表》(HTSUS) 总注11的条款，以及《协调关税表》第98章第XXIII分章和第99章第XXII分章中与《美墨加协定》(USMCA) 相关的任何规定，免税进口的商品。',
                        'specialDescribeEn': 'Articles that are entered free of duty under the terms of general note 11 to the HTSUS, including any treatment set forth in subchapter XXIII of chapter 98 and subchapter XXII of chapter 99 of the HTS, as related to the USMCA.',
                        'effectiveDate': '20250306',
                        'exempting': '有',
                        'specialInfo': '有'
                    },
                ]
            },
        },

        {
            'fix_rate': '-',  # 加拿大 美墨加协定进口关税FREE 用一个短横线表示不需要增加税率，但需要参与后续逻辑处理，此处是后面需要添加豁免规则
            'include_country_list': ['CA'],
            'rules': [
                {
                    'code_matchers': [
                        {
                            'custom': 'usmca',  # hscode 前 8 位存在于 usmca 中
                            'type': 'include',
                            'must_special_codes': ['99030110/99030115'],
                        }
                    ],
                    'special_code': ['99030114'],  # 豁免
                }
            ],

            'special_rate_of_duty': 'United States-Mexico-Canada-Agreement (USMCA)',
            'special_rate_of_duty_explanation': 'United States-Mexico-Canada-Agreement (USMCA)<br>美墨加协定进口关税FREE',

            'special_describes': {
                '99030114': [
                    {
                        'specialDescribeCn': '根据《协调关税表》(HTSUS) 总注11的条款，以及《协调关税表》第98章第XXIII分章和第99章第XXII分章中与《美墨加协定》(USMCA) 相关的任何规定，免税进口的商品。',
                        'specialDescribeEn': 'Articles that are entered free of duty under the terms of general note 11 to the HTSUS, including any treatment set forth in subchapter XXIII of chapter 98 and subchapter XXII of chapter 99 of the HTS, as related to the USMCA.',
                        'effectiveDate': '20250306',
                        'exempting': '有',
                        'specialInfo': '有'
                    },
                ]
            },

        },

        {
            'fix_rate': '200%',  # 俄罗斯 加征 200%
            'include_country_list': ['RU'],
            'terminate_on_match': True,
            'rules': [
                {
                    'code_matchers': [
                        {
                            'patterns': ['^((760[1456789])|(76169951))\\d+$'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038567', '99038569'],
                },

                {
                    'code_matchers': [
                        {
                            'patterns': ['^(76101000|76109000|76141050|76149020|76149040|76149050|87081030|87081060|87082921|94031000|94032000|76129010)\\d+$'],
                            'codes': ['7615102015', '7615102025', '7615103015', '7615103025', '7615105020', '7615105040', '7615107125', '7615107130',
                                      '7615107155', '7615107180', '7615109100', '7615200000', '7616109090', '7616991000', '7616995130', '7616995140',
                                      '7616995190', '6603908100', '8302103000', '8302106030', '8302106060', '8302106090', '8302200000', '8302303010',
                                      '8302303060', '8302413000', '8302416015', '8302416045', '8302416050', '8302416080', '8302423010', '8302423015',
                                      '8302423065', '8302496035', '8302496045', '8302496055', '8302496085', '8302500000', '8302603000', '8302609000',
                                      '8305100050', '8306300000', '8414596590', '8415908025', '8415908045', '8415908085', '8418998005', '8418998050',
                                      '8418998060', '8419505000', '8419901000', '8422900640', '8424909080', '8473302000', '8473305100', '9506910010',
                                      '9506910020', '9506910030', '9506990510', '9506990520', '9506990530', '8479899599', '8479908500', '8479909596',
                                      '8481909060', '8481909085', '8486900000', '8487900080', '8503009520', '8508700000', '8513902000', '8515902000',
                                      '8516905000', '8516908050', '8517710000', '8517790000', '8529907300', '8529909760', '8536908585', '8538100000',
                                      '8541900000', '8543908885', '8547900020', '8547900030', '8547900040', '9506991500', '9506992000', '9506992580',
                                      '9506992800', '9506995500', '9506996080', '8708103050', '8708295160', '8708806590', '8708996890', '8716805010',
                                      '8807300060', '9013908000', '9031909195', '9401999081', '9403991040', '9403999010', '9403999015', '9403999020',
                                      '9403999040', '9403999045', '9405994020', '9506114080', '9506514000', '9506516000', '9506594040', '9506702090',
                                      '9507302000', '9507304000', '9507306000', '9507308000', '9507906000', '9603908050', '2203000060', '2203000090'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038568', '99038570'],
                }
            ],

            'special_describes': {
                '99038567': [
                    {
                        'specialDescribeCn': '<b>9903.85.67（加征）</b><br>铝产品，不包括衍生产品，且这些产品为俄罗斯生产，或在制造过程中使用了任何在俄罗斯冶炼的原铝，或在俄罗斯铸造的铝制品，根据注释19(a)(vii)(A)或注释19(m)(A)的规定，适用于细分(g)中规定的条款，具体以消费进口或从仓库提取消费的日期为准。',
                        'specialDescribeEn': 'Aluminum products except derivative articles that are the product of Russia, or where any amount of primary aluminum used in the manufacture of the aluminum articles is smelted in Russia, or where the aluminum articles are cast in Russia, the foregoing under the terms of note 19(a)(vii)(A) or note 19(m)(A), provided for in subdivision (g), as applicable per the date of entry for consumption or withdrawal from warehouse for consumption.',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038569': [
                    {
                        'specialDescribeCn': '<b>9903.85.69（加征）</b><br>铝产品，不包括衍生产品，且这些产品为俄罗斯生产，或在制造过程中使用了任何在俄罗斯冶炼的原铝，或在俄罗斯铸造的铝制品，根据注释19(a)(vii)(A)或注释19(m)(A)的规定，适用于细分(g)中规定的条款，具体以消费进口或从仓库提取消费的日期为准。',
                        'specialDescribeEn': 'Aluminum products except derivative articles that are the product of Russia, or where any amount of primary aluminum used in the manufacture of the aluminum articles is smelted in Russia, or where the aluminum articles are cast in Russia, the foregoing under the terms of note 19(a)(vii)(A) or note 19(m)(A), provided for in subdivision (g), as applicable per the date of entry for consumption or withdrawal from warehouse for consumption.',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038568': [
                    {
                        'specialDescribeCn': '<b>9903.85.68（加征）</b><br>铝衍生产品，若其为俄罗斯生产，或在制造过程中使用了任何在俄罗斯冶炼的原铝，或在俄罗斯铸造的铝制品，且此类衍生产品属于注释19(a)(iii)或注释19(i)、19(j)或19(k)中列举的税目或子目，具体以消费进口或从仓库提取消费的日期为准。',
                        'specialDescribeEn': 'Derivative aluminum articles that are products of Russia, or where any amount of primary aluminum used in the manufacture of the aluminum articles is smelted in Russia, or where the aluminum articles are cast in Russia, when such derivative articles are provided for in the headings or subheadings enumerated in note 19(a)(iii) or notes 19(i), 19(j) or 19(k) as applicable per the date of entry for consumption or withdrawal from warehouse for consumption.',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038570': [
                    {
                        'specialDescribeCn': '<b>9903.85.70（加征）</b><br>铝衍生产品，若其为俄罗斯生产，或在制造过程中使用了任何在俄罗斯冶炼的原铝，或在俄罗斯铸造的铝制品，且此类衍生产品属于注释19(a)(iii)或注释19(i)、19(j)或19(k)中列举的税目或子目，具体以消费进口或从仓库提取消费的日期为准。',
                        'specialDescribeEn': 'Derivative aluminum articles that are products of Russia, or where any amount of primary aluminum used in the manufacture of the aluminum articles is smelted in Russia, or where the aluminum articles are cast in Russia, when such derivative articles are provided for in the headings or subheadings enumerated in note 19(a)(iii) or notes 19(i), 19(j) or 19(k) as applicable per the date of entry for consumption or withdrawal from warehouse for consumption.',
                        'effectiveDate': '20250312'
                    },
                ]
            },
        },

        {
            'fix_rate': '25%',  # 对全部国家征收钢铝或衍生品  25%
            'exclude_search_by_name': 0,
            'rules': [
                {
                    # 对全部国家征收铝-0312 铝制衍生品1
                    'code_matchers': [
                        {
                            'patterns': ['^(76101000|76109000|76129010)\\d+$'],
                            'codes': ['7615102015', '7615102025', '7615103015', '7615103025', '7615105020', '7615105040', '7615107125', '7615107130',
                                      '7615107155', '7615107180', '7615109100', '7615200000', '7616109090', '7616991000', '7616995130', '7616995140',
                                      '7616995190'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038507'],
                },

                {
                    # 对全部国家征收铝-0312 铝制衍生品2
                    'code_matchers': [
                        {
                            'patterns': ['^(87081060|94031000|94032000)\\d+$'],
                            'codes': ['6603908100', '8302103000', '8302106030', '8302106060', '8302106090', '8302200000', '8302303010', '8302303060',
                                      '8302413000', '8302416015', '8302416045', '8302416050', '8302416080', '8302423010', '8302423015', '8302423065',
                                      '8302496035', '8302496045', '8302496055', '8302496085', '8302500000', '8302603000', '8302609000', '8305100050',
                                      '8306300000', '8414596590', '8415908025', '8415908045', '8415908085', '8418998005', '8418998050', '8418998060',
                                      '8419505000', '8419901000', '8422900640', '8424909080', '8473302000', '8473305100', '9506910010', '9506910020',
                                      '9506910030', '9506990510', '9506990520', '9506990530', '8479899599', '8479908500', '8479909596', '8481909060',
                                      '8481909085', '8486900000', '8487900080', '8503009520', '8508700000', '8513902000', '8515902000', '8516905000',
                                      '8516908050', '8517710000', '8517790000', '8529907300', '8529909760', '8536908585', '8538100000', '8541900000',
                                      '8543908885', '8547900020', '8547900030', '8547900040', '9506991500', '9506992000', '9506992580', '9506992800',
                                      '9506995500', '9506996080', '8708103050', '8708295160', '8708806590', '8708996890', '8716805010', '8807300060',
                                      '9013908000', '9031909195', '9401999081', '9403991040', '9403999010', '9403999015', '9403999020', '9403999040',
                                      '9403999045', '9405994020', '9506114080', '9506514000', '9506516000', '9506594040', '9506702090', '9507302000',
                                      '9507304000', '9507306000', '9507308000', '9507906000', '9603908050', '2203000060', '2203000090'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038508'],
                },

                {
                    # 对全部国家征收钢-0312 钢制衍生品1
                    'code_matchers': [
                        {
                            'patterns': [
                                '^(73012010|73012050|73023000|73072110|73072150|73072210|73072250|73072300|73072900|73079110|73079130|73079150|73079230|73079290|73079330|73079360|73079390|73079910|73079930|73079950|73081000|73082000|73083010|73083050|73084000|73089030|73089060|73089070|73089095|73090000|73101000|73102100|73102900|73110000|73121005|73121010|73121020|73121030|73121050|73121060|73121070|73121080|73121090|73129000|73130000|73141210|73141220|73141230|73141260|73141290|73141410|73141420|73141430|73141460|73141490|73141901|73142000|73143110|73143150|73143900|73144100|73144200|73144930|73144960|73145000|73151100|73151200|73151900|73152010|73152050|73158100|73158210|73158230|73158250|73158270|73158910|73158930|73158950|73159000|73160000|73170010|73170020|73170030|73170055|73170065|73170075|73181100|73181200|73181300|73181410|73181450|73181520|73181540|73181550|73181560|73181580|73181600|73181900|73182100|73182200|73182300|73182400|73182900|73194020|73194030|73194050|73199010|73199090|73201030|73201060|73201090|73202010|73202050|73209010|73209050|73211110|73211130|73211160|73211200|73211900|73218110|73218150|73218210|73218250|73218900|73219010|73219020|73219040|73219050|73219060|73221900|73229000|73231000|73239300|73239400|73239910|73239930|73239950|73239970|73239990|73241000|73242900|73249000|73259100|73259910|73259950|73261100|73261900|73262000|73269010|73269025|73269035|73269045|73269060|73269086)\\d+$'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038190'],
                },

                {
                    # 对全部国家征收钢-0312 钢制衍生品2
                    'code_matchers': [
                        {
                            'patterns': ['^(84313100|84314200|84314910|84314990|84321000|84329000|85479000|94032000|94059920|94059940|94062000|94069001)\\d+$'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038191'],
                },

                {
                    # 对国家征收铝-180323 铝制品
                    'code_matchers': [
                        {
                            'patterns': ['^(7601|7604|7605|7606|7607|7608|7609)\\d+$'],
                            'codes': ['7616995160', '7616995170'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038502'],
                },

                {
                    # 对国家征收铝-180323 铝制衍生品
                    'code_matchers': [
                        {
                            'patterns': ['^(76141050|76149020|76149040|76149050|87081030|87082921)\\d+$'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038504'],
                },

                {
                    # 对国家征收钢-180323 钢制品
                    'code_matchers': [
                        {
                            'patterns': ['^(72166100|72166900|72169100)\\d+$'],
                            'type': 'exclude',
                        },
                        {
                            'patterns': [
                                '^(7208|7209|7210|7211|7212|7225|7226|7313|7314|7315|7227|7228|7216|7217|7229|73011000|730210|73024000|73029000|7304|7305|7306|7307|7218|7219|7220|7221|7222|7223|7224)\\d+$'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038187'],
                },

                {
                    # 对国家征收钢-180323 钢制衍生品
                    'code_matchers': [
                        {
                            'patterns': ['^(73170030|87081030|87082921)\\d+$'],
                            'codes': ['7317005503', '7317005505', '7317005507', '7317005560', '7317005580', '7317006560'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038189'],
                },

                {
                    # 铝衍生品豁免
                    'code_matchers': [
                        {
                            'patterns': ['^(76101000|76109000|87081060|94031000|94032000|76129010)\\d+$'],
                            'codes': ['7615102015', '7615102025', '7615103015', '7615103025', '7615105020', '7615105040', '7615107125', '7615107130',
                                      '7615107155', '7615107180', '7615109100', '7615200000', '7616109090', '7616991000', '7616995130', '7616995140',
                                      '7616995190', '6603908100', '8302103000', '8302106030', '8302106060', '8302106090', '8302200000', '8302303010',
                                      '8302303060', '8302413000', '8302416015', '8302416045', '8302416050', '8302416080', '8302423010', '8302423015',
                                      '8302423065', '8302496035', '8302496045', '8302496055', '8302496085', '8302500000', '8302603000', '8302609000',
                                      '8305100050', '8306300000', '8414596590', '8415908025', '8415908045', '8415908085', '8418998005', '8418998050',
                                      '8418998060', '8419505000', '8419901000', '8422900640', '8424909080', '8473302000', '8473305100', '9506910010',
                                      '9506910020', '9506910030', '9506990510', '9506990520', '9506990530', '8479899599', '8479908500', '8479909596',
                                      '8481909060', '8481909085', '8486900000', '8487900080', '8503009520', '8508700000', '8513902000', '8515902000',
                                      '8516905000', '8516908050', '8517710000', '8517790000', '8529907300', '8529909760', '8536908585', '8538100000',
                                      '8541900000', '8543908885', '8547900020', '8547900030', '8547900040', '9506991500', '9506992000', '9506992580',
                                      '9506992800', '9506995500', '9506996080', '8708103050', '8708295160', '8708806590', '8708996890', '8716805010',
                                      '8807300060', '9013908000', '9031909195', '9401999081', '9403991040', '9403999010', '9403999015', '9403999020',
                                      '9403999040', '9403999045', '9405994020', '9506114080', '9506514000', '9506516000', '9506594040', '9506702090',
                                      '9507302000', '9507304000', '9507306000', '9507308000', '9507906000', '9603908050', '2203000060', '2203000090'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038509'],
                },

                {
                    # 钢衍生品豁免
                    'code_matchers': [
                        {
                            'patterns': [
                                '^(73012010|73012050|73023000|73072110|73072150|73072210|73072250|73072300|73072900|73079110|73079130|73079150|73079230|73079290|73079330|73079360|73079390|73079910|73079930|73079950|73081000|73082000|73083010|73083050|73084000|73089030|73089060|73089070|73089095|73090000|73101000|73102100|73102900|73110000|73121005|73121010|73121020|73121030|73121050|73121060|73121070|73121080|73121090|73129000|73130000|73141210|73141220|73141230|73141260|73141290|73141410|73141420|73141430|73141460|73141490|73141901|73142000|73143110|73143150|73143900|73144100|73144200|73144930|73144960|73145000|73151100|73151200|73151900|73152010|73152050|73158100|73158210|73158230|73158250|73158270|73158910|73158930|73158950|73159000|73160000|73170010|73170020|73170030|73170055|73170065|73170075|73181100|73181200|73181300|73181410|73181450|73181520|73181540|73181550|73181560|73181580|73181600|73181900|73182100|73182200|73182300|73182400|73182900|73194020|73194030|73194050|73199010|73199090|73201030|73201060|73201090|73202010|73202050|73209010|73209050|73211110|73211130|73211160|73211200|73211900|73218110|73218150|73218210|73218250|73218900|73219010|73219020|73219040|73219050|73219060|73221900|73229000|73231000|73239300|73239400|73239910|73239930|73239950|73239970|73239990|73241000|73242900|73249000|73259100|73259910|73259950|73261100|73261900|73262000|73269010|73269025|73269035|73269045|73269060|73269086|84313100|84314200|84314910|84314990|84321000|84329000|85479000|94032000|94059920|94059940|94062000|94069001)\\d+$'],
                            'type': 'include',
                        }
                    ],
                    'special_code': ['99038192'],
                },

            ],

            'special_describes': {
                '99038187': [
                    {
                        'specialDescribeCn': '<b>9903.81.87（加征）</b><br>列在细分j中的铁或钢产品（不包括衍生产品）<br>99038188（税率25%）：/除 （l）、（m） 和 （n） 小节中列出的衍生物品外，在 2025 年 3 月 12 日之前以“外国特权身份”进入美国对外贸易区，并在 2025 年 3 月 12 日或之后入境消费的钢铁产品。',
                        'specialDescribeEn': 'Iron or steel products listed in subdivision j (except derivative articles) <br>99038188：/Iron or steel products except for derivative articles listed in subdivision (l), (m) and (n) that are admitted to a U.S. foreign trade zone under “privileged foreign status” before March 12, 2025, and entered for consumption on or after March 12, 2025.',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038189': [
                    {
                        'specialDescribeCn': '<b>9903.81.89（加征）</b><br>列在细分(l)中的铁或钢衍生产品（受第232条约束的现有钢铁衍生产品）<br>99038193（税率25%）：/在2025年3月12日之前以“外国特权身份”进入美国对外贸易区，并在2025年3月1日或之后进入消费的（l）和（m）小节中规定的钢铁衍生产品（现有衍生钢铁产品和第73章中的新衍生钢铁产品）。',
                        'specialDescribeEn': 'Derivative iron or steel products listed in subdivision (l) (existing steel derivative articles subject to Section 232) <br>99038193：/Derivative products of iron or steel, as specified in subdivisions (l) and (m) (existing derivative steel products, and new derivative steel products in Chapter 73) admitted to a U.S. foreign trade zone under “privileged foreign status” before March 12, 2025, and entered for consumption on or after March 1, 2025.',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038502': [
                    {
                        'specialDescribeCn': '<b>9903.85.02（加征）</b><br>如细分(g)中规定的铝产品，不包括衍生产品',
                        'specialDescribeEn': 'Aluminum products as specified in subdivision (g), except derivative articles',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038504': [
                    {
                        'specialDescribeCn': '<b>9903.85.04（加征）</b><br>列在细分(i)中的铝衍生产品（受第232条约束的现有铝衍生产品）',
                        'specialDescribeEn': 'Derivative aluminum products listed in subdivision (i) (existing aluminum derivative articles subject to Section 232)',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038190': [
                    {
                        'specialDescribeCn': '<b>9903.81.90（加征）</b><br>列在细分(m)中的铁或钢衍生产品（属于第73章且受第232条约束的新钢铁衍生产品）<br>99038193（税率25%）：/在2025年3月12日之前以“外国特权身份”进入美国对外贸易区，并在2025年3月1日或之后进入消费的（l）和（m）小节中规定的钢铁衍生产品（现有衍生钢铁产品和第73章中的新衍生钢铁产品）。<br>99038192（税率0%）：在子项 (m) 或子项 (n) 中列出的衍生铁或钢产品（由在美国熔炼和浇铸的钢材在其他国家加工而成的新钢铁衍生制品）。',
                        'specialDescribeEn': 'Derivative iron or steel products listed in subdivision (m) (new steel derivative articles classified in Chapter 73 subject to Section 232)<br>99038193：/Derivative products of iron or steel, as specified in subdivisions (l) and (m) (existing derivative steel products, and new derivative steel products in Chapter 73) admitted to a U.S. foreign trade zone under “privileged foreign status” before March 12, 2025, and entered for consumption on or after March 1, 2025.<br>99038192：Derivative steel or iron products listed in subdivision (m) or (n) (new derivative steel articles) where the derivative iron or steel product was processed in another country from steel articles that were melted and poured in the United States.',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038191': [
                    {
                        'specialDescribeCn': '<b>9903.81.91（加征）</b><br>第 （n） 小节中列出的衍生钢铁或钢铁产品（未在第 73 章中分类的新钢铁衍生物品，受第 232 节的约束）：进口关税按钢含量的价值征收（见下面的说明）:<br>对于第 73 章以外的新钢材衍生品，应根据钢含量值使用 HTS 9903.81.91 报告25% 的关税。如果钢含量值与输入值相同或未知，则必须根据 HTS 9903.81.91 根据整个输入值报告关税，并且仅在一个条目摘要行上报告。<br>如果钢含量值小于进口物品的输入值，则必须在两行中报告货物。第一行表示非钢含量，第二行表示钢含量。每一行都应按照以下说明进行报告。<br>99038192（税率0%）：在子项 (m) 或子项 (n) 中列出的衍生铁或钢产品（由在美国熔炼和浇铸的钢材在其他国家加工而成的新钢铁衍生制品）。',
                        'specialDescribeEn': 'Derivative iron or steel products listed in subdivision (n) (new steel derivative articles not classified in Chapter 73 subject to Section 232):  the import duty is on the value of the steel content (see instructions below):<br>For new steel derivatives outside of Chapter 73, the 25 percent duty is to be reported with HTS 9903.81.91 based upon the value of the steel content<br>If the value of the steel content is the same as the entered value or is unknown, the duty must be reported under HTS 9903.81.91 based on the entire entered value, and report on only one entry summary line.<br>In the case where the value of the steel content is less than the entered value of the imported article, the good must be reported on two lines.  The first line will represent the non-steel content while the second line will represent the steel content.  Each line should be reported in accordance with the below instructions.<br>99038192：Derivative steel or iron products listed in subdivision (m) or (n) (new derivative steel articles) where the derivative iron or steel product was processed in another country from steel articles that were melted and poured in the United States.',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038507': [
                    {
                        'specialDescribeCn': '<b>9903.85.07（加征）</b><br>列在细分(j)中的铝衍生产品（属于第76章且受第232条约束的新铝衍生产品）<br>99038509（税率0%）：在子项 (j) 或子项 (k) 中列出的衍生钢制品（即新的衍生铝制品），其中衍生铝产品是由在美国熔炼和铸造的铝制品在其他国家加工而成的。',
                        'specialDescribeEn': 'Derivative aluminum products listed in subdivision (j) (new aluminum derivative articles classified in Chapter 76 subject to Section 232)<br>99038509：Derivative steel articles listed in subdivision (j) or (k) (new derivative aluminum articles), where the derivative aluminum products were processed in another country from aluminum articles that were smelted and cast in the United States.',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038508': [
                    {
                        'specialDescribeCn': '<b>9903.85.08（加征）</b><br>在子项 (k) 中列出的衍生铝产品（不属于第 76 章分类、但受 232 条款约束的新铝衍生制品）：进口关税基于铝含量的价值计算（详见以下说明）:<br>对于未在第 76 章中分类的新铝衍生物，应根据铝含量的值报告 25% 的关税。<br>如果铝含量值与输入的值相同或未知，则必须根据整个输入值在 9903.85.08 下报告关税，并且仅在一个条目摘要行上报告。<br>如果铝含量值小于进口物品的输入值，则必须在两行中报告商品。第一行代表非铝含量，第二行代表铝含量。每一行都应按照以下说明进行报告。<br>99038509（税率0%）：在子项 (j) 或子项 (k) 中列出的衍生钢制品（即新的衍生铝制品），其中衍生铝产品是由在美国熔炼和铸造的铝制品在其他国家加工而成的。',
                        'specialDescribeEn': 'Derivative aluminum products listed in subdivision (k) (new aluminum derivative articles not classified in Chapter 76 subject to Section 232):  the import duty is based upon the value of the aluminum content (see instructions below):<br>For new aluminum derivatives not classified in Chapter 76, the 25 percent duty is to be reported based upon the value of the aluminum content. <br>If the value of the aluminum content is the same as the entered value or is unknown, duty must be reported under 9903.85.08 based on the entire entered value, and on only one entry summary line.<br>In the case where the value of the aluminum content is less than the entered value of the imported article, the good must be reported on two lines.  The first line will represent the non-aluminum content, the second line will represent the aluminum content.  Each line should be reported in accordance with the below instructions.<br>99038509：Derivative steel articles listed in subdivision (j) or (k) (new derivative aluminum articles), where the derivative aluminum products were processed in another country from aluminum articles that were smelted and cast in the United States.',
                        'effectiveDate': '20250312'
                    },
                ],
                '99038509': [
                    {
                        'specialDescribeCn': '<b>豁免</b><br>在子项 (j) 或子项 (k) 中列出的衍生钢制品（即新的衍生铝制品），其中衍生铝产品是由在美国熔炼和铸造的铝制品在其他国家加工而成的。',
                        'specialDescribeEn': 'Derivative steel articles listed in subdivision (j) or (k) (new derivative aluminum articles), where the derivative aluminum products were processed in another country from aluminum articles that were smelted and cast in the United States.',
                        'effectiveDate': '20250312',
                        'exempting': '有',
                        'specialInfo': '有'
                    },
                ],
                '99038192': [
                    {
                        'specialDescribeCn': '<b>豁免</b><br>在子项 (m) 或子项 (n) 中列出的衍生铁或钢产品（由在美国熔炼和浇铸的钢材在其他国家加工而成的新钢铁衍生制品）。',
                        'specialDescribeEn': 'Derivative steel or iron products listed in subdivision (m) or (n) (new derivative steel articles) where the derivative iron or steel product was processed in another country from steel articles that were melted and poured in the United States.',
                        'effectiveDate': '20250312',
                        'exempting': '有',
                        'specialInfo': '有'
                    },
                ],
            },
        },
        {
            'fix_rate': '25%',  # 汽车加征 25%
            'rules': [
                {
                    'code_matchers': [
                        {
                            'patterns': [
                                '^(87032201|87033101|87034000|87037000|87042101|87045100|87032301|87033201|87035000|87038000|87043101|87046000|87032401|87033301|87036000|87039001|87044100)\\d+$'],
                            'type': 'include',
                            'exclude_special_codes': ['99038567', '99038568'],
                        },
                    ],
                    'special_code': ['99039401'],
                }
            ],

            'special_describes': {
                '99039401': [
                    {
                        'specialDescribeCn': '<b>9903.94.01（加征）</b><br>除税号9903.94.02、9903.94.03和9903.94.04外，自2025年4月3日起，本分章注释33所规定的乘用车（轿车、运动型多用途车（SUV）、跨界多用途车（CUV）、小型货车及货运厢式车）和轻型卡车，按照本分章美国注释33(b)款的规定执行。',
                        'specialDescribeEn': 'Except for 9903.94.02, 9903.94.03, and 9903.94.04, effective with respect to entries on or after April 3, 2025, passenger vehicles (sedans, sport utility vehicles, crossover utility vehicles, minivans, and cargo vans) and light trucks, as specified in note 33 to this subchapter, as provided for in subdivision (b) of U.S. note 33 to this subchapter. ',
                        'effectiveDate': '20250403',
                    },
                    {
                        'specialDescribeCn': '<b>9903.94.02（豁免）</b><br>自2025年4月3日起，本分章美国注释33(c)款所规定的商品正式生效并适用相关规定。(i) 所有符合本注释(b)款所列《美国统一关税表》（HTSUS）税目规定的商品，但不包括乘用车（轿车、运动型多用途车（SUV）、跨界多用途车（CUV）、小型货车及货运厢式车）和轻型卡车；(ii) 本注释(d)款所述的乘用车和轻型卡车中的美国原产部分，需经商务部长批准后适用。',
                        'specialDescribeEn': 'Effective with respect to entries on or after April 3, 2025, articles as provided for in subdivision (c) of U.S. note 33 to this subchapter.(i) all entries of articles classifiable under provisions of the HTSUS enumerated in subdivision (b) of this note, but that are not passenger vehicles (sedans, sport utility vehicles, crossover utility vehicles, minivans, and cargo vans) and light trucks; as well as (ii) the U.S. content of passenger vehicles and light trucks described in subdivision (d) of this note, upon approval from the Secretary of Commerce.',
                        'effectiveDate': '20250403',
                        'exempting': '有',
                        'specialInfo': '有'
                    },
                    {
                        'specialDescribeCn': '<b>9903.94.03（豁免）</b><br>自2025年4月3日起，本分章美国注释33(d)款所规定的特定乘用车和轻型卡车正式生效并适用相关规定。适用于符合《美墨加协定》（USMCA）特殊关税待遇的乘用车和轻型卡车中的非美国原产部分，需经商务部长批准，方可仅对汽车的非美国原产部分适用25%的从价税税率。',
                        'specialDescribeEn': 'Effective with respect to entries on or after April 3, 2025, certain passenger vehicles and light trucks, as provided for in subdivision (d) of U.S. note 33 to this subchapter.<br>Applies to the non-U.S. content of passenger vehicles and light trucks eligible for special tariff treatment under the United States-Mexico-Canada Agreement (USMCA), upon approval from the Secretary of Commerce to apply the 25% ad valorem rates of duty exclusively to the value of the non-U.S. content of the automobile.',
                        'effectiveDate': '20250403',
                        'exempting': '有',
                        'specialInfo': '有'
                    },
                    {
                        'specialDescribeCn': '<b>9903.94.04（豁免）</b><br>自2025年4月3日起，本分章美国注释33(e)款所规定的特定乘用车和轻型卡车正式生效并适用相关规定。适用于所有国家的乘用车和轻型卡车，这些车辆符合上述税号或子目分类要求，并且其生产年份至少早于进口年份25年。',
                        'specialDescribeEn': 'Effective with respect to entries on or after April 3, 2025, certain passenger vehicles and light trucks, as provided  for in subdivision (e) of U.S. note 33 to this subchapter.<br>Applies to all entries of passenger vehicles and light trucks from all countries classifiable in the headings or subheadings listed above that were manufactured in a year at least 25 years prior to the year of the date of entry.',
                        'effectiveDate': '20250403',
                        'exempting': '有',
                        'specialInfo': '有'
                    },
                ],
            },
        },
        {
            'fix_rate': '-',  # 汽车加征 25% 5.3 日生效
            'rules': [
                {
                    'code_matchers': [
                        {
                            'patterns': [
                                '^(8707|8471|732010|840732|850134|850152|870829|870870|870895|901510|830230|840733|850132|850140|850710|852721|853710|870830|870880|902910|840734|850133|850151|850760|852729|853720|870822|870850|870891|870894|40112010|40122060|83021030|84082020|84133010|84212300|84269100|84821010|84824000|84831030|85079040|85112000|85114000|85118060|85122020|85124020|85129060|87060003|87060025|87081060|87084070|87089360|87089958|94012000|40111010|40121940|70072151|73202010|84133090|84148005|84213200|84825000|85079080|85115000|85122040|85124040|85129070|87060005|87082100|87084075|87089375|87089953|87089968|40111050|40121980|70091000|83012000|84073100|84139110|84145930|84152000|84254900|85118020|85123000|85129020|85198120|85443000|87060015|87081030|87084011|87089955|87169050)\\d+$'],
                            'codes': ['4009120020', '4009420020', '4016996010', '8413919010', '8414596540', '8482200020', '8482200061', '8525601010',
                                      '8536410005', '8539100010', '8707100040', '8707905060', '4009220020', '4013100010', '8409911040', '8414308030',
                                      '8431100090', '8482105044', '8482200030', '8482200070', '8511300040', '8511906020', '8539100050', '8707905020',
                                      '8707905080', '4009320020', '4013100020', '8409991040', '8482105048', '8482200040', '8482200081', '8483101030',
                                      '8511100000', '8511300080', '8511906040', '8707100020', '8707905040', '9029204080'],
                            'type': 'include',
                            'exclude_special_codes': ['99038567', '99038568'],
                        },
                    ],
                    'special_code': ['99039405'],
                }
            ],

            'special_describes': {
                '-': [
                    {
                        'specialDescribeCn': '除税号9903.94.06外，自2025年5月3日起，本分章美国注释33(g)款所规定的汽车零部件正式生效并适用相关规定。',
                        'specialDescribeEn': 'Except for 9903.94.06, effective with respect to entries on or after May 3, 2025, automobile parts, as provided for in subdivision (g) of U.S. note 33 to this subchapter.',
                        'effectiveDate': '20250503',
                        'specialInfo': '25%(5.3开征)'
                    }
                ]
            }
        },
        {
            'fix_rate': '10%',  # 普遍加征 10%
            'rules': [
                {
                    'code_matchers': [
                        {
                            'patterns': [
                                "^(05080000|25041050|25049000|25101000|25102000|25111010|25111050|25191000|25199010|25199020|25249000|25292100|25292200|25302010|25302020|25309010|25309020|25309080|26020000|26030000|26050000|26060000|26080000|26100000|26110030|26110060|26121000|26140030|26140060|26159030|26159060|26161000|26171000|26203000|26209950|27011100|27011200|27011900|27012000|27021000|27022000|27030000|27040000|27050000|27060000|27071000|27072000|27073000|27074000|27075000|27079100|27079910|27079920|27079940|27079951|27079955|27079959|27079990|27081000|27082000|27090010|27090020|27101215|27101218|27101225|27101245|27101290|27101906|27101911|27101916|27101924|27101925|27101926|27101930|27101935|27101940|27101945|27101990|27102005|27102010|27102015|27102025|27109100|27109905|27109910|27109916|27109921|27109931|27109932|27109939|27109945|27109990|27111100|27111200|27111300|27111400|27111900|27112100|27112900|27121000|27122000|27129010|27129020|27131100|27131200|27132000|27139000|27141000|27149000|27150000|27160000|28012000|28042900|28045000|28046100|28048000|28049000|28051910|28051920|28051990|28053000|28111100|28111910|28112910|28112920|28121900|28139010|28152000|28161000|28164010|28164020|28170000|28181010|28181020|28182000|28183000|28201000|28211000|28212000|28220000|28230000|28252000|28255030|28256000|28258000|28259015|28259030|28259090|28261200|28263000|28269090|28273100|28273945|28273960|28273990|28274100|28274950|28275951|28276010|28276051|28332100|28332500|28332700|28332910|28332945|28332951|28342100|28342920|28342951|28366000|28369100|28369200|28369910|28369950|28418000|28419020|28419040|28432901|28433000|28439000|28441010|28441020|28442000|28443020|28443050|28444300|28459001|28461000|28469020|28469040|28469080|28492010|28492020|28499030|28539010|28539090|29034510|29035990|29036990|29037800|29037990|29038915|29038920|29038970|29039200|29049940|29052990|29053990|29055910|29055990|29061950|29062960|29072990|29081960|29091918|29092000|29093060|29094910|29094915|29094920|29094960|29095040|29095045|29095050|29121950|29124926|29141900|29144090|29145030|29145050|29146200|29146921|29146990|29147940|29152930|29153931|29153935|29153947|29153990|29159010|29159014|29159018|29159020|29159050|29161930|29161950|29162050|29163150|29163946|29163979|29171300|29171910|29171970|29173401|29173930|29181151|29181350|29181650|29181960|29181990|29182210|29182250|29182330|29182350|29182920|29182965|29182975|29183025|29183030|29183090|29189930|29189943|29189947|29189950|29199030|29199050|29209051|29211911|29211961|29212900|29213010|29213050|29214290|29214600|29214938|29214943|29214945|29214950|29215980|29221100|29221400|29221909|29221920|29221933|29221960|29221970|29221990|29221996|29222927|29222961|29222981|29223100|29223925|29223945|29223950|29224100|29224250|29224400|29224910|29224926|29224930|29224937|29224949|29224980|29225007|29225010|29225011|29225013|29225014|29225017|29225025|29225035|29225040|29225050|29231000|29232020|29239001|29241100|29241911|29241980|29242116|29242150|29242910|29242962|29242971|29242977|29242995|29251200|29251942|29251991|29252100|29252920|29252960|29252990|29263010|29264000|29269014|29269043|29269048|29270040|29270050|29280025|29280030|29280050|29299020|29299050|29302020|29302090|29303060|29309029|29309049|29309092|29314900|29315300|29319022|29319090|29321400|29321951|29322020|29322030|29322050|29329961|29329970|29329990|29331100|29331935|29331945|29331990|29332100|29332920|29332935|29332943|29332945|29332990|29333301|29333400|29333500|29333700|29333908|29333910|29333920|29333921|29333923|29333925|29333927|29333931|29333941|29333961|29333992|29334100|29334908|29334910|29334915|29334917|29334920|29334926|29334930|29334960|29334970|29335210|29335290|29335300|29335400|29335910|29335915|29335918|29335921|29335922|29335936|29335946|29335953|29335959|29335970|29335980|29335985|29335995|29336960|29337200|29337908|29337915|29337985|29339100|29339901|29339902|29339905|29339906|29339908|29339911|29339912|29339916|29339917|29339922|29339924|29339926|29339942|29339946|29339951|29339953|29339955|29339958|29339961|29339965|29339970|29339975|29339979|29339982|29339985|29339989|29339990|29339997|29341010|29341020|29341090|29342040|29342080|29343023|29343027|29343043|29343050|29349100|29349200|29349901|29349903|29349905|29349906|29349907|29349908|29349909|29349911|29349912|29349915|29349916|29349918|29349920|29349930|29349939|29349944|29349947|29349970|29349990|29355000|29359006|29359010|29359013|29359015|29359020|29359030|29359032|29359033|29359042|29359048|29359060|29359075|29359095|29362100|29362200|29362300|29362401|29362500|29362600|29362700|29362800|29362910|29362916|29362920|29362950|29369001|29371100|29371200|29371900|29372100|29372200|29372310|29372325|29372350|29372910|29372990|29375000|29379005|29379010|29379020|29379040|29379045|29379090|29381000|29389000|29391100|29391910|29391920|29391950|29392000|29393000|29394100|29394200|29394400|29394500|29394903|29395900|29396200|29396300|29396900|29397200|29397900|29398000|29400060|29411010|29411020|29411030|29411050|29412010|29412050|29413000|29414000|29415000|29419010|29419030|29419050|29420005|29420035|29420050|30012000|30019001|30021200|30021300|30021400|30021500|30024100|30024200|30024900|30025100|30025900|30029010|30029052|30031000|30032000|30033910|30033950|30034100|30034200|30034900|30039001|30041010|30041050|30042000|30043100|30043200|30043900|30044100|30044200|30044900|30045010|30045020|30045030|30045040|30045050|30046000|30049010|30049092|30063010|30063050|30066000|30067000|30069310|30069320|30069350|30069360|30069380|31042000|31043000|31049001|31051000|31052000|31056000|32030080|32041380|32041720|32041800|32061100|32061900|34024210|34024220|34024290|36069030|38089410|38089450|38180000|38249100|38249929|38249949|38249955|38249993|39019090|39029000|39046100|39059110|39059980|39069050|39071000|39072100|39072900|39073000|39076100|39076900|39077000|39079950|39081000|39100000|39119025|39119091|39123100|39123900|39129000|39139020|39139050|39140060|40011000|40012100|40012200|40012900|40013000|44011100|44011200|44012100|44012200|44013100|44013200|44013942|44014100|44014900|44021000|44022000|44029001|44031100|44031200|44032101|44032201|44032301|44032401|44032501|44032601|44034200|44034902|44039100|44039301|44039401|44039501|44039601|44039700|44039800|44039901|44041000|44042000|44050000|44061100|44061200|44069100|44069200|44071100|44071200|44071300|44071400|44071900|44072100|44072200|44072301|44072500|44072600|44072700|44072800|44072902|44079100|44079200|44079300|44079400|44079500|44079600|44079700|44079902|44081001|44083101|44083902|44089001|44091005|44091010|44091020|44091040|44091045|44091050|44091060|44091065|44091090|44092105|44092190|44092205|44092210|44092225|44092240|44092250|44092260|44092265|44092290|44092906|44092911|44092926|44092941|44092951|44092961|44092966|44092991|44101100|44101200|44101900|44109000|44111210|44111220|44111230|44111260|44111290|44111310|44111320|44111330|44111360|44111390|44111410|44111420|44111430|44111460|44111490|44119210|44119220|44119230|44119240|44119310|44119320|44119330|44119360|44119390|44119400|44121005|44121090|44123106|44123126|44123142|44123145|44123148|44123152|44123161|44123192|44123306|44123326|44123332|44123357|44123426|44123432|44123457|44123910|44123930|44123940|44123950|44124100|44124200|44124900|44125110|44125131|44125141|44125151|44125210|44125231|44125241|44125251|44125980|44125990|44125995|44129106|44129110|44129131|44129141|44129151|44129207|44129211|44129231|44129242|44129252|44129958|44129961|44129971|44129981|44129991|44129997|44130000|48202000|49011000|49019100|49019900|49021000|49029010|49029020|49030000|49040000|49052000|49059020|49059060|49060000|49111000|49119960|49119980|71069110|71081210|71101100|71101900|71102100|71102900|71103100|71103900|71104100|71104900|71129201|71189000|72021110|72021150|72021910|72021950|72023000|72024100|72024910|72024950|72025000|72028000|72029100|72029340|72029380|72042100|74010000|74020000|74031100|74031200|74031300|74031900|74032100|74032200|74032901|74040030|74040060|74050010|74050060|74061000|74062000|74071015|74071030|74071050|74072115|74072130|74072150|74072170|74072190|74072916|74072934|74072938|74072940|74072950|74081130|74081160|74081900|74082100|74082210|74082250|74082910|74082950|74091110|74091150|74091910|74091950|74091990|74092100|74092900|74093110|74093150|74093190|74093910|74093950|74093990|74094000|74099010|74099050|74099090|74101100|74101200|74102130|74102160|74102200|74111010|74111050|74112110|74112150|74112200|74112910|74112950|74121000|74122000|74130010|74130050|74130090|74151000|74152100|74152900|74153305|74153310|74153380|74153900|74181000|74182010|74182050|74192000|74198003|74198006|74198009|74198015|74198016|74198017|74198030|74198050|75089050|79011100|79011210|79011250|79012000|79020000|79070060|80011000|80012000|80020000|80070050|81011000|81019700|81032000|81033000|81039100|81039900|81041100|81041900|81042000|81043000|81049000|81052030|81052060|81052090|81053000|81059000|81061000|81069000|81082000|81083000|81089030|81089060|81101000|81102000|81109000|81110047|81110049|81122100|81122200|81122900|81124110|81124150|81124900|81125900|81129210|81129230|81129240|81129260|81129265|81129910|81129991|85411000|85412100|85412900|85413000|85414910|85414970|85414980|85414995|85415100|85415900|85419000|85423100|85423200|85423300|85423900|85429000)\\d+$"],
                            'type': 'exclude',
                        },
                        {
                            'patterns': ['^\\d+$'],
                            'type': 'include',
                            'exclude_special_codes': ['99030101/99030105', '99030110/99030115', '99038567', '99038568', '99038507', '99038508', '99038190',
                                                      '99038191', '99038502', '99038504', '99038187', '99038189', '99039401', '99039405'],
                        },

                    ],
                    'special_code': ['99030125'],
                }
            ],

            'special_describes': {
                '99030125': [
                    {
                        'specialDescribeCn': '<b>加征</b><br>除本命令另有规定外，所有进口到美国关税区的物品应依法额外缴纳 10% 的从价税。此类税率适用于东部夏令时 2025 年 4 月 5 日凌晨 12：01 或之后进入消费或从仓库提取消费的货物，但在东部夏令时间 2025 年 4 月 5 日凌晨 12：01 之前在装货港装船并按最终过境方式过境的货物，并在东部夏令时间 2025 年 4 月 5 日凌晨 12：01 之后进入消费或从仓库提取消费的货物，无需缴纳此类额外关税。',
                        'specialDescribeEn': 'Except as otherwise provided in this order, all articles imported into the customs territory of the United States shall be, consistent with law, subject to an additional ad valorem rate of duty of 10 percent.  Such rates of duty shall apply with respect to goods entered for consumption, or withdrawn from warehouse for consumption, on or after 12:01 a.m. eastern daylight time on April 5, 2025, except that goods loaded onto a vessel at the port of loading and in transit on the final mode of transit before 12:01 a.m. eastern daylight time on April 5, 2025, and entered for consumption or withdrawn from warehouse for consumption after 12:01 a.m. eastern daylight time on April 5, 2025, shall not be subject to such additional duty.  ',
                        'effectiveDate': '20250405',
                    },
                    {
                        'specialDescribeCn': '<b>豁免</b><br>本命令附件 II 中规定的以下货物，在符合法律的情况下，不应按本命令规定的从价税率缴纳：（i） 50 U.S.C. 1702（b） 包含的所有物品;（ii） 根据 1962 年《贸易扩张法》第 232 条征收关税的所有钢和铝制品及其衍生物，并在 2018 年 3 月 8 日第 9704 号公告（调整进入美国的铝进口）中宣布，经修订，2018 年 3 月 8 日第 9705 号公告（调整进入美国的钢铁进口）， 经修订的 2020 年 1 月 24 日第 9980 号公告（调整美国的衍生铝制品和衍生钢制品的进口）、2025 年 2 月 10 日的第 10895 号公告（调整美国的铝进口）和 2025 年 2 月 10 日的第 10896 号公告（调整美国的钢材进口）;（iii） 根据 1962 年《贸易扩张法》第 232 条（经修订，并在 2025 年 3 月 26 日第 10908 号公告（调整对美国的汽车和汽车零部件进口）中宣布）征收额外关税的所有汽车和汽车零部件;（iv） 本命令附件 II 中列举的其他产品，包括铜、药品、半导体、木材制品、某些关键矿物以及能源和能源产品;（v） 来自贸易伙伴的所有物品，适用美国协调关税表 （HTSUS） 第 2 栏规定的税率;以及 （vi） 根据 1962 年《贸易扩张法》第 232 条的未来行动可能被征税的所有物品。',
                        'specialDescribeEn': 'The following goods as set forth in Annex II to this order, consistent with law, shall not be subject to the ad valorem rates of duty under this order:  (i) all articles that are encompassed by 50 U.S.C. 1702(b); (ii) all articles and derivatives of steel and aluminum subject to the duties imposed pursuant to section 232 of the Trade Expansion Act of 1962 and proclaimed in Proclamation 9704 of March 8, 2018 (Adjusting Imports of Aluminum Into the United States), as amended, Proclamation 9705 of March 8, 2018 (Adjusting Imports of Steel Into the United States), as amended, and Proclamation 9980 of January 24, 2020 (Adjusting Imports of Derivative Aluminum Articles and Derivative Steel Articles Into the United States), as amended, Proclamation 10895 of February 10, 2025 (Adjusting Imports of Aluminum Into the United States), and Proclamation 10896 of February 10, 2025 (Adjusting Imports of Steel into the United States); (iii) all automobiles and automotive parts subject to the additional duties imposed pursuant to section 232 of the Trade Expansion Act of 1962, as amended, and proclaimed in Proclamation 10908 of March 26, 2025 (Adjusting Imports of Automobiles and Automobile Parts Into the United States); (iv) other products enumerated in Annex II to this order, including copper, pharmaceuticals, semiconductors, lumber articles, certain critical minerals, and energy and energy products; (v) all articles from a trading partner subject to the rates set forth in Column 2 of the Harmonized Tariff Schedule of the United States (HTSUS); and (vi) all articles that may become subject to duties pursuant to future actions under section 232 of the Trade Expansion Act of 1962.',
                        'effectiveDate': '20250405',
                    },
                ],
            },
        },
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
        # 智能分类
        {
            'enabled': 0,
            'poster_url': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/ad/ad-popup-20250306.png',
            'link': '/pages/product/product-buy?packageCode=hs_code_member&tid=1012',
            'quiet_second': 14400,
            'pages': [
                'pages/classification/home/home',
                'pages/classification/calculator/calculator',
                'pages/classification/calculator/calculator-page',
                'pages/classification/search-by-name/search-by-name',
                'pages/customs/customs-clearance-query',
                'pages/my/my/my',
            ]
        },

        # 清关查询
        {
            'enabled': 0,
            'poster_url': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/ad/ad-popup-20250401.png',
            'link': '/pages/product/product-buy?packageCode=customs_clearance_query&tid=1012',
            'quiet_second': 14400,
            'pages': [
                'pages/classification/home/home',
                'pages/classification/calculator/calculator',
                'pages/classification/calculator/calculator-page',
                'pages/classification/search-by-name/search-by-name',
                'pages/customs/customs-clearance-query',
                'pages/my/my/my',
            ]
        }
    ],
    'home_banner_list': [
        {
            'enabled': 1,
            'poster_url': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/ad/home-banner-01.png',
            'link': '/pages/product/product-buy?packageCode=hs_code_member&tid=1013',
        },
        {
            'enabled': 1,
            'poster_url': 'https://xhq-wechat.oss-cn-shanghai.aliyuncs.com/ai-qgb/mp/images/ad/home-banner-02.png',
            'link': '/pages/product/product-buy?packageCode=customs_clearance_query&tid=1013',
        },
    ]
}

redis.set(code, json.dumps(value, ensure_ascii=False))
value = redis.get(code)
print(code, value)

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

code = 'system_config_public_ams_status'
value = ams_status
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
