import scrapy
import json
from wangyi.items import WangyiItem

class WyyxSpider(scrapy.Spider):
    name = 'wyyx'
    allowed_domains = ['you.163.com']
    start_urls =['https://you.163.com/xhr/globalinfo//queryTop.json?__timestamp=1667807315922']

    def parse(self, response):
        i = WangyiItem()
        info = json.loads(response.text)
        message = info["data"]["cateList"]
        for i in message:
            cate1 = i["name"]
            tw = i["subCateGroupList"]
            for it in tw:
                cate2 = it['name']
                thr = it["categoryList"]
                for ite in thr:
                    cate3 = ite["name"]
                    i['cate1'] = cate1
                    i['cate2'] = cate2
                    i['cate3'] = cate3
                    yield i # 缩进问题
        pass
