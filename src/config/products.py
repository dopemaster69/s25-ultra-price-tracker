from src.models.product import Product

S25_ULTRA_256 = Product(
    name="Samsung Galaxy S25 Ultra",
    storage="256 GB",
    preferred_colour="Titanium Black",
    acceptable_colours=[
        "Titanium Black",
        "Titanium Gray",
        "Titanium Silverblue"
    ],
    urls={
        "amazon": "https://www.amazon.in/Samsung-Galaxy-Storage-Titanium-Silverblue/dp/B0DVC72DF8",
        "flipkart": "https://www.flipkart.com/samsung-galaxy-s25-ultra-5g-titanium-black-512-gb/p/itm09d676ceb930d"
    }
)