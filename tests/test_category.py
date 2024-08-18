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
