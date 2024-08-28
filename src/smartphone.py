from src.product import Product


class Smartphone(Product):
    """Class for creating smartphones."""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Smartphone initialization. Parameters needed: smartphone name, description, price, quantity,
        efficiency, model, memory and color."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
