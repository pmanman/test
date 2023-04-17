"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/31 15:48
file :腾讯课堂-后台开发.py
"""
import requests
from lxml import html
import csv

url = 'https://ke.qq.com/course/list?mt=1001&st=2054'
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=header)
response.encoding = 'utf-8'
page = html.etree.HTML(response.text)
# print(page)
# page1 = page.xpath('//div[@class="block-container"]/ul/li')
# page_num = int(page1[-1])
with open('腾讯课堂.csv', 'a+', newline='', encoding='utf-8-sig') as f:
    obj = csv.writer(f)
    row = ['课程名字', '课程链接']
    obj.writerow(row)
    for i in range(1, 35):
        # page_link = f"https://ke.qq.com/course/list?mt=1001&st=2054&page={i}"
        page_link = url + '&page=' + str(i)  # 字符串拼接时必须全部为str 类型
        res = requests.get(page_link, headers=header)
        res.encoding = 'utf-8'
        page = html.etree.HTML(res.text)
        # 得到所有课程列表
        course_li = page.xpath('//section[@class="course-card-expo-wrapper"]/a')
        for course in course_li:
            name = course.xpath('.//div/h3/@title')
            link = course.xpath('.//@href')
            if name:
                name = name[0]
            else:
                name = ''
                # 完整的课程链接
            if link:
                course_link = 'https://ke.qq.com' + link[0]
            else:
                course_link = ''
                # 将信息写入csv文件
            obj.writerow([name, course_link])

# 看见字典根据键取值看见列表直接循环
'https://ke.qq.com/course/list?mt=1001&st=2054&page=2'
'https://ke.qq.com/course/list?mt=1001&st=2054&page=3'
