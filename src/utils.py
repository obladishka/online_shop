import json

from src.category import Category
from src.product import Product


def read_json(file_path: str) -> list[dict]:
    """Function for getting data from JSON-file."""
    with open(file_path, encoding="utf-8") as data_file:
        data = json.load(data_file)
    return data


def create_obj_from_json(data: list[dict]) -> list:
    """Function for automatic objects creation."""
    return [
        Category(
            name=category.get("name"),
            description=category.get("description"),
            products=[Product(**product) for product in category.get("products")],
        )
        for category in data
    ]
