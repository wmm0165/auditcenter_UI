# -*- coding: utf-8 -*-
# @Time : 2019/8/14 10:38
# @Author : wangmengmeng
import pymysql
from config.cfg import *


class ConnectDB:
    def __init__(self):
        print('start connecting MySQL...')
        try:
            self.host = host
            self.port = int(port)
            self.username = user_name
            self.password = pwd
            self.db_sf_full = db_auditcenter
        except Exception as e:
            print(e)
        else:
            print("数据库连接成功！")

    def connect(self):
        return pymysql.Connect(host=self.host, port=self.port, user=self.username, passwd=self.password,
                               database=self.db_sf_full, charset='utf8')



if __name__ == '__main__':
    con = ConnectDB()
    # cur = con.connect().cursor() # 返回格式为 元组里嵌套元组
    """
    如：((1002, '3', 'wangmm', '王萌萌', '122', '122', 0, datetime.datetime(2020, 3, 9, 14, 28, 18), None), (12002, '3', 'wangmm', '王萌萌', 'vvv', 'vvv', 0, datetime.datetime(2020, 3, 13, 13, 43, 11), None))
    """
    cur = con.connect().cursor(pymysql.cursors.DictCursor) # 返回格式为 列表里嵌套字典
    """
    如：[{'id': 1002, 'pharmacist_id': '3', 'pharmacist_name': 'wangmm', 'pharmacist_realname': '王萌萌', 'tag': '122', 'tag_py': '122', 'default_flag': 0, 'created_time': datetime.datetime(2020, 3, 9, 14, 28, 18), 'modified_time': None}, {'id': 12002, 'pharmacist_id': '3', 'pharmacist_name': 'wangmm', 'pharmacist_realname': '王萌萌', 'tag': 'vvv', 'tag_py': 'vvv', 'default_flag': 0, 'created_time': datetime.datetime(2020, 3, 13, 13, 43, 11), 'modified_time': None}]
    """
    cur.execute('SELECT * FROM `sf_collect_tag`')
    # print(cur.fetchone())  # 查询一条数据
    # print(cur.fetchall())  # 查询多条数据
    print(cur.fetchmany(1))  # 查询指定条数据
