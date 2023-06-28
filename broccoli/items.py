# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    barcode = scrapy.Field()
    quantity = scrapy.Field()
    brands = scrapy.Field()
    packages = scrapy.Field()
    categories = scrapy.Field()
    date = scrapy.Field()
