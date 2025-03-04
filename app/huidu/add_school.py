import requests

cookies = {
    'username': 'admin',
    'rememberMe': 'true',
    'password': 'k9q0HzXtkio5t/Jsc2T3KjNQWnU1SCP8J0U3DeSWXiZceOnBvD/GZKVe9bxngfADAArwJbrFEC39aeWKZPodkg==',
    'Admin-Token': 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX2tleSI6IjlmNDg5NGJhLTQxNzUtNDgzYS05NjkwLTU0Mzg5MWU3ZThmMSIsInVzZXJuYW1lIjoiYWRtaW4ifQ.fO53l8cEH_4LkP_Kz-7zfVtxPs076Pf5sTd4jNDmEqsyYGEW0OJbMA5ylPDqjdM_ng7ESV2SjAzkhZe3tnUEuQ',
    'Admin-Expires-In': '720',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6',
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX2tleSI6IjlmNDg5NGJhLTQxNzUtNDgzYS05NjkwLTU0Mzg5MWU3ZThmMSIsInVzZXJuYW1lIjoiYWRtaW4ifQ.fO53l8cEH_4LkP_Kz-7zfVtxPs076Pf5sTd4jNDmEqsyYGEW0OJbMA5ylPDqjdM_ng7ESV2SjAzkhZe3tnUEuQ',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'username=admin; rememberMe=true; password=k9q0HzXtkio5t/Jsc2T3KjNQWnU1SCP8J0U3DeSWXiZceOnBvD/GZKVe9bxngfADAArwJbrFEC39aeWKZPodkg==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX2tleSI6IjlmNDg5NGJhLTQxNzUtNDgzYS05NjkwLTU0Mzg5MWU3ZThmMSIsInVzZXJuYW1lIjoiYWRtaW4ifQ.fO53l8cEH_4LkP_Kz-7zfVtxPs076Pf5sTd4jNDmEqsyYGEW0OJbMA5ylPDqjdM_ng7ESV2SjAzkhZe3tnUEuQ; Admin-Expires-In=720',
    'Origin': 'https://www.heingedu.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.heingedu.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

school_names = """
*宏鸣可小学
*花港迎春
*花港迎春明泉校区
*黄家溪小学
*江村实验
*江陵吉市路齐心
*江陵实小三淞路
*江陵实小淞南路
*江陵实小绣湖东路
*金家坝学校
*黎里小学
*黎里小学梨花校区
*芦墟实小
*鲈实小流虹
*鲈实小越秀
*鲈实小仲英
*梅堰实小
*梅堰实小南校区
*南麻小学
*南麻小学引庆校区
*平望实小
*平望实小北校区
*七都小学
*七都小学吴越校区
*青云学校
*青云学校蒲公英
*区实小爱德
*区实小城中
*区实小太湖
*莘塔小学
*莘塔小学芦北校区
*盛泽实小
*盛泽实小清溪校区
*盛泽小学
*盛泽小学目澜校区
*盛泽小学群铁校区
*盛泽小学兴桥校区
*世恒学校
*水秀实小
*思贤实小
*松陵小学
*苏大附属校
*苏州枫华
*苏州湾实小
*苏州湾外国语学校
*太湖国际
*坛丘小学
*坛丘小学润洋校区
*桃源小学
*天和小学
*同里实小
*铜罗小学
*屯村实小
*菀坪学校
*吴绫实小
*吴绫实小圣塘校区
*新城实小
*新胜实验
*杨嘉墀实小
*云龙实验
*泽新实验
*长安实小
*震泽实小
*震泽实小北校区
"""

for school in school_names.split():
    print(school)

    json_data = {
        'parentId': 401,
        'deptName': school,
        'orderNum': 1,
        'status': '0',
    }
    response = requests.post('https://www.heingedu.cn/prod-api/system/dept', cookies=cookies, headers=headers, json=json_data)
