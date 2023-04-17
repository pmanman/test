"""
*_* coding: utf-8 *_*
author:zmm
time:2022/11/2 10:50
file :博客园 （老师的）.py
"""
import requests
from lxml import html
import json
# 注意点：1.post请求
#         2.请求头信息还需要content-type
#        3.post 请求参数需要序列化

#请求地址：
url = 'https://www.cnblogs.com/AggSite/AggSitePostList'
#请求头
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'content-type': 'application/json; charset=UTF-8'
}
#post 请求携带的参数（PageIndex变化参数）
data = {"CategoryType":"SiteHome","ParentCategoryId":0,"CategoryId":808,"PageIndex":1,"TotalPostCount":4000,"ItemListActionName":"AggSitePostList"}
response = requests.post(url,headers = header,data=json.dumps(data))
# response = requests.post(url,headers = header,data=data)
response.encoding = 'utf-8'
res = response.text
print(response.status_code)
# print(res)
page = html.etree.HTML(res)
article_li = page.xpath('//article[@class="post-item"]')
for article in article_li:
    title = article.xpath('.//a[@class="post-item-title"]/text()')[0]
    link = article.xpath('.//a[@class="post-item-title"]/@href')[0]
    print(title,link)