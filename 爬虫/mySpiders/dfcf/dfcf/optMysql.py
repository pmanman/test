"""
*_* coding: utf-8 *_*
author:zmm
time:2022/11/4 10:52
file :optMysql.py
"""
import pymysql
# 导入settings模块
from dfcf import settings
# 建立mysql连接
sqlConnect = pymysql.connect(
    host=settings.Mysql_host,
    user=settings.Mysql_user,
    passwd=settings.Mysql_pwd,
    db=settings.Mysql_db,
    port=settings.Mysql_port,
)

# 建立游标
cur = sqlConnect.cursor()
class Sql():
    # 创建表（create）
    @staticmethod
    def create_table():
        str = 'create table dfcf(id int auto_increment primary key, entrance varchar(255), drink varchar(255), possible varchar(255)), painting varchar(255), suggestion varchar(255), boil varchar(255), intrude varchar(255), leg varchar(255), excuse varchar(255), appoinexcusetment varchar(255), science varchar(255), invented varchar(255), cat varchar(255), dog varchar(255);'
        cur.execute(str)
        sqlConnect.commit()
        pass
    # 插入数据（insert）

    @staticmethod
    def insert_dfcf(data):
        str = 'insert into dfcf(entrance, drink,  pp, painting, suggestion, boil, intrude, leg, excuse, appointment, science, invented, cat, dog) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (data['entrance'], data["drink"], data["possible"], data["painting"], data["suggestion"], data['boil'], data["intrude"], data["leg"], data["excuse"], data["appointment"], data["science"], data['invented'], data['cat'], data["dog"])
        cur.execute(str)
        sqlConnect.commit()
        pass
    # 更新数据（update）
    @staticmethod
    def update_dfcf(s):
        pass
    # 删除数据（delete）
    @staticmethod
    def delete_dfcf():
        pass
    # 关闭连接（close）
    @staticmethod
    def close_dfcf():
        pass
    def aa(self):
        pass
    pass
