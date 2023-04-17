"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/27 14:38
file :requests.PY
"""
import requests
# 1.基本的get请求
link = 'https://www.douban.com'
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
response = requests.get(link, headers=header)# 发送请求
response.encoding = 'utf-8'
print(response.text)

# 带参数的get
s1 = 'https://www.baidu.com/s?wd=河南艺术职业学院'
res1 = requests.get(s1, headers=header)
res1.encoding = 'utf-8'
print(res1.text)

s2 = 'https://www.baidu.com/s?'
params = {
    "wd": "河南艺术职业学院"
}
res2 = requests.get(s1, headers=header)
res2.encoding = 'utf-8'
print(res2.text)

url = 'http://httpbin.org.get'
req = requests.get(url)
print(req.text)
