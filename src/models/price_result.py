class PriceResult:

    def __init__(
        self,
        retailer,
        title,
        storage,
        colour,
        price,
        url,
        success=True,
        error=None
    ):
        self.retailer = retailer
        self.title = title
        self.storage = storage
        self.colour = colour
        self.price = price
        self.url = url
        self.success = success
        self.error = error