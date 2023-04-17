"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/26 9:28
file :包牛牛抓信息.py
"""
import requests
from lxml import html
from pymongo import MongoClient
def bnn():
    conn = MongoClient('127.0.0.1', 27017)  # 创建连接
    db = conn.test  # 连接mydb数据库，没有则自动创建
    my_set = db.bnn  # 创建数据集合 自动创建
    for i in range(1, 6):
        url = f'http://www.bao66.cn/search/web,407,0,钱包,,{i},5.html'
        header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
        res = requests.get(url, headers=header)
        print(res)
        page = html.etree.HTML(res.text)
        res1 = page.xpath('//ul[@class="product_box"]/li')
        for i in res1:
            dict = {}
            name = i.xpath('.//a[@class="name"]/text()')
            if name:
                dict["name"] = name[0]
            else:
                name = ''
            title = i.xpath('.//p[@class="product_desc"]/@title')
            if title:
                dict["title"] = title[0]
            else:
                title = ''
            price = i.xpath('.//a[@class="price"]/b/text()')
            if price:
                dict["price"] = price[0]
            else:
                price = ''
            print(name, title, price)
            my_set.insert_many([dict])
            # my_set.insert_one([dict])
z = bnn()






