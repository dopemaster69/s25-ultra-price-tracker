import json

from src.database.db import get_connection


def export_latest_prices():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT retailer,
               product,
               storage,
               price,
               timestamp
        FROM price_history
        ORDER BY timestamp DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    latest = {}

    for retailer, product, storage, price, timestamp in rows:

        if retailer not in latest:

            latest[retailer] = {
                "product": product,
                "storage": storage,
                "price": price,
                "updated": timestamp
            }

    lowest_retailer = None
    lowest_price = None

    for retailer, info in latest.items():

        if lowest_price is None or info["price"] < lowest_price:

            lowest_price = info["price"]
            lowest_retailer = retailer

    output = {
        "generated_at": rows[0][4] if rows else None,
        "lowest_price": lowest_price,
        "lowest_retailer": lowest_retailer,
        "retailers": latest
    }

    with open("latest_prices.json", "w", encoding="utf-8") as file:

        json.dump(
            output,
            file,
            indent=4
        )

    print("✅ latest_prices.json generated")