import scrapy
import json
from dfcf.items import DfcfItem

class DongfangSpider(scrapy.Spider):
    name = 'dongfang'
    allowed_domains = ['fund.eastmoney.com']
    start_urls = [
        f'http://fund.eastmoney.com/data/rankhandler.aspx?op=dy&dt=kf&ft=all&rs=&gs=0&sc=qjzf&st=desc&sd=2021-11-04&ed=2022-11-04&es=0&qdii=&pi={k}&pn=50&dx=0&v=0.48317388996328847' for k in range(1,5)]

    def parse(self, response):
        info = response.text
        res = info.split('var rankData = ')[1].split(',allRecords')[0] + '}'
        page = res.replace('datas', '"datas"')
        data = json.loads(page)
        datas = data['datas']
        for k in datas:
            item = DfcfItem()
            a = k.split(',')  # 得到一个列表
            # li.pop(2) # 不能边循环边删除
            # li.pop(12)
            # a = li[:14]
            item['entrance'] = a[0]  # 基金代码
            item['drink'] = a[1]  # 名字
            item["possible"] = a[2]
            item['painting'] = a[3]
            item['suggestion'] = a[4]
            item['boil'] = a[5]
            item['intrude'] = a[6]
            item['leg'] = a[7]
            item['excuse'] = a[8]
            # if a[9]:
            item['appointment'] = a[9]
            # # else:
            # #     item['appointment'] = ''
            item['science'] = a[10]
            item['invented'] = a[11]
            item['cat'] = a[12]
            item['dog'] = a[13]
            yield item
        pass
