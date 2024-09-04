class PrintMixin:
    """Mixin-class for printing info about products' creation."""

    def __repr__(self):
        """Method for message creation and printing."""
        print(f"{self.__class__.__name__}{*[value for value in self.__dict__.values()], }")
