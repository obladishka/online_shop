class Category:
    """Class for creating product categories."""
    name: str
    description: str
    products: list

    categories_quantity = 0
    products_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        self.categories_quantity += 1
        self.products_quantity += len(products)
