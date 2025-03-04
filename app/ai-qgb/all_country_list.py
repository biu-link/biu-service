import json

from util.tools import get_json_file

all_country_list = [
    {
        "name": "常用",
        "country_list": [
            {
                "name": "中国"
            },
            {
                "name": "越南"
            },
            {
                "name": "马来西亚"
            },
            {
                "name": "泰国"
            },
            {
                "name": "印度"
            },
            {
                "name": "印度尼西亚"
            },
            {
                "name": "新加坡"
            },
            {
                "name": "菲律宾"
            },
            {
                "name": "日本"
            },
            {
                "name": "韩国"
            },
            {
                "name": "德国"
            },
            {
                "name": "法国"
            },
            {
                "name": "荷兰"
            },
            {
                "name": "意大利"
            },
            {
                "name": "英国"
            },
            {
                "name": "澳大利亚"
            },
            {
                "name": "新西兰"
            },
            {
                "name": "加拿大"
            },
            {
                "name": "墨西哥"
            },
            {
                "name": "巴西"
            },
            {
                "name": "南非"
            }
        ]
    },
    {
        "name": "亚洲",
        "country_list": [
            {
                "name": "阿富汗"
            },
            {
                "name": "阿联酋"
            },
            {
                "name": "阿曼"
            },
            {
                "name": "阿塞拜疆"
            },
            {
                "name": "巴基斯坦"
            },
            {
                "name": "巴勒斯坦"
            },
            {
                "name": "巴林"
            },
            {
                "name": "不丹"
            },
            {
                "name": "朝鲜"
            },
            {
                "name": "东帝汶"
            },
            {
                "name": "菲律宾"
            },
            {
                "name": "格鲁吉亚"
            },
            {
                "name": "哈萨克斯坦"
            },
            {
                "name": "韩国"
            },
            {
                "name": "吉尔吉斯斯坦"
            },
            {
                "name": "柬埔寨"
            },
            {
                "name": "卡塔尔"
            },
            {
                "name": "科威特"
            },
            {
                "name": "老挝"
            },
            {
                "name": "黎巴嫩"
            },
            {
                "name": "马尔代夫"
            },
            {
                "name": "马来西亚"
            },
            {
                "name": "蒙古"
            },
            {
                "name": "孟加拉国"
            },
            {
                "name": "缅甸"
            },
            {
                "name": "尼泊尔"
            },
            {
                "name": "日本"
            },
            {
                "name": "沙特阿拉伯"
            },
            {
                "name": "斯里兰卡"
            },
            {
                "name": "塔吉克斯坦"
            },
            {
                "name": "泰国"
            },
            {
                "name": "土耳其"
            },
            {
                "name": "土库曼斯坦"
            },
            {
                "name": "文莱"
            },
            {
                "name": "乌兹别克斯坦"
            },
            {
                "name": "新加坡"
            },
            {
                "name": "叙利亚"
            },
            {
                "name": "亚美尼亚"
            },
            {
                "name": "也门"
            },
            {
                "name": "伊拉克"
            },
            {
                "name": "伊朗"
            },
            {
                "name": "以色列"
            },
            {
                "name": "印度"
            },
            {
                "name": "印度尼西亚"
            },
            {
                "name": "约旦"
            },
            {
                "name": "越南"
            }
        ]
    },
    {
        "name": "非洲",
        "country_list": [
            {
                "name": "阿尔及利亚"
            },
            {
                "name": "埃及"
            },
            {
                "name": "埃塞俄比亚"
            },
            {
                "name": "安哥拉"
            },
            {
                "name": "贝宁"
            },
            {
                "name": "博茨瓦纳"
            },
            {
                "name": "布基纳法索"
            },
            {
                "name": "布隆迪"
            },
            {
                "name": "多哥"
            },
            {
                "name": "厄立特里亚"
            },
            {
                "name": "佛得角"
            },
            {
                "name": "冈比亚"
            },
            {
                "name": "刚果（布）"
            },
            {
                "name": "刚果（金）"
            },
            {
                "name": "吉布提"
            },
            {
                "name": "几内亚"
            },
            {
                "name": "几内亚比绍"
            },
            {
                "name": "加纳"
            },
            {
                "name": "加蓬"
            },
            {
                "name": "津巴布韦"
            },
            {
                "name": "喀麦隆"
            },
            {
                "name": "科摩罗"
            },
            {
                "name": "科特迪瓦"
            },
            {
                "name": "肯尼亚"
            },
            {
                "name": "莱索托"
            },
            {
                "name": "利比里亚"
            },
            {
                "name": "利比亚"
            },
            {
                "name": "卢旺达"
            },
            {
                "name": "马达加斯加"
            },
            {
                "name": "马拉维"
            },
            {
                "name": "马里"
            },
            {
                "name": "毛里求斯"
            },
            {
                "name": "毛里塔尼亚"
            },
            {
                "name": "摩洛哥"
            },
            {
                "name": "莫桑比克"
            },
            {
                "name": "纳米比亚"
            },
            {
                "name": "南非"
            },
            {
                "name": "南苏丹"
            },
            {
                "name": "尼日尔"
            },
            {
                "name": "尼日利亚"
            },
            {
                "name": "塞拉利昂"
            },
            {
                "name": "塞内加尔"
            },
            {
                "name": "塞舌尔"
            },
            {
                "name": "圣多美和普林西比"
            },
            {
                "name": "斯威士兰"
            },
            {
                "name": "苏丹"
            },
            {
                "name": "索马里"
            },
            {
                "name": "坦桑尼亚"
            },
            {
                "name": "突尼斯"
            },
            {
                "name": "乌干达"
            },
            {
                "name": "赞比亚"
            },
            {
                "name": "乍得"
            },
            {
                "name": "中非共和国"
            }
        ]
    },
    {
        "name": "欧洲",
        "country_list": [
            {
                "name": "阿尔巴尼亚"
            },
            {
                "name": "爱尔兰"
            },
            {
                "name": "爱沙尼亚"
            },
            {
                "name": "安道尔"
            },
            {
                "name": "奥地利"
            },
            {
                "name": "白俄罗斯"
            },
            {
                "name": "保加利亚"
            },
            {
                "name": "北马其顿"
            },
            {
                "name": "比利时"
            },
            {
                "name": "冰岛"
            },
            {
                "name": "波黑"
            },
            {
                "name": "波兰"
            },
            {
                "name": "丹麦"
            },
            {
                "name": "德国"
            },
            {
                "name": "俄罗斯联邦"
            },
            {
                "name": "法国"
            },
            {
                "name": "梵蒂冈"
            },
            {
                "name": "芬兰"
            },
            {
                "name": "荷兰"
            },
            {
                "name": "黑山"
            },
            {
                "name": "捷克"
            },
            {
                "name": "克罗地亚"
            },
            {
                "name": "拉脱维亚"
            },
            {
                "name": "立陶宛"
            },
            {
                "name": "列支敦士登"
            },
            {
                "name": "卢森堡"
            },
            {
                "name": "罗马尼亚"
            },
            {
                "name": "马耳他"
            },
            {
                "name": "摩尔多瓦"
            },
            {
                "name": "摩纳哥"
            },
            {
                "name": "挪威"
            },
            {
                "name": "葡萄牙"
            },
            {
                "name": "瑞典"
            },
            {
                "name": "瑞士"
            },
            {
                "name": "塞尔维亚"
            },
            {
                "name": "塞浦路斯"
            },
            {
                "name": "圣马力诺"
            },
            {
                "name": "斯洛伐克"
            },
            {
                "name": "斯洛文尼亚"
            },
            {
                "name": "乌克兰"
            },
            {
                "name": "西班牙"
            },
            {
                "name": "希腊"
            },
            {
                "name": "匈牙利"
            },
            {
                "name": "意大利"
            },
            {
                "name": "英国"
            }
        ]
    },
    {
        "name": "北美洲",
        "country_list": [
            {
                "name": "安提瓜和巴布达"
            },
            {
                "name": "巴巴多斯"
            },
            {
                "name": "巴哈马"
            },
            {
                "name": "巴拿马"
            },
            {
                "name": "伯利兹"
            },
            {
                "name": "多米尼加"
            },
            {
                "name": "多米尼克"
            },
            {
                "name": "格林纳达"
            },
            {
                "name": "哥斯达黎加"
            },
            {
                "name": "古巴"
            },
            {
                "name": "海地"
            },
            {
                "name": "洪都拉斯"
            },
            {
                "name": "加拿大"
            },
            {
                "name": "美国"
            },
            {
                "name": "墨西哥"
            },
            {
                "name": "尼加拉瓜"
            },
            {
                "name": "萨尔瓦多"
            },
            {
                "name": "圣基茨和尼维斯"
            },
            {
                "name": "圣卢西亚"
            },
            {
                "name": "圣文森特和格林纳丁斯"
            },
            {
                "name": "特立尼达和多巴哥"
            },
            {
                "name": "危地马拉"
            },
            {
                "name": "牙买加"
            }
        ]
    },
    {
        "name": "南美洲",
        "country_list": [
            {
                "name": "阿根廷"
            },
            {
                "name": "巴拉圭"
            },
            {
                "name": "巴西"
            },
            {
                "name": "秘鲁"
            },
            {
                "name": "玻利维亚"
            },
            {
                "name": "厄瓜多尔"
            },
            {
                "name": "哥伦比亚"
            },
            {
                "name": "圭亚那"
            },
            {
                "name": "苏里南"
            },
            {
                "name": "委内瑞拉"
            },
            {
                "name": "乌拉圭"
            },
            {
                "name": "智利"
            }
        ]
    },
    {
        "name": "大洋洲",
        "country_list": [
            {
                "name": "澳大利亚"
            },
            {
                "name": "巴布亚新几内亚"
            },
            {
                "name": "斐济"
            },
            {
                "name": "基里巴斯"
            },
            {
                "name": "库克群岛"
            },
            {
                "name": "马绍尔群岛"
            },
            {
                "name": "密克罗尼西亚联邦"
            },
            {
                "name": "瑙鲁"
            },
            {
                "name": "纽埃"
            },
            {
                "name": "帕劳"
            },
            {
                "name": "萨摩亚"
            },
            {
                "name": "所罗门群岛"
            },
            {
                "name": "汤加"
            },
            {
                "name": "图瓦卢"
            },
            {
                "name": "瓦努阿图"
            },
            {
                "name": "新西兰"
            }
        ]
    }
]

changyong = '''
常用
中国
越南
马来西亚
泰国
印度
印度尼西亚
新加坡
菲律宾
日本
韩国
德国
法国
荷兰
意大利
英国
澳大利亚
新西兰
加拿大
墨西哥
巴西
南非
'''

yazhou = '''
亚洲
阿富汗
阿联酋
阿曼
阿塞拜疆
巴基斯坦
巴勒斯坦
巴林
不丹
朝鲜
东帝汶
菲律宾
格鲁吉亚
哈萨克斯坦
韩国
吉尔吉斯斯坦
柬埔寨
卡塔尔
科威特
老挝
黎巴嫩
马尔代夫
马来西亚
蒙古
孟加拉国
缅甸
尼泊尔
日本
沙特阿拉伯
斯里兰卡
塔吉克斯坦
泰国
土耳其
土库曼斯坦
文莱
乌兹别克斯坦
新加坡
叙利亚
亚美尼亚
也门
伊拉克
伊朗
以色列
印度
印度尼西亚
约旦
越南
'''

feizhou = '''
非洲
阿尔及利亚
埃及
埃塞俄比亚
安哥拉
贝宁
博茨瓦纳
布基纳法索
布隆迪
多哥
厄立特里亚
佛得角
冈比亚
刚果（布）
刚果（金）
吉布提
几内亚
几内亚比绍
加纳
加蓬
津巴布韦
喀麦隆
科摩罗
科特迪瓦
肯尼亚
莱索托
利比里亚
利比亚
卢旺达
马达加斯加
马拉维
马里
毛里求斯
毛里塔尼亚
摩洛哥
莫桑比克
纳米比亚
南非
南苏丹
尼日尔
尼日利亚
塞拉利昂
塞内加尔
塞舌尔
圣多美和普林西比
斯威士兰
苏丹
索马里
坦桑尼亚
突尼斯
乌干达
赞比亚
乍得
中非共和国
'''

ouzhou = '''
欧洲
阿尔巴尼亚
爱尔兰
爱沙尼亚
安道尔
奥地利
白俄罗斯
保加利亚
北马其顿
比利时
冰岛
波黑
波兰
丹麦
德国
俄罗斯联邦
法国
梵蒂冈
芬兰
荷兰
黑山
捷克
克罗地亚
拉脱维亚
立陶宛
列支敦士登
卢森堡
罗马尼亚
马耳他
摩尔多瓦
摩纳哥
挪威
葡萄牙
瑞典
瑞士
塞尔维亚
塞浦路斯
圣马力诺
斯洛伐克
斯洛文尼亚
乌克兰
西班牙
希腊
匈牙利
意大利
英国
'''

beimei = '''
北美洲
安提瓜和巴布达
巴巴多斯
巴哈马
巴拿马
伯利兹
多米尼加
多米尼克
格林纳达
哥斯达黎加
古巴
海地
洪都拉斯
加拿大
美国
墨西哥
尼加拉瓜
萨尔瓦多
圣基茨和尼维斯
圣卢西亚
圣文森特和格林纳丁斯
特立尼达和多巴哥
危地马拉
牙买加

'''

nanmei = '''
南美洲
阿根廷
巴拉圭
巴西
秘鲁
玻利维亚
厄瓜多尔
哥伦比亚
圭亚那
苏里南
委内瑞拉
乌拉圭
智利

'''

dayang = '''
大洋洲
澳大利亚
巴布亚新几内亚
斐济
基里巴斯
库克群岛
马绍尔群岛
密克罗尼西亚联邦
瑙鲁
纽埃
帕劳
萨摩亚
所罗门群岛
汤加
图瓦卢
瓦努阿图
新西兰

'''


def parse_country():
    content_list = [
        changyong, yazhou, feizhou, ouzhou, beimei, nanmei, dayang
    ]

    country_list = []

    for content in content_list:
        names = content.split('\n')

        parent = None

        for i in range(len(names)):
            name = names[i].strip()
            if not name:
                continue

            if parent is None:
                parent = {
                    'name': name,
                    'country_list': []
                }
                country_list.append(parent)
                continue

            parent['country_list'].append({'name': name})

    print(json.dumps(country_list, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    parse_country()

    export_country = get_json_file('export_country.json')

    for item in all_country_list:
        for country in item['country_list']:
            name = country['name']

            match_country = list(filter(lambda x: x['name'] == name, export_country['items']))
            if (len(match_country) == 0):
                print(name)
