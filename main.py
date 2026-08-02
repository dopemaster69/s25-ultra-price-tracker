from src.services.price_engine import PriceEngine
from src.exporters.json_exporter import export_latest_prices


def run_collection():

    engine = PriceEngine()

    results = engine.collect_all()

    export_latest_prices()

    return results


def main():

    results = run_collection()

    print()
    print("=" * 60)
    print("ATLAS")
    print("=" * 60)

    for result in results:

        if result.success:

            print(f"✓ {result.retailer}")
            print(f"Title    : {result.title}")
            print(f"Storage  : {result.storage}")
            print(f"Colour   : {result.colour}")
            print(f"Price    : ₹{result.price:,}")

        else:

            print(f"✗ {result.retailer}")
            print(f"Error    : {result.error}")

        print("-" * 60)

    print("\n✅ latest_prices.json generated")


if __name__ == "__main__":
    main()