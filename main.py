from src.database.db import initialize_database
from src.services.price_engine import PriceEngine


def main():

    initialize_database()

    engine = PriceEngine()

    url = input("Amazon URL: ")

    price = engine.collect_amazon_price(url)

    print(f"\nCurrent Price: ₹{price}")
    print("✅ Saved to database")


if __name__ == "__main__":
    main()