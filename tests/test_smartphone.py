import pytest


def test_smartphone_init(smartphone_1, smartphone_2):
    """Testing smartphones' creation."""
    assert smartphone_1.name == "Iphone 15"
    assert smartphone_1.efficiency == 98.2
    assert smartphone_1.memory == 512

    assert smartphone_2.description == "1024GB, Синий"
    assert smartphone_2.model == "Note 11"
    assert smartphone_2.color == "Синий"


def test_smartphones_summation(smartphone_1, smartphone_2):
    """Testing normal work of summation method."""
    assert smartphone_1 + smartphone_2 == 2114000.0


@pytest.mark.parametrize("other", ["product_1", "grass_1"])
def test_smartphones_summation_wrong_type(smartphone_1, other):
    """Testing normal work of summation method."""
    with pytest.raises(TypeError) as ex:
        result = smartphone_1 + other
    assert str(ex.value) == "Only objects of Smartphone class can be summed up."
