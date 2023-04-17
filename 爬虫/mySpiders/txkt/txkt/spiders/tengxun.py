import scrapy


class TengxunSpider(scrapy.Spider):
    name = 'tengxun'

    allowed_domains = ['qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001']

    def parse(self, response):
        li = response.xpath('//div[@class="course-list"]/div')
        for i in li:
            name = i.xpath('.//h3[@class="kc-course-card-name"]/@title').extract_first()
            link = i.xpath('.//a[@class="kc-course-card js-report-link kc-list-course-card kc-course-card-column"]/@href').extract_first()
            print(name, 'https://ke.qq.com/' + link)
        pass