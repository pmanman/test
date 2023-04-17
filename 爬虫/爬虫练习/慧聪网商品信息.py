"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/9 10:21
file :慧聪网商品信息.py
"""
import requests
from lxml import html
# 请求
url = 'https://www.hc360.com/seller/search93.html'
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
response = requests.get(url, headers=header)
# 指定编码
response.encoding = 'utf-8'
# 文档树对象
html = html.etree.HTML(response.text)
# 解析
goods = html.xpath('//div[@class="wrap-grid"]/ul/li')
for good in goods:
    gg = {}
    name = good.xpath('.//dd[@class="newName"]/a/@title')  # 名字
    price = good.xpath('.//span[@class="seaNewPrice"]/text()')  # 价格
    img = good.xpath('.//div[@class="picmid pRel"]//img/@src')  # 图片
    if len(name) > 0 and len(price) > 0 and len(img) > 0:
        host = 'https://www.hc360.com/'
        a = img[0].replace('../', host)
        gg['name'] = name[0]
        gg['price'] = price[-1]
        gg['img'] = a
    else:
        print(name[0])


