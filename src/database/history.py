import sqlite3

DB_PATH = "data/prices.db"


def get_price_history():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            price,
            timestamp
        FROM price_history
        ORDER BY id ASC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "price": row["price"],
            "timestamp": row["timestamp"]
        }
        for row in rows
    ]