#

import os

folder = r'D:\project\huidu\source20241125\ruoyi-web\dist\static\js'
# for root, dirs, files in os.walk(folder):
#     for filename in files:
#         if filename.endswith('.js') and len(filename) == 26:
#             print(root)
#             print(filename)
#             to_filename = f'{filename[0:14]}.js'
#             print(to_filename)
#             src = f'{root}\\{filename}'
#             dest = f'{root}\\{to_filename}'
#             os.rename(src, dest)


# chunk-f85496d4.8b36d81f.js

file_info = {}

folder = r'D:\project\huidu\版本比较\ruoyi-web-server\static\js'
for root, dirs, files in os.walk(folder):
    for filename in files:
        if filename.endswith('.js') and len(filename) == 26:
            full_path = f'{root}\\{filename}'
            file_time = os.path.getmtime(full_path)

            to_filename = f'{filename[0:14]}.js'
            file_key = f'{root}\\{to_filename}'

            exist_time = file_info.get(file_key)
            if exist_time is None:
                file_info[file_key] = file_time
            else:
                if file_time > exist_time:
                    file_info[file_key] = file_time

print(file_info)

for root, dirs, files in os.walk(folder):
    for filename in files:
        if filename.endswith('.js') and len(filename) == 26:
            full_path = f'{root}\\{filename}'
            file_time = os.path.getmtime(full_path)

            to_filename = f'{filename[0:14]}.js'
            file_key = f'{root}\\{to_filename}'

            exist_time = file_info.get(file_key)
            if file_time < exist_time:
                print(f'remove:{full_path}')
                os.remove(full_path)
