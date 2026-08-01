from selectolax.parser import HTMLParser

from src.models.price_result import PriceResult
from src.scrapers.base import BaseScraper


class AmazonScraper(BaseScraper):

    def scrape(self, url):

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

                price = (
                    node.text(strip=True)
                        .replace(",", "")
                        .replace(".", "")
                )

                return PriceResult(
                    retailer="Amazon",
                    price=int(price),
                    url=url
                )

        return PriceResult(
            retailer="Amazon",
            price=None,
            url=url,
            success=False
        )