from unittest.mock import patch

import pytest

from src.product import Product


def test_product_init(product_1, product_2):
    """Testing products' creation."""
    assert product_1.name == "Iphone 15"
    assert product_1.price == 210000.0

    assert product_2.description == "1024GB, Синий"
    assert product_2.quantity == 14


def test_product_init_zero_quantity():
    """Testing creation of a product with zero quantity."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)


def test_new_product(product_dict):
    """Testing normal work of new product creating method."""
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.quantity == 5


def test_new_product_existing_product_same_price(product_dict):
    """Testing method work when product already exists and there is no price conflict."""
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.quantity == 10


def test_new_product_existing_product_lower_price(product_dict):
    """Testing method work when product already exists and price is lower than current."""
    product_dict["price"] = 80000
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.price == 180000
    assert new_product.quantity == 15


def test_new_product_existing_product_higher_price(product_dict):
    """Testing method work when product already exists and price is higher than current."""
    product_dict["price"] = 200000
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.price == 200000
    assert new_product.quantity == 20


@pytest.mark.parametrize(
    "data",
    [
        {},
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
        },
        "Samsung Galaxy S23 Ultra",
    ],
)
def test_new_product_wrong_input_data(data):
    """Testing method work when the wrong data is transmitted."""
    assert Product.new_product(data) is None


def test_price(product_1):
    """Testing product's price return."""
    assert product_1.price == 210000.0


def test_price_setter(product_1):
    """Testing normal work of price setter."""
    assert product_1.price == 210000.0
    product_1.price = 220000.0
    assert product_1.price == 220000.0


def test_price_setter_wrong_price(product_1, capsys):
    """Testing work of price setter with a wrong price."""
    assert product_1.price == 210000.0
    product_1.price = -210000.0
    captured = capsys.readouterr()
    assert captured.out == "Price should not be zero or negative\n"
    product_1.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Price should not be zero or negative\n"
    assert product_1.price == 210000.0


@patch("builtins.input", return_value="y")
def test_price_setter_lower_price_confirmed(mock_input, product_1):
    """Testing work of price setter when price is lower than current and the operation is confirmed."""
    assert product_1.price == 210000.0
    product_1.price = 200000.0
    assert product_1.price == 200000.0


@patch("builtins.input", return_value="n")
def test_price_setter_lower_price_not_confirmed(mock_input, product_1):
    """Testing work of price setter when price is lower than current and the operation is not confirmed."""
    assert product_1.price == 210000.0
    product_1.price = 200000.0
    assert product_1.price == 210000.0


def test_product_str(product_1):
    """Testing product's information displaying."""
    assert str(product_1) == "Iphone 15, 210000 руб. Остаток: 8 шт."


def test_product_add(product_1, product_2):
    """Testing normal work of summation method."""
    assert product_1 + product_2 == 2114000.0


@pytest.mark.parametrize(
    "product2",
    [
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
        },
        "Samsung Galaxy S23 Ultra",
        210000.0,
        ("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ],
)
def test_product_add_wrong_type(product_1, product2):
    """Testing products' summation method when the second component is not a product."""
    with pytest.raises(TypeError) as ex:
        product_1 + product2
    assert str(ex.value) == "Only objects of Product class can be summed up."
