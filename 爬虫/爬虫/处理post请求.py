"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/27 8:49
file :处理post.PY
"""
import urllib.request
import urllib.parse
import json

# 构造request对象
url = "https://fanyi.baidu.com/sug"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
# post请求体
data = {
    "kw": "red"
}
info = bytes(urllib.parse.urlencode(data).encode("utf-8"))
requests = urllib.request.Request(url, data=info, headers=header)
response = urllib.request.urlopen(requests)
html = response.read().decode('utf-8')
print(json.loads(html))

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
"Sec-Fetch-Site": "same-origin",
# "Cookie": "BIDUPSID=32ED3A156BF49FA2B9B2AF2010866DF2; PSTM=1663655194; BAIDUID=32ED3A156BF49FA2EEE18BE02A3AD8DE:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=32ED3A156BF49FA2EEE18BE02A3AD8DE:FG=1; BA_HECTOR=00ala5a0akagah84840h69st1hj2pqr18; ZFY=:AUEwBE8ifSR8gj4s0o6UnV52KJpPKP6UpIsAQnxf9S4:C; BDRCVFR[22-MnffAYic]=mk3SLVN4HKm; delPer=0; PSINO=1; H_PS_PSSID=; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664239127; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664239494; ab_sr=1.0.1_ODRhM2QyYTI3ZWU4ZWYxNGRjZWIwYWUyYjE1YzMzNTBlMDY1M2Y1ZmYxYmYzYjBjZTJmMDkyNjZiMmVmZWUwYzlmNWMxMDkxZjczMTQ3MDhlZjIyY2E5N2VhYjM3MjYyMDIxOWRkNTY2YjYwMjNiYjRiZTBkZmI1YjNiOGM3NmY5YzIzNTdkMDczZTE0ZWYxMzUxYzQyMjRjYTFhY2VkOQ=="
}
data = {
    "from": "en",
    "to": "zh",
    "query": "red",
    "transtype": "realtime",
    "simple_means_flag": 3,
    "sign": 207046.510967,
    "token": "d39a881675250496689f9e5feebbc49a",
    "domain": "common"
}
info = bytes(urllib.parse.urlencode(data).encode("utf-8"))
request = urllib.request.Request(url, data=info, headers=header)
# 添加请求头
request.add_header("Cookie", "BIDUPSID=32ED3A156BF49FA2B9B2AF2010866DF2; PSTM=1663655194; BAIDUID=32ED3A156BF49FA2EEE18BE02A3AD8DE:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=32ED3A156BF49FA2EEE18BE02A3AD8DE:FG=1; BA_HECTOR=00ala5a0akagah84840h69st1hj2pqr18; ZFY=:AUEwBE8ifSR8gj4s0o6UnV52KJpPKP6UpIsAQnxf9S4:C; BDRCVFR[22-MnffAYic]=mk3SLVN4HKm; delPer=0; PSINO=1; H_PS_PSSID=; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664239127; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664239494; ab_sr=1.0.1_ODRhM2QyYTI3ZWU4ZWYxNGRjZWIwYWUyYjE1YzMzNTBlMDY1M2Y1ZmYxYmYzYjBjZTJmMDkyNjZiMmVmZWUwYzlmNWMxMDkxZjczMTQ3MDhlZjIyY2E5N2VhYjM3MjYyMDIxOWRkNTY2YjYwMjNiYjRiZTBkZmI1YjNiOGM3NmY5YzIzNTdkMDczZTE0ZWYxMzUxYzQyMjRjYTFhY2VkOQ==")
request.add_header("Connection", "keep-alive")
print(request.get_header("Connection"))
response = urllib.request.urlopen(request)
res = response.read().decode('utf-8')
print(json.loads(res))

# 抓包豆瓣
url = "https://accounts.douban.com/j/mobile/login/basic"
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
"Cookie": "bid=JIza2hBiQQA; apiKey=; __utma=30149280.849795010.1664257170.1664257170.1664257170.1; __utmc=30149280; __utmz=30149280.1664257170.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.3.10.1664257170; login_start_time=1664257405732"
}
data = {
"remember": "true",
"name": 13838214275,
"password": 123456,
}
info = bytes(urllib.parse.urlencode(data).encode("utf-8"))
request = urllib.request.Request(url, data=info, headers=header)
response = urllib.request.urlopen(request)
h = response.read().decode('utf-8')
print(json.loads(h))
