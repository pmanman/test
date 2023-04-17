"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/26 10:36
file :demo1.PY
"""

import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read().decode('utf-8')
print(html)

response = urllib.request.urlopen('https://www.python.org')
html = response.read().decode('utf-8')
print(html)
print(type(response))
print(response.getcode())  # 响应状态码
print(response.geturl())  # 请求地址
print(response.info())  # 页面元信息 response

url = 'http://www.itcast.cn'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
# 构造request对象
requests = urllib.request.Request('http://www.baidu.com', headers=header)
res = urllib.request.urlopen(requests)
html = res.read().decode('utf-8')
print(type(res))
print(res.getcode())  # 响应状态码
print(res.geturl())  # 请求地址
print(res.info())


