"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/21 10:36
file :网易严选美食酒水.py
"""
# 导包
import requests
from lxml import html
import re
import json

# 请求的url和请求头
url = ' https://you.163.com/item/list?categoryId=1005002&_stat_area=nav_5&_stat_referer=index'
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
# 请求网页
response = requests.get(url, headers=header)
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
# print(type(data))
# 字典取值
categoryItemList = data['categoryItemList']
for item in categoryItemList:
    itemList = item['itemList']
    for i in itemList:
        name = i['name']
        print(name)
    pass




