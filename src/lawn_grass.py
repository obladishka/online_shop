from src.product import Product


class LawnGrass(Product):
    """Class for creating lawn grass."""

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Lawn grass initialization. Parameters needed: grass name, description, price, quantity,
        country, germination_period and color."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
