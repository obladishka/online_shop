import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.products_iterator import ProductIterator
from src.smartphone import Smartphone


@pytest.fixture
def product_1():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_2():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def zero_quantity_product():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)


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
            Product("55 QLED 4K", "Backlight", 210000.0, 8),
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


@pytest.fixture
def product_dict():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def products_iterator(smartphones):
    return iter(ProductIterator(smartphones))


@pytest.fixture
def smartphone_1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone_2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
