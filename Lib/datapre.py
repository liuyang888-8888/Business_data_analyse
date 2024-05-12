# -*- coding: utf-8 -*-
#  道阻且长，行则将至
# -----Sunnyln---
#  5/9/2024  4:24 PM
import os
import glob
import pandas as pd
from datetime import datetime, timedelta
# import tqdm

from joblib import Parallel, delayed
from tqdm import tqdm


def code_llama():
    # 定义一个空的DataFrame
    df = pd.DataFrame()

    # 遍历behavior文件夹中的所有txt文件
    for file in glob.glob("C:\\Users\\nxxia\Desktop\商业数据分析\datas\data\\behavior"):
        # 读取每个txt文件的内容
        with open(file, "r") as f:
            content = f.read()

        # 从文件名中提取样本ID和日期
        filename = os.path.basename(file)
        sample_id = filename.split("_")[0]
        date = filename.split("_")[1].split(".")[0]

        # 将每行的字段值对转换为字典
        data = []
        for line in content.split("\n"):
            fields = line.split("[=]")
            row = {}
            for field in fields:
                key, value = field.split("<=>")
                row[key] = value
            data.append(row)

        # 将数据转换为DataFrame并添加样本ID和日期
        df_file = pd.DataFrame(data)
        df_file["SampleID"] = sample_id
        df_file["Date"] = date

        # 将DataFrame与之前的数据合并
        df = df.append(df_file, ignore_index=True)

    # 将合并后的数据保存到CSV文件中
    df.to_csv("behavior_merged.csv", index=False)
    print("Data merged and saved to behavior_merged.csv")
# behavior_df = pd.DataFrame(
#         columns=['Sample_ID', 'Timestamp', 'Process', 'PID', 'URL', 'Address_Handle', 'Tab_Handle', 'Version',
#                  'Window_Handle', 'Program_Name', 'Company'])
def process_txt(file_path,current,total):
    file_name=os.path.basename(file_path)
    sample_id = file_name.split('_')[0]
    new_df=pd.DataFrame(
        columns=['Sample_ID', 'Timestamp', 'Process', 'PID', 'URL', 'Address_Handle', 'Tab_Handle', 'Version',
                 'Window_Handle', 'Program_Name', 'Company'])
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        # 解析Last和L_Start
        last_update = int(lines[0].split('<=>')[1].strip())
        start_time_str = lines[1].split('<=>')[1].strip()
        start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H-%M-%S')

        # 遍历其余行并解析行为数据
        for line in lines[2:]:
            if line.strip():  # 跳过空行
                row_data = {
                    'Sample_ID': sample_id,
                    'Timestamp': None,  # 格式化时间戳为字符串
                    'Process': None,
                    'PID': None,
                    'URL': None,
                    'Address_Handle': None,
                    'Tab_Handle': None,
                    'Version': None,
                    'Window_Handle': None,
                    'Program_Name': None,
                    'Company': None,
                }
                fields = line.strip().split('[=]')
                if fields[0].split('<=>')[0] != 'T':
                    continue
                for field in fields:
                    try:
                        key, value = field.split('<=>')
                    except Exception as e:
                        print('Error in file:', file_path)
                        print('Error line:', line)

                        raise ValueError('Error in file:', file_path)

                    # 根据不同的key值将数据添加到DataFrame中
                    if key == 'T':
                        timestamp = start_time + timedelta(seconds=int(value))  # 计算时间戳
                        row_data['Timestamp'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                    elif key == 'P':
                        row_data['Process'] = value
                    elif key == 'I':
                        row_data['PID'] = value
                    elif key == 'U':
                        row_data['URL'] = value
                    elif key == 'A':
                        row_data['Address_Handle'] = value
                    elif key == 'B':
                        row_data['Tab_Handle'] = value
                    elif key == 'V':
                        row_data['Version'] = value
                    elif key == 'W':
                        row_data['Window_Handle'] = value
                    elif key == 'N':
                        row_data['Program_Name'] = value
                    elif key == 'C':
                        row_data['Company'] = value

            new_df = new_df.append(row_data, ignore_index=True)
    print(f'Processed file {current} of {total}: {file_path}')
    return new_df



def Baiduwenxin():
    import os
    import pandas as pd

    count= 0

    # 读取demographic.csv文件
    demographic_df = pd.read_csv('C:\\Users\\nxxia\Desktop\商业数据分析\datas\data\\behavior')

    # 初始化一个空的DataFrame来存储合并后的行为数据

    file_list = []
    # 遍历behavior文件夹中的所有日志文件
    for root, dirs, files in os.walk('data/behavior'):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                file_list.append(file_path)
    total=len(file_list)
    all = Parallel(n_jobs=-1, verbose=10)(
        delayed(process_txt)(file_path, i, total) for i, file_path in
        enumerate(file_list))

    # merged_df = pd.merge(behavior_df, demographic_df[['USERID']], on='USERID', how='left')
    behavior_df=pd.concat(all)
    # 将结果保存到CSV文件
    print("保存合并后的数据到merged_behavior.csv")
    behavior_df.to_csv('merged_behavior.csv', index=False, encoding='utf-8')

def check():
    #E:\Postgraduate\behavior
    import os

    count = 0

    # 初始化一个空的DataFrame来存储合并后的行为数据

    # 遍历behavior文件夹中的所有日志文件
    for root, dirs, files in os.walk('E:\Postgraduate\\behavior'):
        for file in tqdm(files,desc='Processing files', unit='file'):
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                file_name = os.path.basename(file_path)
                sample_id = file_name.split('_')[0]
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                    # 解析Last和L_Start
                    last_update = int(lines[0].split('<=>')[1].strip())
                    start_time_str = lines[1].split('<=>')[1].strip()
                    print(start_time_str)
                    start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H-%M-%S')
                    # 遍历其余行并解析行为数据
                    for line in lines[2:]:
                        if line.strip():  # 跳过空行
                            row_data = {
                                'Sample_ID': sample_id,
                                'Timestamp': None,  # 格式化时间戳为字符串
                                'Process': None,
                                'PID': None,
                                'URL': None,
                                'Address_Handle': None,
                                'Tab_Handle': None,
                                'Version': None,
                                'Window_Handle': None,
                                'Program_Name': None,
                                'Company': None,
                            }
                            fields = line.strip().split('[=]')
                            if fields[0].split('<=>')[0] != 'T':
                                continue
                            for field in fields:
                                try:
                                    key, value = field.split('<=>')
                                except Exception as e:
                                    print('Error in file:', file_path)
                                    print('Error line:', line)

                                    raise ValueError('Error in file:', file_path)

                                # 根据不同的key值将数据添加到DataFrame中
                                if key == 'T':
                                    timestamp = start_time + timedelta(seconds=int(value))  # 计算时间戳
                                    specified_time = datetime(1, 2, 2, 9, 33, 4)
                                    row_data['Timestamp'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                                    if timestamp<specified_time:
                                        print(file_path)
                                        raise




if __name__ == "__main__":
    check()