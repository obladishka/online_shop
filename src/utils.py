import json


def read_json(file_path: str) -> list[dict]:
    """Function for getting data from JSON-file."""
    with open(file_path, encoding="utf-8") as data_file:
        data = json.load(data_file)
    return data
