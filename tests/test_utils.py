from unittest.mock import patch

from src.utils import read_json


@patch("src.utils.json.load")
@patch("src.utils.open")
def test_read_json(mock_open, mock_load, json_data):
    """Testing normal work of the func."""
    mock_load.return_value = json_data
    assert read_json("test.json") == json_data
    mock_open.assert_called_once_with("test.json", encoding="utf-8")
