# coding=utf-8
# -----道阻且长 行则将至-------
# -----   刘 洋 洋   -----
# ---  版权所有 侵权必究  ----
# ---- 一切解释权归本人所有 ----
# 日 期：2024/4/29 
# 时 间：21:03
import pandas as pd
from joblib import Parallel, delayed
from tqdm import tqdm

import config
import pymysql
import tools.process_data as label
def update_behavior_data():
    # 读取CSV文件
    sql = """SELECT behavior.index,url FROM behavior"""



    # 建立数据库连接
    conn = pymysql.connect(**config.mysql_config)
    cursor = conn.cursor()


    # 插入数据

    cursor.execute(sql)
    raw_data_tuple = cursor.fetchall()
    data_list = [list(ele) for ele in raw_data_tuple]
    for row in tqdm(data_list):
        #url_dom='{}',url_label='{}'
        if row[1] is not None:
            dom=label.process_data(row[1])
            labels=label.get_category(dom)
            update_sql=f"""UPDATE behavior SET url_dom='{dom}',url_label='{labels}' WHERE `index`={row[0]}"""
            cursor.execute(update_sql)
    # 提交事务
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()


def update_all_data():
    sql = """SELECT behavior.index,url FROM behavior"""
    # 建立数据库连接
    conn = pymysql.connect(**config.mysql_config)
    cursor = conn.cursor()

    # 插入数据

    cursor.execute(sql)
    raw_data_tuple = cursor.fetchall()
    data_list = [list(ele) for ele in raw_data_tuple]
    Parallel(n_jobs=-1, verbose=100)(
        delayed(muli_update_behavior_data)(file_path) for file_path in
        tqdm(data_list))
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()
def muli_update_behavior_data(row):
    if row[1] is not None and row[1] !='NULL':
        conn = pymysql.connect(**config.mysql_config)
        cursor = conn.cursor()
        dom = label.process_data(row[1])
        labels = label.get_category(dom)
        update_sql = f"""UPDATE behavior SET url_dom='{dom}',url_label='{labels}' WHERE `index`={row[0]}"""
        cursor.execute(update_sql)
        # 提交事务
        conn.commit()

        # 关闭连接
        cursor.close()
        conn.close()
if __name__=="__main__":
    update_all_data()
    # pass
