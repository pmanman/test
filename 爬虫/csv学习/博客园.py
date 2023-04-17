"""
*_* coding: utf-8 *_*
author:zmm
time:2022/11/2 8:49
file :博客园.py
"""
import csv
import requests
from lxml import html
# 请求地址
url = 'https://www.cnblogs.com/AggSite/AggSitePostList'
# 请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
# post 请求携带的参数（PageIndex变化参数）
response = requests.get(url, headers=header)
response.encoding = 'utf-8'
page = html.etree.HTML(response.text)
# https://www.cnblogs.com/#p2
# https://www.cnblogs.com/#p3
with open("bokeyuan.csv", "a+", newline="", encoding='utf-8-sig') as f:
    obj = csv.writer(f)
    row = ["名字", "链接"]
    obj.writerow(row)
    for i in range(1, 4):
        page_link = url + '#p' + str(i)
        res = requests.get(page_link, headers=header)
        res.encoding = 'utf-8'
        page1 = html.etree.HTML(res.text)
        # 得到所有的文章名字
        course_li = page1.xpath('//div[@class="post-list"]/article/section/div')
        for course in course_li:
            name = course.xpath('.//a/text()')
            link = course.xpath('.//a/@href')
            if name:
                name = name[0]
            else:
                name = ''
            if link:
                link = link[0]
            else:
                link = ''
            obj.writerow([name, link])
