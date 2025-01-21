import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_iphone():
    return Product("iPhone 15 Pro Max", "1Tb", 200000, 20)


@pytest.fixture
def product_huawei():
    return Product("Huawei 7S", "512Gb", 30000, 14)


@pytest.fixture
def category_phone():
    return Category("Смартфоны", "Умные телефоны", ["iPhone 15 Pro Max", "Huawei 7S"])
