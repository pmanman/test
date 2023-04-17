import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TengSpider(CrawlSpider):
    name = 'tent'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001']

    rules = (
        Rule(LinkExtractor(allow=(r'/course/\d+',),unique = True),
             callback='parse_item',
             follow=True),
    )
    # 'https://ke.qq.com/course/341933'
    def parse_item(self, response): # 解析课程详情页
        name = response.xpath('//h3[@class="course-title"]/text()').extract_first()
        good = response.xpath('//span[@class="item-num"]/text()').extract_first()
        student = response.xpath('//span[@class="item-num"]/text()').extract()[-1]
        # print(name,good,student)
        yield {
            '课程名字': name,
            '课程好评率': good,
            '学生数': student
        }
        # return item
