# 税率类型分组

import re

file = open('rate_list.txt', 'r', encoding='utf-8')
result = file.read()
# print(content)

lines = result.splitlines()

arr = []

for line in lines:
    line = re.sub(r'\d+\.\d+', '9.9', line)
    line = re.sub(r' \d+%', ' 9.9%', line)
    line = re.sub(r' \d+¢', ' 9.9¢', line)
    line = re.sub(r'^\d+%', '9.9%', line, )
    line = re.sub(r'^\d+¢', '9.9¢', line, )
    print(line)
    arr.append(line)

# unique_lines = list(set(arr))
# for line in unique_lines:
#     print(line)


