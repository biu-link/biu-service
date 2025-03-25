import pandas as pd
import json


def read_excel_file(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path, header=0)

    # 获取行数和列数
    num_rows, num_cols = df.shape

    print(f"Excel文件共有 {num_rows} 行和 {num_cols} 列。\n")

    rows = []
    for index, row in df.iterrows():
        rows.append(list(row))

    return rows


def main():
    file_path = r'D:\doc\工作记录\技术文档\清关查询\AMS回执编码.xlsx'  # 替换为你的Excel文件路径
    rows = read_excel_file(file_path)

    setting = {}

    for row in rows:
        setting[str(row[0])] = {
            'code': str(row[0]),
            'type': row[1],
            'short_desc': row[2],
            'detail_cn': row[5]
        }

    print(json.dumps(setting, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    main()
