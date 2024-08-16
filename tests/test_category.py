from src.category import Category


def test_category_init(smartphones, tv_sets):
    """Testing categories' creation and counting."""
    assert smartphones.name == "Smartphones"
    assert smartphones.description == "Smartphones that make your life better"
    assert len(smartphones.products) == 2

    assert tv_sets.name == "TV sets"
    assert tv_sets.description == "Modern TVs that allow you to enjoy watching"
    assert len(tv_sets.products) == 1

    assert smartphones.categories_quantity == 2
    assert tv_sets.categories_quantity == 2
    assert Category.categories_quantity == 2

    assert smartphones.products_quantity == 3
    assert tv_sets.products_quantity == 3
    assert Category.products_quantity == 3
