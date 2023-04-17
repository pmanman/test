"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/28 15:55
file :解析豆瓣.PY
"""
import requests
# 登录url地址
url = 'https://accounts.douban.com/j/mobile/login/basic'
# 登录需要的请求头
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
"Cookie": 'll="108303"; bid=JIza2hBiQQA; apiKey=; __utma=30149280.849795010.1664257170.1664261879.1664351110.3; __utmc=30149280; __utmz=30149280.1664351110.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; last_login_way=phone; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.26318; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1664351912%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.2fad=*; _pk_id.100001.2fad=2254cf93f6121eda.1664351912.1.1664351952.1664351912.; __utmt=1; login_start_time=1664352452686; user_data={%22area_code%22:%22+86%22%2C%22number%22:%2213838214275%22%2C%22code%22:%229053%22}; vtoken=undefined; __gads=ID=331d82bee17088d8-22e6d94abfd6000b:T=1664352475:RT=1664352475:S=ALNI_MbHdosgZ2arHvhJ8W09m3KG4Brc1Q; __gpi=UID=000009e9b69f037b:T=1664352475:RT=1664352475:S=ALNI_MYw6Lb36J918TbbOp-skKTyy1fVQQ; __utmb=30149280.32.10.1664351110'
}
# 需要的参数
data = {
    "remember": "true",
    "name": "13838214275",
    "password": "zmm0524."
}
session = requests.session()
res = session.post(url, data=data, headers=header)
res.encoding = 'utf-8'
print(res.text)
link = 'https://www.douban.com/people/263183940/?_i=4352485JIza2hB'
header1 = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
"Referer": "https://www.douban.com/"
}
res2 = requests.get(link, headers=header1)
print(res2)