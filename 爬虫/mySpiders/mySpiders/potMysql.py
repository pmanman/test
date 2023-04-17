"""
*_* coding: utf-8 *_*
author:zmm
time:2022/11/3 10:38
file :potMysql.py
"""
import pymysql
# 导入settings模块
from mySpiders import settings
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
        str = 'create table chinaz(id int auto_increment primary key, uname varchar(255), info varchar(255), paiming varchar(255));'
        cur.execute(str)
        sqlConnect.commit()
        pass
    # 插入数据（insert）
    @staticmethod
    def insert_chinaz(data):
        str = 'insert into chinaz(`uname`, info, paiming) values ("%s","%s","%s");' % (data['name'], data['info'], data['rank'])
        cur.execute(str)
        sqlConnect.commit()
        pass
    # 更新数据（update）
    @staticmethod
    def update_chinaz(s):
        sql = f"update china set uname={s} where id=1"
        cur.execute(sql)
        sqlConnect.commit()  # 执行sql语句
        pass
    # 删除数据（delete）
    @staticmethod
    def delete_chinaz():
        pass
    # 关闭连接（close）
    @staticmethod
    def close_chinaz():
        pass
    def aa(self):
        pass
    pass

