from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Class for creating products."""

    name: str
    description: str
    price: float
    quantity: int

    products = []

    def __init__(self, name, description, price, quantity):
        """Product initialization. Parameters needed: product name, description, price and quantity."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.products.append(self)
        super().__repr__()

    def __str__(self):
        """Method for displaying info about a product."""
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Method for calculating total price of same products."""
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError(f"Only objects of {self.__class__.__name__} class can be summed up.")

    @classmethod
    def new_product(cls, product: dict):
        """Method for creating new products. If product already exists, its quantity increases by the quantity of
        a newly added product. In case of price conflict, the price is set on a level of a higher one."""

        if type(product) is dict and all(
            i in sorted(product.keys()) for i in ["description", "name", "price", "quantity"]
        ):

            if any(obj.name == product.get("name") for obj in cls.products):

                for obj in cls.products:
                    if product.get("name") == obj.name and product.get("price") > obj.price:
                        obj.price = product.get("price")
                        obj.quantity += product.get("quantity")
                        return obj
                    elif product.get("name") == obj.name:
                        obj.quantity += product.get("quantity")
                        return obj

            else:
                return cls(**product)

    @property
    def price(self):
        """Method for product price returning."""
        return self.__price

    @price.setter
    def price(self, price):
        """Method for setting new product price. In case the new price is lower than a current one,
        additional confirmation is needed."""

        if price <= 0:
            print("Price should not be zero or negative")

        elif price < self.__price:
            confirmation = input("Please confirm price decrease. For confirmation input 'y': ")
            if confirmation.lower().strip() == "y":
                self.__price = price

        else:
            self.__price = price
