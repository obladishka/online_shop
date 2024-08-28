import pytest


def test_lawn_grass_init(grass_1, grass_2):
    """Testing smartphones' creation."""
    assert grass_1.name == "Газонная трава"
    assert grass_1.country == "Россия"
    assert grass_1.germination_period == "7 дней"

    assert grass_2.description == "Выносливая трава"
    assert grass_2.quantity == 15
    assert grass_2.color == "Темно-зеленый"


def test_smartphones_summation(grass_1, grass_2):
    """Testing normal work of summation method."""
    assert grass_1 + grass_2 == 16750.0


@pytest.mark.parametrize("other", ["product_1", "smartphone_1"])
def test_smartphones_summation_wrong_type(grass_1, other):
    """Testing summation method with different product types."""
    with pytest.raises(TypeError) as ex:
        grass_1 + other
    assert str(ex.value) == "Only objects of LawnGrass class can be summed up."
