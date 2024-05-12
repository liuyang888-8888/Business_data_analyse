# coding=utf-8
# -----道阻且长 行则将至-------
# -----   刘 洋 洋   -----
# ---  版权所有 侵权必究  ----
# ---- 一切解释权归本人所有 ----
# 日 期：2024/4/29 
# 时 间：21:03
import pandas as pd
import config
import pymysql
def get_all_data():
    # 从数据库取数据

    #名称 评论 主题 来源
    sql = """SELECT screen_name,text,topics,source FROM `weibo`"""
    db = pymysql.connect(**config.mysql_config)
    cursor = db.cursor()
    cursor.execute("USE weibo")
    cursor.execute(sql)
    data_tuple = cursor.fetchall()
    db.close()

    data_list = [list(ele) for ele in data_tuple]
    reviews = [sub[1] for sub in data_list]
    return data_list

def save_behavior_data():
    # 读取CSV文件
    data = pd.read_csv(config.merged_behavior_path)



    # 建立数据库连接
    conn = pymysql.connect(**config.mysql_config)
    cursor = conn.cursor()


    # 插入数据
    for index, row in data.iterrows():
        if pd.isna(row['Process']):
            proces= None
        else:
            proces=row['Process']

        if pd.isna(row['URL']):
            ur=None
        else:
            if len(row['URL'])>255:
                ur=row['URL'][:253]
            else:
                ur=row['URL']

        if pd.isna(row['Program_Name']):
            proname=None
        else:
            proname=row['Program_Name']

        if pd.isna(row['Company']):
            comp=None
        else:
            comp=row['Company']
        cursor.execute('INSERT INTO behavior (id,time,process,url,program_name,company) VALUES (%s, %s,%s,%s,%s,%s)',
                       (row['Sample_ID'],
                        row['Timestamp'],
                        proces,
                        ur,
                        proname,
                        comp))

    # 提交事务
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()

if __name__=="__main__":
    #save_behavior_data()
    pass
