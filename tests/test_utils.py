from unittest.mock import patch

from src.utils import create_obj_from_json, read_json


@patch("src.utils.json.load")
@patch("src.utils.open")
def test_read_json(mock_open, mock_load, json_data):
    """Testing normal work of the func."""
    mock_load.return_value = json_data
    assert read_json("test.json") == json_data
    mock_open.assert_called_once_with("test.json", encoding="utf-8")


def test_create_obj_from_json(json_data, product_1, product_2):
    """Testing dynamic objects creation."""
    assert create_obj_from_json(json_data)[0].name == "Смартфоны"
    assert len(create_obj_from_json(json_data)[0].products) == 2

    assert create_obj_from_json(json_data)[0].products[0].name == product_1.name
    assert create_obj_from_json(json_data)[0].products[1].description == product_2.description
