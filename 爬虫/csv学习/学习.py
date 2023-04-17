"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/13 11:34
file :学习.py
"""
import csv

# 1.向csv文件中写入文件
# newline = '' 没有空行， 否则每条数据之间有空行
with open("stu.csv", "a", newline='') as f:
    row3 = ['姓名', '年龄', '职业',  '住址', '工资']
    row = ['光头强', '25', '伐木工', '狗熊岭', '0']
    row2 = ['海绵宝宝', '18', '做汉堡', '海底世界', '海币']
    # 写入
    # write = csv.writer(f)
    # write.writerow(row2)
    # print("写入完毕！")

# 2.读取
# 读取文件表头数据
# 方式一
with open("stu.csv") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    for i in rows:
        print(i)
    # print(rows[0])

# # 方式二
# with open("test.csv") as f:
#     # 1.创建阅读器对象
#     reader = csv.reader(f)
#     # 2.读取文件第一行数据
#     head_row = next(reader)
#     print(head_row)
#
# #1.获取文件某一列数据

# with open("test.csv") as f:
#     reader = csv.reader(f)
#     column=[row for row in reader]
#     print(column[2])
#
#

# with open("test1.csv",'a+',newline='') as f:
#      row = ['光头强', '25', '伐木工', '狗熊岭', '0']
#      row2 = ['海绵宝宝', '18', '做汉堡', '海底世界', '海币']
#      write=csv.writer(f)
#      write.writerow(row)
#      f.seek(0)
#      reader=csv.reader(f)
#      rows=[row for row in reader]
#      #2.遍历rows列表
#      for row in rows:
#          #3.把每一行写到Aim.csv中
#          print(row)
#      print("完毕！")
