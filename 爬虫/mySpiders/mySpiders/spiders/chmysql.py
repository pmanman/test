"""
*_* coding: utf-8 *_*
author:zmm
time:2022/11/3 10:25
file :chmysql.py
"""
import scrapy
from mySpiders.items import MyspidersItem
# 存储数据到MySQL数据库
# 1.写spiders文件（该文件要和items文件关联）  2.要修改settings文件（添加数据库的配置，打开管道）  3.修改管道文件（pipelines文件，该文件要操作数据库）  4.新增一个py文件用于做增删改查

class ChinazSpider(scrapy.Spider):
    name = 'chmysql'  # 爬虫的识别名称
    allowed_domains = ['chinaz.com']  # 爬虫搜索的域名范围
    start_urls = ['https://top.chinaz.com/hangye/']  # 爬取的起始URL元组或者列表
    def parse(self, response):
        li = response.xpath('//ul[@class="listCentent"]/li')
        for i in li:
            item = MyspidersItem()
            name = i.xpath('.//a/@title').extract_first()
            info = i.xpath('.//p[@class="RtCInfo"]/text()').extract_first()
            rank = i.xpath('.//strong[@class="col-red02"]/text()').extract_first()
            # print(name, info, rank)
            item['name'] = name
            item['info'] = info
            item['rank'] = rank
            yield item
        pass
