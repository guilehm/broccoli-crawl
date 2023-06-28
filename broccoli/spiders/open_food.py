import json
from datetime import datetime

import scrapy
from scrapy import Request

from broccoli.items import ProductItem


class OpenFoodSpider(scrapy.Spider):
    name = "open_food"
    base_url = "https://world.openfoodfacts.org"
    start_urls = [base_url]

    def parse_product_list(self, response):
        products = response.xpath('//div[@id="search_results"]/ul[@class="products"]/li')
        links = products.xpath('./a/@href').getall()

        self.logger.info(f"found {len(links)} products")

        for link in links:
            yield Request(f"{self.base_url}{link}")

    def parse_product_detail(self, response):
        yield ProductItem(
            name=response.xpath('//*[@id="field_generic_name_value"]/span/text()').get(),
            url=response.request.url,
            barcode=response.xpath('//*[@id="barcode_paragraph"]/span/text()').get(),
            quantity=response.xpath('//*[@id="field_quantity_value"]/text()').get(),
            brands=[{
                "href": brand.xpath('./@href').get(),
                "name": brand.xpath('./text()').get(),
            } for brand in response.xpath('//*[@id="field_brands_value"]/a[@itemprop="brand"]')],
            packaging=[{
                "href": brand.xpath('./@href').get(),
                "name": brand.xpath('./text()').get(),
            } for brand in response.xpath('//*[@id="field_packaging_value"]/a[@class="tag well_known"]')],
            categories=[{
                "href": brand.xpath('./@href').get(),
                "name": brand.xpath('./text()').get(),
            } for brand in response.xpath('//*[@id="field_categories_value"]/a[@class="tag well_known"]')],
            date=datetime.now().isoformat(),
        )

    def parse(self, response, **kwargs):
        if response.request.url == self.base_url:
            return self.parse_product_list(response)
        if response.request.url.startswith(f"{self.base_url}/product/"):
            return self.parse_product_detail(response)
