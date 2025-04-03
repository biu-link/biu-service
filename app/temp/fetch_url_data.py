import requests
import json
import csv

from util.times import Times


def fetch_data():
    rows = []

    f = open('fetch_data.txt', 'w', encoding='utf-8')

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6',
        'Connection': 'keep-alive',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Origin': 'https://gs.amac.org.cn',
        'Referer': 'https://gs.amac.org.cn/amac-infodisc/res/pof/manager/managerList.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {}

    for page in range(0, 1):  # 201
        print(page)

        response = requests.post(
            f'https://gs.amac.org.cn/amac-infodisc/api/pof/manager/query?&page={page}&size=100',
            headers=headers,
            json=json_data,
            proxies={"no_proxy": "*"}
        )

        content = json.loads(response.content.decode())
        f.write(json.dumps(content['content'], indent=2)[1:-1] + ',')

    # print(rows)
    # print(len(rows))
    f.close()


def format_data():
    f = open('fetch_data2.txt', 'r', encoding='utf-8')
    content = f.read()
    f.close()

    rows = json.loads(content)
    fieldnames = rows[0].keys()

    for row in rows:
        row['id'] = "'" + row['id']
        row['establishDate'] = Times.datetime_to_string(Times.timestamp_to_datetime(row['establishDate']/1000))[0:10]
        row['registerDate'] = Times.datetime_to_string(Times.timestamp_to_datetime(row['registerDate']/1000))[0:10]
        # print(row['establishDate'])
        # return

    with open('fetch_data.csv', mode='w', newline='', encoding='utf-8') as f2:
        writer = csv.DictWriter(f2, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        # 写入表头
        writer.writeheader()

        # 写入数据行
        writer.writerows(rows)


# fetch_data()

format_data()
