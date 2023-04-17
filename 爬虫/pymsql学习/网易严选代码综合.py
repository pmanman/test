"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/25 8:59
file :网易严选代码综合.py
"""
import requests
import pymysql
import json
import re

class Yan(object):
    def __init__(self):
        self.header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
        self.url = 'https://you.163.com/xhr/globalinfo//queryTop.json'
        self.link = 'https://you.163.com/item/list?categoryId={}&subCategoryId={}'
        self.goodli = []
        self.conn = pymysql.connect(host='localhost', user='root', password='123456', database='tutu', port=3306)
        # 获取游标
        self.cursor = self.conn.cursor()

    def get_cate(self):
        response = requests.get(self.url, self.header)
        response.encoding = 'utf-8'
        info = response.text
        # print(info)
        d = json.loads(info)
        # 字典取值
        cateList = d['data']['cateList']
        for item in cateList:
            cate1_name = item['name']
            subCateGroupList = item['subCateGroupList']
            for sub in subCateGroupList:
                cate2_name = sub['name']
                categoryList = sub['categoryList']
                for cate in categoryList:
                    cate3_name = cate['name']
                    superCategoryId = cate['superCategoryId']
                    id = cate['id']
                    cate3_link = self.link.format(superCategoryId, id)
                    self.get_good(cate1_name, cate2_name, cate3_name, cate3_link)
                    if len(self.goodli) > 0:
                        for i in self.goodli:
                            data = {k: '"' + str(v) + '"' for k, v in i.items()}
                            sql = f'insert into wangyi(cate1, cate2, cate3, name, price, img, des) values({str(data["cate1"])},{data["cate2"]}, {data["cate3"]}, {data["name"]}, {data["price"]}, {data["img"]}, {data["desc"]});'
                            print(sql)
                            self.save(sql)
        self.cursor.close()
        self.conn.close()

    def get_good(self, cate1, cate2, cate3, cate3_link):
        # 请求网页
        response = requests.get(cate3_link, headers=self.header)
        # 指定编码
        response.encoding = 'utf-8'
        # 输出响应文本
        info = response.text
        # print(info)
        # 运用正则匹配所需字符串
        res = re.findall('var json_Data=(.*)};', info)  # (.*)正则中的贪婪匹配
        # print(res[0])
        text = res[0] + "}"
        # json数据类型转化
        data = json.loads(text)
        # 字典取值
        categoryItemList = data['categoryItemList']
        for item in categoryItemList:
            itemList = item['itemList']
            for i in itemList:
                good = {}
                name = i['name']
                simpleDesc = i['simpleDesc']
                retailPrice = i['retailPrice']
                scenePicUrl = i['scenePicUrl'] + '?type=webp&imgageView'
                good['cate1'] = cate1
                good['cate2'] = cate2
                good['cate3'] = cate3
                good['name'] = name
                good['price'] = retailPrice
                good['img'] = scenePicUrl
                good['desc'] = simpleDesc
                self.goodli.append(good)
            pass

    def save(self, sql):
        # 1.连接数据库 2.获取游标
        # 执行sql语句 插入语句
        self.cursor.execute(sql)
        # 提交数据
        self.conn.commit()
        # conn.close()
w = Yan()
w.get_cate()
