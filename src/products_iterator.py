from src.category import Category


class ProductIterator:
    """Class for iterating through products of a category."""

    category: Category

    def __init__(self, category):
        """Object initialization. Parameters needed: object of Category class."""
        if isinstance(category, Category):
            self.category = category

    def __iter__(self):
        """Method for iterator creation."""
        self.index = -1
        return self.category

    def __next__(self):
        """Method for iteration."""
        if self.index + 1 < len(self.category.products_list):
            self.index += 1
            return self.category.products_list[self.index]
        else:
            raise StopIteration
