"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/29 14:05
file :XPath和lxml.PY
"""

from lxml import html

# 目的：使用xpath获取html中想要的信息

# 1.得到网页响应内容 response.text
doc = """
<div>
    <ul>
        <li class="item-0">
            <a href="link1.html">first item</a>
        </li>
        <li class="item-1">
            <a href="link2.html">second item</a>
        </li>
        <li class="item-inactive">
            <a href="link3.html">third item</a>
        </li>
        <li class="item-1">
            <a href="link4.html">fourth item</a>
        </li>
        <li class="item-0">
            <a href="link5.html">fifth item</a> 
        </li> 
    </ul>
 </div>
"""

# 2.将响应内容转化成文档树对象
page = html.etree.HTML(doc)
# 3.使用xpath
# li = page.xpath('//li')  # 获取任意的li标签
li = page.xpath('//div/ul/li')
# 获取任意的a标签
# a = page.xpath('//a')
# a = page.xpath('//li/a')
a = page.xpath('//div/ul/li/a')
# 获取任意的a标签的href属性
shu = page.xpath('//a/@href')
# 获取任意的li标签的class属性
c = page.xpath('//li/@class ')
# 获取任意的a标签的文字信息
te = page.xpath('//a/text()')
# 获取第一个的a标签的文字信息
# tel = page.xpath('//li/a/text()')
tel = page.xpath('//li[1]/a/text()')
# 获取最后一个的a标签的文字信息
# wen = page.xpath('//li[last()]/a/text()')
wen = page.xpath('//li/a/text()')[-1]
# 获取最class = item-0 的li标签的a的标签的href属性
w = page.xpath('//li[@class="item-0"]/a/@href')
# 获取class为item的ul标签下href属性为item-0的a标签的文本信息
# u = page.xpath('//ul[class="item"]/li/a[@href="link1.html"]/text()')
u = page.xpath('//ul[class="item"]//a[@href="link1.html"]/text()')
# contains函数
it = page.xpath('//*[contains(@class,"item")]')
# starts-with函数
s = page.xpath('//*[starts-with(@href,"link5")]')
# position位置
p = page.xpath('//li[position()<3]/a/text()')
print(len(p))

