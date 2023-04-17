"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/20 11:16
file :微博.py
"""
import requests
import json
import urllib.parse
url = 'https://weibo.com/ajax/side/hotSearch'
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=header)
# 指定编码格式
res.encoding = 'utf-8'
# 获取网页文本信息
page = res.text
print(page)
# 使用json模块
info = json.loads(page)
realtime = page['data']['realtime']
for item in realtime:
    title = item['word']
    category = item['category']
    # 拼接 link
    link = 'https://s.weibo.com/weibo?q=%23{}%23&topic_ad='.format(title)
    # url中文编码
    a = urllib.parse
