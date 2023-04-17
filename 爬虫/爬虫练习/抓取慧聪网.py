"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/8 10:40
file :抓取慧聪网.PY
"""
import requests
from lxml import html
url = 'https://www.hc360.com/'
response = requests.get(url)
response.encoding = 'utf-8'
html = html.etree.HTML(response.text)
# a = html.xpath('//dd/dl/dt/span/text()')
# print(a)
cates = html.xpath('//dd[@class="aside-dd"]/dl')# 所有类目12个 包含一级，二级，三级类目
for cate in cates:
    print(cate)
    cate1 = cate.xpath('.//dt/span/text()')# 一级类目
    cate_li = cate.xpath('.//dd/dl')# 包含所有三级类目的二级类目列表
    for i in cate_li:
        dict = {}
        cate2 = i.xpath('.//dt/text()')# 二级类目
        # cate3 = i.xpath('.//dd/a/text()')
        cate3 = i.xpath('.//dd/a')# 三级类目
        for j in cate3:
            cate3l = j.xpath('.//text()')
            dict['cate1'] = cate1# 一级类目
            dict['cate2'] = cate2
            dict['cate3'] = cate3l
            print(dict)
        print('-------------------------')