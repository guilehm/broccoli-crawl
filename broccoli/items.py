# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    barcode = scrapy.Field()
    quantity = scrapy.Field()
    brands = scrapy.Field()
    packaging = scrapy.Field()
    categories = scrapy.Field()
    date = scrapy.Field()
