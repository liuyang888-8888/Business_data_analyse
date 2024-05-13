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

def update_behavior_data():
    # 读取CSV文件
    sql = """SELECT behavior.index,url FROM behavior"""



    # 建立数据库连接
    conn = pymysql.connect(**config.mysql_config)
    cursor = conn.cursor()


    # 插入数据

    cursor.execute(sql)
    raw_data_tuple = cursor.fetchall()

    for i,row in enumerate(raw_data_tuple):
        #url_dom='{}',url_label='{}'
        update_sql=f"""UPDATE behavior SET url_dom='{}',url_label='{}' WHERE `index`={row[0]}"""
        cursor.execute(sql)
    # 提交事务
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()

if __name__=="__main__":
    save_behavior_data()
    # pass
