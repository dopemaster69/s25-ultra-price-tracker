from src.scrapers.amazon import AmazonScraper


def main():

    scraper = AmazonScraper()

    url = input("Amazon URL: ")

    price = scraper.get_price(url)

    print("\nCurrent Price")

    print(price)


if __name__ == "__main__":
    main()