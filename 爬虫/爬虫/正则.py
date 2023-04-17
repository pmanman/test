"""
*_* coding: utf-8 *_*
author:zmm
time:2022/9/30 15:36
file :正则.PY
"""
# flag:
# 1.知道正则三个匹配方法 以及区别
# match 从头开始，找不到会报错，返回None
# search 从整个字符串开始匹配，匹配一次成功结束
# findall 匹配整个字符串，将匹配成功的结果都返回这些字符串的列表中
import re
# ret = re.match('\d', '速度与激情10')
# ret = re.match('情', '速度与激情10激情')
ret = re.findall('情', '速度与激情10激情')
print(ret)

# 2. 理解 \d和\d+
s1 = '阅读量9999，点赞数1111'
a = re.findall('\d', s1)
print(a)
b = re.findall('\d+', s1)
print(b)
# *: 匹配0个或无数个
# +: 匹配1次过无数个
# ?: 匹配1个或0个
# .(点): 匹配任意字符

# 3.会使用re.findall()  返回的是列表

# 4.理解贪婪模式与非贪婪模式
#  贪婪(.*) 非贪婪(.*?)\
# 3.匹配出所有的浮点数
# s = "80.2 fds2.1 0.003"---输出结果["80.2","2.1","0.003"]

# 5.把一个字符串中非数字的内容拼成一个字符串
# 例如输入的是 a1b2c3----输出"abc"
a = 'a1b2c3'
b = re.findall('\d+', a)
print(b)
c = "".join(b)
print(c)
