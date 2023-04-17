import scrapy


class TxktSpider(scrapy.Spider):
    name = 'txkt'
    allowed_domains = ['ke.qq.com']
    start_urls = [f'https://ke.qq.com/course/list?mt=1001&st=2064&page={i}' for i in range(1, 35)]

    def parse(self, response):
        li = response.xpath('//div[@class="course-list"]/div')
        for item in li:
            data = {}
            name = item.xpath('.//h3/@title').extract_first()
            link = item.xpath('.//a/@href').extract_first()
            link1 = f"https://ke.qq.com{link}"
            print(name, link1)
            if name:
                name = name
            else:
                name = " "
            if link1:
                link1 = link1
            else:
                link1 = " "
            data["name"] = name
            data["link1"] = link1
            yield data
        pass
