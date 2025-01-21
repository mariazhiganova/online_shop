import json

from settings import JSON_PATH
from src.category import Category
from src.product import Product


def read_json(file_path: str) -> dict:
    """
    Функция, которая читает json-файл: принимает путь до файла и возвращает словарь с данными
    """
    with open(file_path, "r", encoding="UTF-8") as f:
        data = json.load(f)

    return data


def create_objects_from_json(data: dict):
    """
    Функция, которая принимает словарь с данными, создает объекты класса и возвращает их список.
    """
    categories = []
    for cat in data:
        products = []
        for product in cat["products"]:
            products.append(Product(**product))
        cat["products"] = products
        categories.append(Category(**cat))

    return categories


if __name__ == "__main__":
    raw_data = read_json(JSON_PATH)
    categories_data = create_objects_from_json(raw_data)
    print(categories_data)
