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
    }
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
        'kMmemranbJIvbAtPfVSeJoOJxI1xBgOtDbN1PsCYffo',
        'kGJJvsSQBogxmJ71sGBbqNC1VclhbTcxjAXQfWmrp80',
        'MmhfyLUJ1LgfLEUQBcUV-IZdCKL9MMjMj0u9tnogF7c',
    ],
    'invite_join_group_text': '可邀请好友继续参与拼团',
    'join_now_text': '超实用!快来和我一起拼团吧!',
    'invite_join_group_promotion': '仅剩 <span style="color:#FF6600;">{remain_people}</span> 人,快呼唤小伙伴参加吧!',

    'customs_clearance_query': {
        'example_mbl': 'HLCUSZX241-DEMO',
        'no_quota_tip': '您还未购买查询条数',
        'quota_used_up_tip': '您的搜索条数已用完',
    },
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

        {  # 墨西哥 美墨加协定进口关税FREE
            'fix_rate': '-',  # 用一个短横线表示不需要增加税率，但需要参与后续逻辑处理，此处是后面需要添加豁免规则
            'include_country_list': ['MX'],
            'rules': [
                {
                    'code_matchers': [
                        {
                            'custom': 'usmca',  # hscode 前 8 位存在于 usmca 中
                            'type': 'include',
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

        {  # 加拿大 美墨加协定进口关税FREE
            'fix_rate': '-',  # 用一个短横线表示不需要增加税率，但需要参与后续逻辑处理，此处是后面需要添加豁免规则
            'include_country_list': ['CA'],
            'rules': [
                {
                    'code_matchers': [
                        {
                            'custom': 'usmca',  # hscode 前 8 位存在于 usmca 中
                            'type': 'include',
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

        {  # 俄罗斯 加征 200%
            'fix_rate': '200%',
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
                            'patterns': ['^(76101000|76109000|76141050|76149020|76149040|76149050|87081030|87081060|87082921|94031000|94032000)\\d+$'],
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
                                      '9507302000', '9507304000', '9507306000', '9507308000', '9507906000', '9603908050'],
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

        {  # 对全部国家征收钢铝或衍生品  25%
            'fix_rate': '25%',
            'rules': [
                {
                    # 对全部国家征收铝-0312 铝制衍生品1
                    'code_matchers': [
                        {
                            'patterns': ['^(76101000|76109000)\\d+$'],
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
                                      '9507304000', '9507306000', '9507308000', '9507906000', '9603908050'],
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
            },
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
            'enabled': 0,
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
