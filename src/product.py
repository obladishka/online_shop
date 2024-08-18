class Product:
    """Class for creating products."""

    name: str
    description: str
    price: float
    quantity: int

    products = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.products.append(self)

    @classmethod
    def new_product(cls, product: dict):
        if sorted(product.keys()) == ["description", "name", "price", "quantity"]:
            if any(obj.name == product.get("name") for obj in cls.products):
                for obj in cls.products:
                    if product.get("name") == obj.name and product.get("price") > obj.price:
                        obj.price = product.get("price")
                        obj.quantity += product.get("quantity")
                    elif product.get("name") == obj.name:
                        obj.quantity += product.get("quantity")
            else:
                return cls(**product)
