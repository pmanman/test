"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/8 13:52
file :json京东.PY
"""
import json
import requests
url = ' https://dc.3.cn/category/get?&callback=getCategoryCallback'
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
# 请求网页信息
response = requests.get(url, headers=header)
# response.encoding = 'utf-8'
# 得到页面信息（str类型）
info = response.text  # 查看网页源代码
print(info)
info = info.replace('getCategoryCallback(', '').replace(')', '')
# 转换数据类型
page = json.loads(info)
print(type(page))
# 层层取值
data = page["data"]
for item in data:
    s = item["s"]
    # print(s)
    for i in s:
        it = i['s']
        # print(it)
        for j in it:
            name = j['n']
            # print(name)
            na = name.split('|')[1]
            print(na)
            pass
    break
