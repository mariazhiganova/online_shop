from tests.conftest import product_huawei


def test_product_1_init(product_iphone):
    assert product_iphone.name == 'iPhone 15 Pro Max'
    assert product_iphone.description == '1Tb'
    assert product_iphone.price == 200000
    assert product_iphone.quantity == 20

def test_product_2_init(product_huawei):
    assert product_huawei.name == 'Huawei 7S'
    assert product_huawei.description == '512Gb'
    assert product_huawei.price == 30000
    assert product_huawei.quantity == 14
