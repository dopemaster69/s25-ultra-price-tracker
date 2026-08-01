from src.scrapers.amazon import AmazonScraper
from src.database.db import save_price


class PriceEngine:

    def __init__(self):
        self.amazon = AmazonScraper()

    def collect_amazon_price(self, url):

        price = self.amazon.get_price(url)

        cleaned_price = (
            price.replace("₹", "")
                 .replace(",", "")
                 .replace(".", "")
                 .strip()
        )

        numeric_price = int(cleaned_price)

        save_price(
            retailer="Amazon",
            product="Samsung Galaxy S25 Ultra",
            storage="256 GB",
            price=numeric_price
        )

        return numeric_price