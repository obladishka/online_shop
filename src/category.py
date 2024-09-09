from src.product import Product


class Category:
    """Class for creating product categories."""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Category initialization. Parameters needed: category name, description and products' list."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Method for displaying info about a category."""
        quantity = sum(product.quantity for product in self.products_list)
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, product: Product):
        """Method for new products adding. Only products of Product class can be added."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Only objects of Product class can be added.")

    @property
    def products(self):
        """Method for displaying products info in a string form."""
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self):
        """Method for returning products list in a list form."""
        return self.__products

    def middle_price(self):
        """Method for calculating average price for products in the list."""
        try:
            return round(sum(product.price for product in self.products_list) / self.product_count, 2)
        except ZeroDivisionError:
            return 0
