"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/28 10:25
file :demo1.PY
"""
import requests
import json
# 带参数的get请求
hea = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
url = 'http://httpbin.org/get?name=图图&age=3'
response = requests.get(url, headers=hea)
print(response.text)

# 方法二
url = "http://httpbin.org/get"
pa = {
    "name": "嘟嘟",
    "class": 1
}
res = requests.get(url, params=pa, headers=hea)
print(res.text)

# post请求
url1 = 'http://httpbin.org/post'
data = {
    "name": "python"
}
res2 = requests.post(url1, data=data, headers=hea)
print(res2.text)

# 百度翻译
url2 = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
data = {
"from": "en",
"to": "zh",
"query": "aa",
"transtype": "realtime",
"simple_means_flag": 3,
"sign": "922561.717040",
"token": "d39a881675250496689f9e5feebbc49a",
"domain": "common"
}
h = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
"Cookie": 'BIDUPSID=32ED3A156BF49FA2B9B2AF2010866DF2; PSTM=1663655194; BAIDUID=32ED3A156BF49FA2EEE18BE02A3AD8DE:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=32ED3A156BF49FA2EEE18BE02A3AD8DE:FG=1; ZFY=:AUEwBE8ifSR8gj4s0o6UnV52KJpPKP6UpIsAQnxf9S4:C; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDRCVFR[22-MnffAYic]=mk3SLVN4HKm; delPer=0; PSINO=1; H_PS_PSSID=; BA_HECTOR=0g80a1ag2g0485ag0kak9uq41hj7dil1b; BCLID=9910674386680117627; BCLID_BFESS=9910674386680117627; BDSFRCVID=ajuOJexroG0uo4Jj-znsuRnt6uweG7bTDYrEDb8tOfSVLYPVJeC6EG0Pts1-dEu-EHtdogKKBeOTHn0F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=ajuOJexroG0uo4Jj-znsuRnt6uweG7bTDYrEDb8tOfSVLYPVJeC6EG0Pts1-dEu-EHtdogKKBeOTHn0F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3h3RrX26rDHJTg5DTjhPrM-f6tWMT-MTryKKJaaKbkj66uhRbh04C3jlofKx-fKHnRh4oN3n_Wfh7I0pjdWq8ZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPULxo9LUvXtgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DLlD6-a3e; H_BDCLCKID_SF_BFESS=tR3h3RrX26rDHJTg5DTjhPrM-f6tWMT-MTryKKJaaKbkj66uhRbh04C3jlofKx-fKHnRh4oN3n_Wfh7I0pjdWq8ZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPULxo9LUvXtgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DLlD6-a3e; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664239127,1664333410; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664333493; ab_sr=1.0.1_OGUwMGIwMzU3NTgwZWU2OWJmOGU0OTUwYTdiMWY5NjJlMjVjZGRiNWZiMmEwMDVlMDg3NWVlZDhhZmZjY2RmZmU1NmExMzc0ZTdkMmY0MGM4ZWI1ZTEzNDUwYzRjZTY1NWY2NmYwYmFjYWZmMDU1NmYyNmQxNzAyYmNkZDgyZTFmMDhlNDI0ODZlOWY4NWQ0Yjk3MmU2YjEzNjRhNWViYQ=='
}
res3 = requests.post(url2, data=data, headers=h)
print(json.loads(res3.text))