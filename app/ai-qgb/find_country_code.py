from util.tools import get_json_file

content1 = """
99038001	奥地利
99038001	比利时
99038001	保加利亚
99038001	克罗地亚
99038001	塞浦路斯
99038001	捷克
99038001	丹麦
99038001	爱沙尼亚
99038001	芬兰
99038001	法国
99038001	德国
99038001	希腊
99038001	匈牙利
99038001	爱尔兰
99038001	意大利
99038001	拉脱维亚
99038001	立陶宛
99038001	卢森堡
99038001	马耳他
99038001	荷兰
99038001	波兰
99038001	葡萄牙
99038001	罗马尼亚
99038001	斯洛伐克
99038001	斯洛文尼亚
99038001	西班牙
99038001	瑞典
99038001	澳大利亚
99038001	阿根廷
99038001	巴西
99038001	加拿大
99038001	墨西哥
99038001	韩国
99038001	日本
99038001	英国
99038001	乌克兰
"""

content2 = """
99038501	阿根廷
99038501	澳大利亚
99038501	加拿大
99038501	墨西哥
99038501	奥地利
99038501	比利时
99038501	保加利亚
99038501	克罗地亚
99038501	塞浦路斯
99038501	捷克
99038501	丹麦
99038501	爱沙尼亚
99038501	芬兰
99038501	法国
99038501	德国
99038501	希腊
99038501	匈牙利
99038501	爱尔兰
99038501	意大利
99038501	拉脱维亚
99038501	立陶宛
99038501	卢森堡
99038501	马耳他
99038501	荷兰
99038501	波兰
99038501	葡萄牙
99038501	罗马尼亚
99038501	斯洛伐克
99038501	斯洛文尼亚
99038501	西班牙
99038501	瑞典
"""

country_list = get_json_file('export_country.json')['items']


def start(content):
    arr = content.split('\n')
    country_codes = []

    for line in arr:
        if not line:
            continue

        cols = line.split()
        special_code = cols[0]
        country_name = cols[1]
        country_code = ''

        for country in country_list:
            if country['name'] == country_name:
                country_code = country['code']
                country_codes.append(country_code)
                break

        print(special_code, country_name, country_code)

    print(country_codes)


start(content2)
