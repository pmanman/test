import scrapy
import json
import urllib.parse
class WbSpider(scrapy.Spider):
    name = 'wb'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.com/ajax/side/hotSearch']

    def parse(self, response):
        info1 = json.loads(response.text)
        info = info1['data']['realtime']
        for i in info:
            data = {}
            rank = i['rank']
            word = i['word']
            l = urllib.parse.quote('name')
            link = f'https://s.weibo.com/weibo?q={l}$topic_ad='
            data['rank'] = rank
            data['word'] = word
            data['link'] = link
            yield data
        pass
