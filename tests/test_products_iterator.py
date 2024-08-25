import pytest


def test_products_iterator_init(products_iterator, smartphones):
    """Testing object's creation."""
    iterator = products_iterator
    assert iterator.category == smartphones


def test_products_iterator_index(products_iterator):
    """Testing correct index setting."""
    assert products_iterator.index == -1


def test_products_iterator(products_iterator):
    """Testing correct work of the iterator."""
    assert next(products_iterator).name == "Iphone 15"
    assert next(products_iterator).quantity == 14

    with pytest.raises(StopIteration):
        next(products_iterator)
