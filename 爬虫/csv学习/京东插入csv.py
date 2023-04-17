"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/14 11:15
file :京东插入csv.py
"""
import csv
import requests
from lxml import html
url = 'https://www.jd.com/'
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"
}
response = requests.get(url, headers=header)
print(response.text)
h = html.etree.HTML(response.text)
y = h.xpath('//li[@class="cate_menu_item"]/a/text()')
print(y)
with open("京东.csv", "a+", newline="") as f:
    jd = csv.writer(f)
    jd.writerow(y)
