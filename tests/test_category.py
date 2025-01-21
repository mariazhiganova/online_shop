from src.category import Category


def test_category_init(category_phone):
    assert category_phone.name == 'Смартфоны'
    assert category_phone.description == 'Умные телефоны'
    assert category_phone.products == ['iPhone 15 Pro Max', 'Huawei 7S']

    assert category_phone.category_count == 1
    assert category_phone.product_count  == 2
