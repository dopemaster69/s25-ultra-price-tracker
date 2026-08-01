import sqlite3
from pathlib import Path

DB_PATH = Path("data/prices.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS price_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        retailer TEXT NOT NULL,
        product TEXT NOT NULL,
        storage TEXT NOT NULL,
        price INTEGER NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_price(retailer, product, storage, price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO price_history
    (
        retailer,
        product,
        storage,
        price
    )
    VALUES (?, ?, ?, ?)
    """, (
        retailer,
        product,
        storage,
        price
    ))

    conn.commit()
    conn.close()