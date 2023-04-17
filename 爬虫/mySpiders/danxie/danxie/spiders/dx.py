import scrapy


class DxSpider(scrapy.Spider):
    name = 'dx'
    allowed_domains = ['www.go2.cn']
    start_urls = [f'http://www.go2.cn/search/all/?category_id=all&search_1=1&q=%E5%8D%95%E9%9E%8B&kl=hot&page={i}' for i in range(1, 5)]

    def parse(self, response):
        li = response.xpath('//div[@class="search-result-list"]/ul/li')
        for i in li:
            dict = {}
            name = i.xpath('.//div[@class="pro-name app-text-nowrap"]/text()').extract_first()
            info = i.xpath('.//div[@class="pro-info app-text-nowrap"]/text()').extract_first()
            price = i.xpath('.//div/span[@class="price"]/text()').extract_first()
            link = i.xpath('.//a/@href').extract_first()
            img = i.xpath('.//img/@src').extract_first()
            img1 = f'http://z.go2.cn{link}'
            link1 = f'http://www.go2.cn{img}'
            dict['name'] = name
            dict['info'] = info
            dict['price'] = price
            dict['img1'] = img1
            dict['link1'] = link1
            yield dict

        pass
