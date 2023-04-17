# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from mySpiders.potMysql import Sql

class MyspidersPipeline:
    def process_item(self, item, spider):
        try:
            # Sql.create_table()
            Sql.insert_chinaz(item)
            pass
        except Exception as ex:
            print(ex.args)
        return item
