import sqlite3

from pathlib import Path


DB_PATH = Path("data/prices.db")


class RecommendationEngine:

    def __init__(self):

        self.connection = sqlite3.connect(DB_PATH)

        self.connection.row_factory = sqlite3.Row

    def analyse(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT price,
                   timestamp
            FROM price_history
            ORDER BY timestamp ASC
            """
        )

        rows = cursor.fetchall()

        if not rows:

            return None

        prices = [row["price"] for row in rows]

        current = prices[-1]

        previous = prices[-2] if len(prices) > 1 else current

        lowest = min(prices)

        highest = max(prices)

        average = round(sum(prices) / len(prices))

        difference = current - previous

        percentage = 0

        if previous != 0:

            percentage = round((difference / previous) * 100, 2)

        if current == lowest:

            recommendation = "BUY NOW"

            confidence = 96

            reason = "Current price matches the lowest recorded price."

        elif current <= average:

            recommendation = "GOOD DEAL"

            confidence = 82

            reason = "Current price is below the historical average."

        else:

            recommendation = "WAIT"

            confidence = 71

            reason = "Current price is above the historical average."

        return {

            "current": current,

            "previous": previous,

            "lowest": lowest,

            "highest": highest,

            "average": average,

            "difference": difference,

            "percentage": percentage,

            "recommendation": recommendation,

            "confidence": confidence,

            "reason": reason

        }