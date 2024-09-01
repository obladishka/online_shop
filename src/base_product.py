from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Abstract class for products."""

    @abstractmethod
    def __add__(self, other):
        """Method for calculating total price of products."""
        pass
