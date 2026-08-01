from selectolax.parser import HTMLParser

from src.models.price_result import PriceResult
from src.scrapers.base import BaseScraper


class AmazonScraper(BaseScraper):

    def scrape(self, url):

        html = self.fetch(url)

        tree = HTMLParser(html)

        # ---------- PRICE ----------
        price = None

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
                digits = "".join(ch for ch in node.text(strip=True) if ch.isdigit())

                if digits:
                    price = int(digits)
                    break

        # ---------- TITLE ----------
        title = ""

        title_node = tree.css_first("#productTitle")

        if title_node:
            title = title_node.text(strip=True)

        # ---------- STORAGE ----------
        storage = "Unknown"

        if "256" in title:
            storage = "256 GB"
        elif "512" in title:
            storage = "512 GB"
        elif "1TB" in title or "1 TB" in title:
            storage = "1 TB"

        # ---------- COLOUR ----------
        colour = "Unknown"

        colours = [
            "Titanium Black",
            "Titanium Gray",
            "Titanium Silverblue",
            "Titanium Whitesilver",
            "Titanium Jadegreen"
        ]

        for c in colours:
            if c.lower() in title.lower():
                colour = c
                break

        if price is None:
            return PriceResult(
                retailer="Amazon",
                title=title,
                storage=storage,
                colour=colour,
                price=None,
                url=url,
                success=False,
                error="Price not found"
            )

        return PriceResult(
            retailer="Amazon",
            title=title,
            storage=storage,
            colour=colour,
            price=price,
            url=url
        )