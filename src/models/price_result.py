class PriceResult:

    def __init__(
        self,
        retailer,
        price,
        url,
        success=True
    ):
        self.retailer = retailer
        self.price = price
        self.url = url
        self.success = success