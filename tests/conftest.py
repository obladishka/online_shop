import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_2():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def smartphones():
    return Category(
        "Smartphones",
        "Smartphones that make your life better",
        [
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def tv_sets():
    return Category(
        "TV sets",
        "Modern TVs that allow you to enjoy watching",
        [
            Product('55" QLED 4K', "Backlight", 210000.0, 8),
        ],
    )


@pytest.fixture
def json_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
    ]
