"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/28 16:30
file :91家纺网.py
"""
import requests
from lxml import html
url = 'http://detail.91jf.com/goods/7hu49f3'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=header)
res.encoding = 'utf-8'
page = res.text
print(page)
# info = html.etree.HTML(page.text)

