"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/25 22:56
file :包牛牛.py
"""

import requests  # 导包

url = 'http://www.bao66.cn/web/'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers=header)
print(resp.text)
print(resp.status_code)  # 响应状态码
print(resp.url)  # 请求url