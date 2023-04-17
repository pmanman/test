"""
*_* coding: utf-8 *_*
author:zmm
time:2022/11/23 14:11
file :初级实现.py
"""
import csv
import json
import requests
url = 'https://so.csdn.net/api/v3/search?q=python&t=all&p=1&s=0&tm=0&lv=-1&ft=0&l=&u='
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=header)
res.encoding = 'utf-8'
res1 = json.loads(res.text)
# print(res1)
cate = res1['result_vos']
with open("cjsx.csv", "w+", newline="") as f:
    a = csv.writer(f)
    one = ['标题', '链接']
    a.writerow(one)
    for i in cate:
        title = i['title']
        new_title = title.replace('<em>', '').replace('</em>', '')
        if new_title:
            new_title = new_title
        else:
            new_title = ''
        link = i['url']
        if link:
            link = link
        else:
            link = ''
        # print(new_title, link)
        two = [new_title, link]
        a.writerow(two)


