import re
import json

import scrapy


class OpenFoodSpider(scrapy.Spider):
    name = "open_food"
    start_urls = ["https://world.openfoodfacts.org/"]

    def parse(self, response, **kwargs):
        script_content = response.xpath(
            "//script[@type='text/javascript' and contains(text(), 'var products')]/text()"
        ).get("")

        data_pattern = r"var products = (.*?);"
        match = re.search(pattern=data_pattern, string=script_content)
        if not match:
            return

        products = json.loads(match.group(1))

        with open("./whatever.json", "w") as outfile:
            outfile.write(json.dumps(products))
