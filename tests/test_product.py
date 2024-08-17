def test_product_init(product_1, product_2):
    """Testing products' creation."""
    assert product_1.name == "Iphone 15"
    assert product_1.price == 210000.0

    assert product_2.description == "1024GB, Синий"
    assert product_2.quantity == 14
