"""
*_* coding: utf-8 *_*
author:zmm
time:2022/11/7 15:51
file :optMysql.py
"""
import pymysql
# 导入settings模块
from wangyi import settings
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
        str = 'create table wyyx(id int auto_increment primary key, cate1 varchar(255),  cate2 varchar(255),cate3 varchar(255);'
        cur.execute(str)
        sqlConnect.commit()
        pass
    # 插入数据（insert）

    @staticmethod
    def insert_wyyx(data):
        str = 'insert into wyyx(cate1, cate2, cate3) values ("%s","%s","%s");' % (data['cate1'], data["cate2"], data['cate3'])
        cur.execute(str)
        sqlConnect.commit()
        pass
    # 更新数据（update）
    @staticmethod
    def update_wyyx(s):
        pass
    # 删除数据（delete）
    @staticmethod
    def delete_wyyx():
        pass
    # 关闭连接（close）
    @staticmethod
    def close_wyyx():
        pass
    def aa(self):
        pass
    pass
