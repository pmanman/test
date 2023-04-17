"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/31 8:50
file :微博热搜.py
"""
import requests
import json
import csv

url = ' https://weibo.com/ajax/statuses/topic_band?sid=v_weibopro&category=all&page=1&count=10'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
response = requests.get(url, headers=header)
response.encoding = 'utf-8'
page = response.text
info = json.loads(page)
print(info)

with open('weibo.csv', 'a+', newline="") as f:
    wb = csv.writer(f)
    row = ["排名", "话题", "阅读数", "讨论数", "链接"]
    wb.writerow(row)
    item = info['data']['statuses']
    for i in item:
        # rank = i['rank']
        # topic = i['topic']
        #     if len(i) != 0:
        #         next_title = i['next_title']
        #     else:
        #         next_title = ''
        # read = i['read']
        # mention = i['mention']
        # text= i['text']
        # print(rank, topic, read, mention, images_url)

        a = [i['rank'], i['topic'], i['read'],i['mention']]
        wb.writerow(a)

