class Product:

    def __init__(
        self,
        name,
        storage,
        preferred_colour,
        acceptable_colours,
        urls
    ):
        self.name = name
        self.storage = storage
        self.preferred_colour = preferred_colour
        self.acceptable_colours = acceptable_colours
        self.urls = urls