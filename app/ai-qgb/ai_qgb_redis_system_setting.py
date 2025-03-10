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
        {  # 铝制品加征1
            'fix_rate': '25%',
            'exclude_country_list': ['AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL',
                                     'PL',
                                     'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'AU', 'AR', 'BR', 'CA', 'MX', 'KR', 'JP', 'GB', 'UA'],
            'include_hs_code': ['7206100000', '7206900000', '7207110000', '7207120010', '7207120050', '7207190030', '7207190090', '7207200025', '7207200045',
                                '7207200075', '7207200090', '7208101500', '7208103000', '7208106000', '7208253000', '7208256000', '7208260030', '7208260060',
                                '7208270030', '7208270040', '7208270045', '7208270060', '7208360030', '7208360060', '7208370030', '7208370060', '7208380015',
                                '7208380030', '7208380090', '7208390015', '7208390020', '7208390025', '7208390030', '7208390090', '7208403030', '7208403060',
                                '7208406030', '7208406060', '7208510030', '7208510045', '7208510060', '7208520000', '7208530000', '7208540000', '7208900000',
                                '7209150000', '7209160030', '7209160040', '7209160045', '7209160060', '7209160070', '7209160091', '7209170030', '7209170040',
                                '7209170045', '7209170060', '7209170070', '7209170091', '7209181530', '7209181560', '7209182510', '7209182520', '7209182580',
                                '7209182585', '7209186020', '7209186090', '7209250000', '7209260000', '7209270000', '7209280000', '7209900000', '7210110000',
                                '7210120000', '7210200000', '7210300030', '7210300060', '7210410000', '7210490030', '7210490040', '7210490045', '7210490091',
                                '7210490095', '7210500000', '7210500020', '7210500090', '7210610000', '7210690000', '7210703000', '7210706030', '7210706060',
                                '7210706090', '7210901000', '7210906000', '7210909000', '7211130000', '7211140030', '7211140045', '7211140090', '7211191500',
                                '7211192000', '7211193000', '7211194500', '7211196000', '7211197530', '7211197560', '7211197590', '7211231500', '7211232000',
                                '7211233000', '7211234500', '7211236030', '7211236060', '7211236085', '7211236090', '7211292030', '7211292090', '7211294500',
                                '7211296030', '7211296080', '7211900000', '7212100000', '7212200000', '7212301030', '7212301090', '7212303000', '7212305000',
                                '7212401000', '7212405000', '7212500000', '7212600000', '7213100000', '7213200010', '7213200080', '7213913011', '7213913015',
                                '7213913020', '7213913092', '7213913093', '7213914500', '7213916000', '7213990030', '7213990060', '7213990090', '7214100000',
                                '7214200000', '7214300010', '7214300080', '7214910015', '7214910016', '7214910020', '7214910060', '7214910090', '7214990015',
                                '7214990016', '7214990020', '7214990021', '7214990026', '7214990030', '7214990031', '7214990036', '7214990040', '7214990045',
                                '7214990060', '7214990075', '7214990090', '7215100010', '7215100080', '7215500015', '7215500016', '7215500018', '7215500020',
                                '7215500060', '7215500061', '7215500063', '7215500065', '7215500090', '7215901000', '7215903000', '7215905000', '7216100010',
                                '7216100050', '7216210000', '7216220000', '7216310000', '7216320000', '7216330030', '7216330060', '7216330090', '7216400010',
                                '7216400050', '7216500000', '7216990010', '7216990090', '7217101000', '7217102000', '7217103000', '7217104030', '7217104040',
                                '7217104045', '7217104090', '7217105030', '7217105090', '7217106000', '7217107000', '7217108010', '7217108020', '7217108025',
                                '7217108030', '7217108045', '7217108060', '7217108075', '7217108090', '7217109000', '7217201500', '7217203000', '7217204510',
                                '7217204520', '7217204530', '7217204540', '7217204550', '7217204560', '7217204570', '7217204580', '7217206000', '7217207500',
                                '7217301530', '7217301560', '7217303000', '7217304504', '7217304511', '7217304520', '7217304530', '7217304541', '7217304550',
                                '7217304560', '7217304590', '7217306000', '7217307500', '7217901000', '7217905030', '7217905060', '7217905090', '7218100000',
                                '7218910015', '7218910030', '7218910060', '7218990015', '7218990030', '7218990045', '7218990060', '7218990090', '7219110030',
                                '7219110060', '7219120002', '7219120006', '7219120021', '7219120026', '7219120051', '7219120056', '7219120066', '7219120071',
                                '7219120081', '7219130002', '7219130031', '7219130051', '7219130071', '7219130081', '7219140030', '7219140065', '7219140090',
                                '7219210005', '7219210020', '7219210040', '7219210060', '7219220005', '7219220015', '7219220020', '7219220025', '7219220035',
                                '7219220040', '7219220045', '7219220070', '7219220075', '7219220080', '7219230030', '7219230060', '7219240030', '7219240060',
                                '7219310010', '7219310050', '7219320005', '7219320020', '7219320025', '7219320035', '7219320036', '7219320038', '7219320042',
                                '7219320044', '7219320045', '7219320060', '7219330005', '7219330020', '7219330025', '7219330035', '7219330036', '7219330038',
                                '7219330042', '7219330044', '7219330045', '7219330070', '7219330080', '7219340005', '7219340020', '7219340025', '7219340030',
                                '7219340035', '7219340050', '7219350005', '7219350015', '7219350030', '7219350035', '7219350050', '7219900010', '7219900020',
                                '7219900025', '7219900060', '7219900080', '7220110000', '7220121000', '7220125000', '7220201010', '7220201015', '7220201060',
                                '7220201080', '7220206005', '7220206010', '7220206015', '7220206060', '7220206080', '7220207005', '7220207010', '7220207015',
                                '7220207060', '7220207080', '7220208000', '7220209030', '7220209060', '7220900010', '7220900015', '7220900060', '7220900080',
                                '7221000005', '7221000015', '7221000017', '7221000018', '7221000030', '7221000045', '7221000075', '7222110001', '7222110005',
                                '7222110006', '7222110050', '7222110055', '7222110056', '7222110057', '7222110059', '7222110080', '7222110081', '7222110082',
                                '7222110084', '7222190001', '7222190005', '7222190006', '7222190050', '7222190051', '7222190052', '7222190054', '7222200001',
                                '7222200005', '7222200006', '7222200041', '7222200043', '7222200045', '7222200046', '7222200047', '7222200049', '7222200062',
                                '7222200064', '7222200067', '7222200069', '7222200071', '7222200073', '7222200075', '7222200080', '7222200081', '7222200082',
                                '7222200084', '7222200085', '7222200086', '7222200087', '7222200089', '7222300000', '7222300001', '7222300010', '7222300011',
                                '7222300012', '7222300022', '7222300024', '7222300080', '7222300081', '7222300082', '7222300084', '7222403025', '7222403045',
                                '7222403065', '7222403085', '7222406000', '7223001005', '7223001015', '7223001016', '7223001030', '7223001031', '7223001045',
                                '7223001046', '7223001060', '7223001061', '7223001075', '7223001076', '7223005000', '7223009000', '7224100005', '7224100045',
                                '7224100075', '7224900005', '7224900015', '7224900025', '7224900035', '7224900045', '7224900055', '7224900065', '7224900075',
                                '7225110000', '7225190000', '7225301110', '7225301180', '7225303005', '7225303050', '7225305110', '7225305130', '7225305160',
                                '7225305180', '7225307000', '7225401110', '7225401180', '7225401190', '7225403005', '7225403050', '7225405110', '7225405130',
                                '7225405160', '7225407000', '7225501110', '7225501130', '7225501160', '7225506000', '7225507000', '7225508010', '7225508080',
                                '7225508085', '7225910000', '7225920000', '7225990010', '7225990090', '7226111000', '7226119030', '7226119060', '7226191000',
                                '7226199000', '7226200000', '7226910500', '7226911530', '7226911560', '7226912530', '7226912560', '7226915000', '7226917000',
                                '7226918000', '7226921030', '7226921060', '7226923030', '7226923060', '7226925000', '7226927005', '7226927050', '7226928005',
                                '7226928050', '7226990110', '7226990130', '7226990180', '7227100000', '7227200000', '7227200030', '7227200080', '7227901030',
                                '7227901060', '7227902030', '7227902060', '7227906005', '7227906010', '7227906020', '7227906030', '7227906035', '7227906040',
                                '7227906080', '7227906085', '7227906090', '7228100010', '7228100030', '7228100060', '7228201000', '7228205000', '7228302000',
                                '7228304000', '7228306000', '7228308005', '7228308010', '7228308015', '7228308040', '7228308041', '7228308045', '7228308050',
                                '7228308060', '7228308070', '7228400000', '7228501010', '7228501020', '7228501040', '7228501060', '7228501080', '7228505005',
                                '7228505015', '7228505040', '7228505050', '7228505070', '7228601030', '7228601060', '7228606000', '7228608000', '7228703010',
                                '7228703020', '7228703041', '7228703060', '7228703081', '7228706000', '7228800000', '7229200010', '7229200015', '7229200090',
                                '7229900500', '7229901000', '7229905006', '7229905008', '7229905016', '7229905031', '7229905051', '7229909000', '7301100000',
                                '7302101010', '7302101015', '7302101025', '7302101035', '7302101045', '7302101055', '7302101065', '7302101075', '7302105020',
                                '7302105040', '7302105060', '7302400000', '7302901000', '7302909000', '7304110020', '7304110050', '7304110080', '7304191020',
                                '7304191030', '7304191045', '7304191060', '7304191080', '7304195020', '7304195050', '7304195080', '7304220030', '7304220045',
                                '7304220060', '7304233000', '7304236030', '7304236045', '7304236060', '7304243010', '7304243020', '7304243030', '7304243040',
                                '7304243045', '7304243050', '7304243060', '7304243080', '7304244010', '7304244020', '7304244030', '7304244040', '7304244050',
                                '7304244060', '7304244080', '7304246015', '7304246030', '7304246045', '7304246060', '7304246075', '7304291010', '7304291020',
                                '7304291030', '7304291040', '7304291050', '7304291060', '7304291080', '7304292010', '7304292020', '7304292030', '7304292040',
                                '7304292050', '7304292060', '7304292080', '7304293110', '7304293120', '7304293130', '7304293140', '7304293150', '7304293160',
                                '7304293180', '7304294110', '7304294120', '7304294130', '7304294140', '7304294150', '7304294160', '7304294180', '7304295015',
                                '7304295030', '7304295045', '7304295060', '7304295075', '7304296115', '7304296130', '7304296145', '7304296160', '7304296175',
                                '7304313000', '7304316010', '7304316050', '7304390002', '7304390004', '7304390006', '7304390008', '7304390016', '7304390020',
                                '7304390024', '7304390028', '7304390032', '7304390036', '7304390040', '7304390044', '7304390048', '7304390052', '7304390056',
                                '7304390062', '7304390068', '7304390072', '7304390076', '7304390080', '7304413005', '7304413015', '7304413045', '7304416005',
                                '7304416015', '7304416045', '7304490005', '7304490015', '7304490045', '7304490060', '7304511000', '7304515005', '7304515015',
                                '7304515045', '7304515060', '7304591000', '7304592030', '7304592040', '7304592045', '7304592055', '7304592060', '7304592070',
                                '7304592080', '7304596000', '7304598010', '7304598015', '7304598020', '7304598025', '7304598030', '7304598035', '7304598040',
                                '7304598045', '7304598050', '7304598055', '7304598060', '7304598065', '7304598070', '7304598080', '7304901000', '7304903000',
                                '7304905000', '7304907000', '7305111030', '7305111060', '7305115000', '7305121030', '7305121060', '7305125000', '7305191030',
                                '7305191060', '7305195000', '7305202000', '7305204000', '7305206000', '7305208000', '7305312000', '7305314000', '7305316000',
                                '7305316010', '7305316090', '7305391000', '7305395000', '7305901000', '7305905000', '7306110010', '7306110050', '7306191010',
                                '7306191050', '7306195110', '7306195150', '7306213000', '7306214000', '7306218010', '7306218050', '7306291030', '7306291090',
                                '7306292000', '7306293100', '7306294100', '7306296010', '7306296050', '7306298110', '7306298150', '7306301000', '7306303000',
                                '7306305010', '7306305015', '7306305020', '7306305025', '7306305028', '7306305032', '7306305035', '7306305040', '7306305055',
                                '7306305085', '7306305090', '7306401010', '7306401015', '7306401090', '7306405005', '7306405015', '7306405040', '7306405042',
                                '7306405044', '7306405062', '7306405064', '7306405080', '7306405085', '7306405090', '7306501000', '7306503000', '7306505010',
                                '7306505030', '7306505050', '7306505070', '7306611000', '7306613000', '7306615000', '7306617030', '7306617060', '7306691000',
                                '7306693000', '7306695000', '7306697030', '7306697060', '7306901000', '7306905000'],
            'special_code': '99038001',
            'describe_list': [
                {
                    'specialDescribeCn': '除了在9903.80.03项下描述的衍生铁或钢产品外，根据本章附注16中列出的关税项或子项所规定的铁或钢产品，除澳大利亚、阿根廷、巴西、加拿大、墨西哥（如U.S.附注16的(h)(i)条款所述）、韩国、欧洲联盟成员国（如U.S.附注16(f)条款所述）、日本、英国或乌克兰的产品，按U.S.附注16的相关条款进入，或者根据商务部根据U.S.附注16所建立的任何规定，或商务部宣布的任何豁免进入的产品。',
                    'specialDescribeEn': 'Except for derivative iron or steel products described in heading 9903.80.03, products of iron or steel provided for in the tariff headings or subheadings enumerated in note 16 to this subchapter, except products of Australia, of Argentina, of Brazil, of Canada, of Mexico (as specified in subdivision (h)(i) of such U.S. note 16), of South Korea, of member countries of the European Union specified in subdivision (f) of such U.S. note 16 or of Japan, or of the United Kingdom, or of Ukraine entered under the terms of such U.S. note 16, under any provisions that may be established by the Department of Commerce under such U.S. note 16, or any exclusions that may be determined and announced by the Department of Commerce',
                    'effectiveDate': '20220101'
                },
            ],
        },
        {  # 铝制品加征2
            'fix_rate': '10%',
            'exclude_country_list': ['AR', 'AU', 'CA', 'MX', 'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV',
                                     'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE'],
            'include_hs_code': ['7601103000', '7601106000', '7601106030', '7601106090', '7601203000', '7601206000', '7601209030', '7601209045', '7601209060',
                                '7601209075', '7601209080', '7601209085', '7601209090', '7601209095', '7604101000', '7604103000', '7604103010', '7604103050',
                                '7604105000', '7604105030', '7604105060', '7604210000', '7604210010', '7604210090', '7604291000', '7604291010', '7604291090',
                                '7604293010', '7604293030', '7604293050', '7604293060', '7604293090', '7604295020', '7604295030', '7604295050', '7604295060',
                                '7604295090', '7605110000', '7605110030', '7605110090', '7605190000', '7605210000', '7605210030', '7605210090', '7605290000',
                                '7606113030', '7606113060', '7606116000', '7606123015', '7606123025', '7606123030', '7606123035', '7606123045', '7606123055',
                                '7606123090', '7606123091', '7606123096', '7606126000', '7606913030', '7606913055', '7606913060', '7606913075', '7606913090',
                                '7606913095', '7606916020', '7606916040', '7606916055', '7606916060', '7606916080', '7606916095', '7606923025', '7606923030',
                                '7606923035', '7606923060', '7606923075', '7606923090', '7606926020', '7606926040', '7606926055', '7606926060', '7606926080',
                                '7606926095', '7607113000', '7607116000', '7607116010', '7607116090', '7607119030', '7607119060', '7607119090', '7607191000',
                                '7607193000', '7607196000', '7607201000', '7607205000', '7608100030', '7608100090', '7608200030', '7608200090', '7609000000',
                                '7616995060', '7616995070', '7616995160', '7616995170'],
            'special_code': '99038501',
            'describe_list': [
                {
                    'specialDescribeCn': '除了在9903.85.03或9903.85.21、9903.85.25、9903.85.27至9903.85.44和9903.85.50至9903.85.66小项中描述的产品，按照本章注释19所列的铝制品，除阿根廷、澳大利亚、加拿大、墨西哥（除非在该美国注释19第(a)(viii)项中有所规定）、欧盟成员国（按该美国注释19第(a)(v)项所列的成员国）之外的产品，且可能会由商务部根据该美国注释19所设定的任何限制；或任何商务部可能确定并公布的排除项。',
                    'specialDescribeEn': 'Except for products described in heading 9903.85.03 or heading 9903.85.21, 9903.85.25, subheadings 9903.85.27 through 9903.85.44 and subheadings 9903.85.50 through 9903.85.66, products of aluminum provided for in the tariff headings or subheadings enumerated in note 19 to this subchapter, except products of Argentina, of Australia, of Canada, of Mexico (except as specified in subdivision (a)(viii) of such U.S. note 19), of member countries of the European Union specified in subdivision (a)(v) of such U.S. note 19, under any limitations that may be established by the Department of Commerce under such U.S. note 19; or any exclusions that may be determined and announced by the Department of Commerce',
                    'effectiveDate': '20220101'
                },
            ],
        },
        {  # 墨西哥 加征 25%
            'fix_rate': '25%',
            'include_country_list': ['MX'],
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
