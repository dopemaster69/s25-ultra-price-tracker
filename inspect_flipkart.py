import requests

url = "https://www.flipkart.com/samsung-galaxy-s25-ultra-5g-titanium-black-512-gb/p/itm09d676ceb930d"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}

response = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("Status Code:", response.status_code)
print("Final URL:", response.url)

with open("flipkart.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Saved {len(response.text)} characters to flipkart.html")