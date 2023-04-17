"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/8 10:22
file :抓取珠宝.PY
"""
import requests
from lxml import html
url = 'http://www.zhubaojie.com/'
response = requests.get(url)
response.encoding = 'utf-8'
text1 = response.text
page = html.etree.HTML(text1)
i = page.xpath('//ul[@class="site-menu"]/li/a/text()')
print(i)
''''
1 导入模块
2. url 
3.请求方式  post get 
分情况  抓取数据  xpath 
1 导包


'''

