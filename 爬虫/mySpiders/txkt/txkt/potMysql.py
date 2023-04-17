"""
*_* coding: utf-8 *_*
author:zmm
time:2022/11/3 20:42
file :potMysql.py
"""
import pymysql
# 导入settings模块
from txkt import settings
# 建立mysql连接
sqlConnect = pymysql.connect(
    host=settings.Mysql_host,
    user=settings.Mysql_user,
    passwd=settings.Mysql_pwd,
    db=settings.Mysql_db,
    port=settings.Mysql_port
)

# 建立游标
cur = sqlConnect.cursor()
class Sql():
    # 创建表（create）
    @staticmethod
    def create_table():
        str = 'create table txkt(id int auto_increment primary key, uname varchar(255), link varchar(255));'
        cur.execute(str)
        sqlConnect.commit()
        pass
    # 插入数据（insert）
    @staticmethod
    def insert_txkt(data):
        str = 'insert into txkt(uname, link) values ("%s","%s");' % (data['name'], data['link'])
        cur.execute(str)
        sqlConnect.commit()
        pass
    # 更新数据（update）
    @staticmethod
    def update_txkt(s):
        sql = f"update txkt set uname={s} where id=1"
        cur.execute(sql)
        sqlConnect.commit()  # 执行sql语句
        pass
    # 删除数据（delete）
    @staticmethod
    def delete_txkt():
        pass
    # 关闭连接（close）
    @staticmethod
    def close_txkt():
        pass
    def aa(self):
        pass
    pass
