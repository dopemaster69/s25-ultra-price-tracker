from selectolax.parser import HTMLParser

from src.models.price_result import PriceResult
from src.scrapers.base import BaseScraper


class CromaScraper(BaseScraper):

    def scrape(self, url):

        html = self.fetch(url)

        tree = HTMLParser(html)

        selectors = [
            ".amount",
            ".new-price",
            "[class*='price']",
            "[data-testid='price']",
            ".cp-price"
        ]

        for selector in selectors:

            node = tree.css_first(selector)

            if node:

                text = node.text(strip=True)

                digits = "".join(ch for ch in text if ch.isdigit())

                if digits:
                    return PriceResult(
                        retailer="Croma",
                        price=int(digits),
                        url=url
                    )

        return PriceResult(
            retailer="Croma",
            price=None,
            url=url,
            success=False
        )