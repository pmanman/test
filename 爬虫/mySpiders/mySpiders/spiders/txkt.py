import scrapy


class TxktSpider(scrapy.Spider):
    name = 'txkt'
    allowed_domains = ['qq.com']
    start_urls = ['http://qq.com/']

    def parse(self, response):
        pass
