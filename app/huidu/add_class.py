from util.tools import get_json_file

school_list = get_json_file('school_list.json')
print(school_list)

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


def get_school_id(school_name):
    for school in school_list:
        if school['dept_name'] == school_name:
            return school['dept_id']


def main():
    f = open('class_list.txt', 'r', encoding='utf-8')
    lines = f.readlines()

    for line in lines:
        # print(line)

        cols = line.split()
        school_name = cols[0]
        school_id = get_school_id(school_name)

        grade = cols[1]
        num = cols[2]

        grade_class_string = f'{grade}年级（{num}）班'

        print(school_name, school_id, grade_class_string)
        add_class(school_id, grade_class_string)


def add_class(school_id, class_name):
    json_data = {
        'className': class_name,
        'deptId': school_id,
    }

    response = requests.post('https://www.heingedu.cn/prod-api/ai/class/add', cookies=cookies, headers=headers, json=json_data)


main()
