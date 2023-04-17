"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/26 18:58
file :request抓取.PY
"""
import urllib.parse
import urllib.request
url = "http://www.baidu.com/s"
word = {"wd": "京东"}
word = urllib.parse.urlencode(word)
new_url = url + "?" + word
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
request = urllib.request.Request(new_url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)