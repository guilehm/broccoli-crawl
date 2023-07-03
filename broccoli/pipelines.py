# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_URL"))
db = client["brocooli"]


class BroccoliPipeline:
    def process_item(self, item, spider):
        db[spider.name].insert_one(dict(item))
        return item
