import scrapy

from scrapy import Request


class OpenFoodSpider(scrapy.Spider):
    name = "open_food"
    base_url = "https://world.openfoodfacts.org"
    start_urls = [base_url]

    def parse(self, response, **kwargs):
        products = response.xpath('//div[@id="search_results"]/ul[@class="products"]/li')
        links = products.xpath('./a/@href').getall()
        for link in links[:2]:
            yield Request(f"{self.base_url}{link}")
