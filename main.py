from src.database.db import initialize_database
from src.services.price_engine import PriceEngine


def main():

    initialize_database()

    engine = PriceEngine()

    url = input("Amazon URL: ")

    results = engine.collect_all(url)

    print()

    print("=" * 50)

    print("PRICE REPORT")

    print("=" * 50)

    for result in results:

        if result.success:
            print(f"{result.retailer:<15} ₹{result.price:,}")
        else:
            print(f"{result.retailer:<15} FAILED")


if __name__ == "__main__":
    main()