import requests

for i in range(1, 2000):
    print(f'{i} -- start')
    session = requests.session()
    response = session.get(f'http://localhost:9205/activity/async/test?id={i}')
    # print(response.content)
    session.close()
    print(f'{i} -- end')
