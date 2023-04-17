import scrapy


class ChinazSpider(scrapy.Spider):
    name = 'chinaz'  # 爬虫的识别名称
    allowed_domains = ['chinaz.com']  # 爬虫搜索的域名范围
    start_urls = ['https://top.chinaz.com/hangye/']  # 爬取的起始URL元组或者列表
    def parse(self, response):
        # 解析数据 直接用response.xpath()
        # 和之前的区别：1.不需要进行requesets请求（下载器已经做过了）
                    # 2.不需要转化文档树对象（内部已经实现）
        # 使用xpath获取数据类型：<class 'scrapy.selector.unified.SelectorList'>
        # extract（）使用此方法获取数据(数据类型是列表)
        # 列表取值：[0]  或者extract_first()
        li = response.xpath('//ul[@class="listCentent"]/li')
        for i in li:
            data = {}
            name = i.xpath('.//a/@title').extract_first()
            info = i.xpath('.//p[@class="RtCInfo"]/text()').extract_first()
            rank = i.xpath('.//strong[@class="col-red02"]/text()')
            print(name, info, rank)
            data['name'] = name
            data['info'] = info
            data['rank'] = rank
            # print(type(name))
            # 存储csv文件操作： 1.使用yield关键词 2.返回字典格式 3.运行命令
            # yield {
            #     '名字': name,
            #     '简介': info,
            #     '排名': rank
            # }
            yield data
        pass
