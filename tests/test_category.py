from src.category import Category


def test_category_init(category_phone):
    assert category_phone.name == "Смартфоны"
    assert category_phone.description == "Умные телефоны"
    assert category_phone.products_in_list == ["iPhone 15 Pro Max", "Huawei 7S"]

    assert category_phone.category_count == 1
    assert category_phone.product_count == 2


def test_categories_str_property(product_iphone, product_huawei):
    category = Category("Смартфоны", "Описание", [product_iphone, product_huawei])
    assert category.products == (
        "iPhone 15 Pro Max, 200000 руб. Остаток: 20 шт.\n" "Huawei 7S, 30000 руб. Остаток: 14 шт.\n"
    )


def test_add_product(product_iphone, product_huawei):
    Category.product_count = 0
    Category.category_count = 0
    category = Category("Смартфоны", "Современные смартфоны", [product_iphone])

    assert category.product_count == 1
    assert category.category_count == 1

    category.add_product(product_huawei)

    assert category.product_count == 2
    assert category.category_count == 1

    assert product_huawei in category.products_in_list
    assert product_iphone in category.products_in_list
