from src.config.products import S25_ULTRA_256


def main():
    print("=" * 50)
    print("PROJECT ATLAS")
    print("=" * 50)

    print(f"Product : {S25_ULTRA_256.name}")
    print(f"Storage : {S25_ULTRA_256.storage}")
    print(f"Colour  : {S25_ULTRA_256.preferred_color}")

    print("\nRetailers:")

    for retailer in S25_ULTRA_256.urls:
        print(f"- {retailer}")


if __name__ == "__main__":
    main()