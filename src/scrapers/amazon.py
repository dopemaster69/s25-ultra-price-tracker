from selectolax.parser import HTMLParser
from src.scrapers.base import BaseScraper


class AmazonScraper(BaseScraper):

    def get_price(self, url):

        html = self.fetch(url)

        tree = HTMLParser(html)

        selectors = [
            "#corePrice_feature_div .a-price-whole",
            ".a-price-whole",
            "#priceblock_ourprice",
            "#priceblock_dealprice",
            ".apexPriceToPay .a-price-whole",
        ]

        for selector in selectors:

            node = tree.css_first(selector)

            if node:
                return node.text(strip=True)

        return None