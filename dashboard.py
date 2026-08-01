import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ATLAS",
    page_icon="📱",
    layout="wide"
)

st.title("📱 ATLAS")
st.caption("Samsung Galaxy S25 Ultra Price Tracker")

# --------------------------
# DATABASE
# --------------------------

conn = sqlite3.connect("data/prices.db")

df = pd.read_sql_query("""
SELECT *
FROM price_history
ORDER BY timestamp ASC
""", conn)

conn.close()

if df.empty:
    st.warning("No price history found.")
    st.stop()

latest = df.iloc[-1]

# --------------------------
# TOP METRICS
# --------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Current Price",
    f"₹{latest['price']:,}"
)

col2.metric(
    "Lowest Price",
    f"₹{df['price'].min():,}"
)

col3.metric(
    "Highest Price",
    f"₹{df['price'].max():,}"
)

col4.metric(
    "Entries",
    len(df)
)

st.divider()

# --------------------------
# PRODUCT DETAILS
# --------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("Product")

    st.write(f"**Retailer:** {latest['retailer']}")
    st.write(f"**Product:** {latest['product']}")
    st.write(f"**Storage:** {latest['storage']}")

with right:

    st.subheader("Last Updated")

    st.write(latest["timestamp"])

st.divider()

# --------------------------
# PRICE HISTORY
# --------------------------

st.subheader("📈 Price History")

chart = df.set_index("timestamp")["price"]

st.line_chart(chart)

st.divider()

# --------------------------
# DATABASE TABLE
# --------------------------

st.subheader("Database")

st.dataframe(
    df.sort_values(
        "timestamp",
        ascending=False
    ),
    use_container_width=True
)