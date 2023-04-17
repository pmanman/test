"""
*_* coding: utf-8 *_*
author:zmm
time:2022/11/3 20:37
file :tengxunketang.py
"""
import scrapy
from txkt.items import TxktItem

class TengxunSpider(scrapy.Spider):
    name = 'tengxunketang'

    allowed_domains = ['qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001']

    def parse(self, response):
        li = response.xpath('//div[@class="course-list"]/div')
        for i in li:
            item = TxktItem()
            name = i.xpath('.//h3[@class="kc-course-card-name"]/@title').extract_first()
            link = i.xpath('.//a[@class="kc-course-card js-report-link kc-list-course-card kc-course-card-column"]/@href').extract_first()
            link = 'https://ke.qq.com/' + link
            print(name, link)
            item['name'] = name
            item['link'] = link
            yield item
        pass