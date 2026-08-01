from src.scrapers.amazon import AmazonScraper
from src.database.db import save_price


class PriceEngine:

    def __init__(self):

        self.scrapers = [
            AmazonScraper()
        ]

    def collect_all(self, url):

        results = []

        for scraper in self.scrapers:

            result = scraper.scrape(url)

            results.append(result)

            if result.success:

                save_price(
                    retailer=result.retailer,
                    product="Samsung Galaxy S25 Ultra",
                    storage="256 GB",
                    price=result.price
                )

        return results