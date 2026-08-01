from src.config.products import S25_ULTRA_256
from src.database.db import save_price
from src.scrapers.amazon import AmazonScraper


class PriceEngine:

    def __init__(self):

        self.product = S25_ULTRA_256

        self.scrapers = [
            (
                AmazonScraper(),
                self.product.urls["amazon"]
            )
        ]

    def collect_all(self):

        results = []

        for scraper, url in self.scrapers:

            result = scraper.scrape(url)

            if not result.success:
                results.append(result)
                continue

            # Validate storage
            if result.storage != self.product.storage:
                result.success = False
                result.error = (
                    f"Expected {self.product.storage}, "
                    f"found {result.storage}"
                )
                results.append(result)
                continue

            # Validate colour
            if result.colour not in self.product.acceptable_colours:
                result.success = False
                result.error = (
                    f"Unexpected colour: {result.colour}"
                )
                results.append(result)
                continue

            save_price(
                retailer=result.retailer,
                product=self.product.name,
                storage=result.storage,
                price=result.price
            )

            results.append(result)

        return results