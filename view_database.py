import sqlite3

connection = sqlite3.connect("data/prices.db")

cursor = connection.cursor()

rows = cursor.execute("""
SELECT *
FROM price_history
ORDER BY timestamp DESC
""").fetchall()

print("\nPRICE HISTORY")
print("=" * 80)

for row in rows:
    print(row)

connection.close()