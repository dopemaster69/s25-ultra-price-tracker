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

    output = {
        "retailers": latest
    }

    with open("latest_prices.json", "w", encoding="utf-8") as file:

        json.dump(
            output,
            file,
            indent=4
        )

    print("✅ latest_prices.json generated")