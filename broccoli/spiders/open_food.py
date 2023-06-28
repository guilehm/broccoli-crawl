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

        for link in links[:1]:
            yield Request(f"{self.base_url}{link}")

    def parse_product_detail(self, response):
        yield ProductItem(
            barcode=response.xpath('//*[@id="barcode_paragraph"]/span/text()').get(),
            quantity=response.xpath('//*[@id="field_quantity_value"]/text()').get(),
            brands=[{
                "href": brand.xpath('.//a[@itemprop="brand"]/@href').get(),
                "name": brand.xpath('.//a[@itemprop="brand"]/text()').get(),
            } for brand in response.xpath('//*[@id="field_brands"]')],
        )

    def parse(self, response, **kwargs):

        print("1", response.request.url == self.base_url)
        print("2", response.request.url.startswith(f"{self.base_url}/products/"))
        if response.request.url == self.base_url:
            return self.parse_product_list(response)
        if response.request.url.startswith(f"{self.base_url}/product/"):
            return self.parse_product_detail(response)
