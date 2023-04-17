"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/26 15:45
file :实现数据传输.PY
"""
import urllib.parse

dic = {
    "姓名": "图图",
    "家庭地址": "翻斗花园"
}
info = urllib.parse.urlencode(dic)  # 编码
print(info)

res = urllib.parse.unquote(info)
print(res)

import urllib.request
url = "http://www.baidu.com/s"
word = {"wd": "河南艺术职业学院"}
word = urllib.parse.urlencode(word)
new_url = url + "?" + word
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
request = urllib.request.Request(new_url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)