"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/12 9:31
file :学习pymongo.py
"""
from pymongo import MongoClient
conn = MongoClient('127.0.0.1', 27017)   # 创建连接
db = conn.test   # 连接mydb数据库，没有则自动创建
my_set = db.stu    # 创建数据集合 自动创建

# 插入数据
# 1.insert_one()插入一条数据
# 2.insert_many()插入多条数据

info = {
    'no': 1,
    'name': 'mike',
    'age': 20
}
# my_set.insert_one(info)

many = [
    {'no': 2, 'name': 'mike', 'age': 20},
    {'no': 3, 'name': '张三', 'age': 22},
    {'no': 4, 'name': '李四', 'age': 18}
     ]
my_set.insert_many(many)

# 查询数据
# 1.find_one()方法：查找一条文档对象
# 2.find_many()方法：查找多条文档对象
# 3.find()方法：查找所有文档对象

# result = my_set.find({'age':20})
# # print(result)
# # for doc in result:
# #     print(doc)

# result = my_set.find_one({'age':20})
# print(result)


# 更新数据
# 1.update_one()方法：更新一条文档对象
# 2.update_many()方法：更新多条文档对象

# my_set.update_one({'age':18},{'$set':{'name':'zhaoliu'}})
# my_set.update_one({'age':5},{'$set':{'name':'zhaoliu'}})
# my_set.update_many({'name': 'mike'}, {'$set': {'age': 19}})
# 删除数据
# 1.delete_one()方法：删除一条文档对象
# 2.delete_many()方法：删除所有

# my_set.delete_one({'age': 18})
conn.close()
