"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/30 10:50
file :京东.PY
"""
# 1.导包 2.抓包 3.使用requests进行请求 4.获取响应文本信息 5.转换文档树类型 6.使用xpath匹配所需信息
import requests
from lxml import html
url = 'https://www.jd.com'
r = requests.get(url)
print(r.text)
html = html.etree.HTML(r.text)
data = html.xpath('//li[@class="cate_menu_item"]/a/text()')
print(data)

header = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
rp = requests.get(url, headers=header)
rp.encoding = 'utf-8'
page = rp.text
html = html.etree.HTML(page)
html.xpath('//div[@id="j_cate"]/ul/li/a/text()')


