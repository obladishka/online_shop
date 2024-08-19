from src.category import Category


def test_category_init(smartphones, tv_sets):
    """Testing categories' creation and counting."""
    assert smartphones.name == "Smartphones"
    assert smartphones.description == "Smartphones that make your life better"
    assert len(smartphones.products_list) == 2

    assert tv_sets.name == "TV sets"
    assert tv_sets.description == "Modern TVs that allow you to enjoy watching"
    assert len(tv_sets.products_list) == 1

    assert smartphones.category_count == 2
    assert tv_sets.category_count == 2
    assert Category.category_count == 2

    assert smartphones.product_count == 3
    assert tv_sets.product_count == 3
    assert Category.product_count == 3


def test_add_product(smartphones, product_1):
    """Testing normal work of new product adding method."""
    smartphones.add_product(product_1)
    assert len(smartphones.products_list) == 3
    assert smartphones.products_list[-1].name == product_1.name
    assert smartphones.products_list[-1].quantity == product_1.quantity

    assert smartphones.product_count == 6
    assert Category.product_count == 6


def test_add_product_wrong_type(smartphones):
    """Testing work of new product adding method when not a product is added (should not be added)."""
    smartphones.add_product("some_product")
    assert len(smartphones.products_list) == 2
    assert smartphones.products_list[-1].name == "Xiaomi Redmi Note 11"
    assert smartphones.products_list[-1].quantity == 14


def test_products(smartphones):
    """Testing displaying of products in the list."""
    assert smartphones.products == (
        "Iphone 15, 210000 RUB. Balance: 8 pcs.\n" "Xiaomi Redmi Note 11, 31000 RUB. Balance: 14 pcs."
    )


def test_products_list(tv_sets):
    """Testing return of products list."""
    assert type(tv_sets.products_list) is list
    assert len(tv_sets.products_list) == 1
    assert tv_sets.products_list[0].name == "55 QLED 4K"
