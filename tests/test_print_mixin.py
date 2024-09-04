from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin_product(capsys):
    """Testing information printing for product's creation."""
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    captured = capsys.readouterr()
    assert captured.out == "Product('Iphone 15', '512GB, Gray space', 210000.0, 8)\n"


def test_print_mixin_smartphone(capsys):
    """Testing information printing for smartphone's creation."""
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    captured = capsys.readouterr()
    assert captured.out == "Smartphone('Iphone 15', '512GB, Gray space', 210000.0, 8)\n"


def test_print_mixin_grass(capsys):
    """Testing information printing for loan grass's creation."""
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    captured = capsys.readouterr()
    assert captured.out == "LawnGrass('Газонная трава', 'Элитная трава для газона', 500.0, 20)\n"
