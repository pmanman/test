"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/10 15:35
file :复习pymysql.py
"""
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='123456', database='tutu', port=3306)
# 获取游标
cursor = conn.cursor()
# 执行sql语句
s = 'UPDATE wls SET age=15 WHERE id=7'
sql = 'select * from wls;'
cursor.execute(s)
cursor.execute(sql)

print(cursor.fetchall())
# print(cursor.fetchmany(2))
# 提交数据
conn.commit()
cursor = conn.cursor()
# 4. 关闭游标
cursor.close()