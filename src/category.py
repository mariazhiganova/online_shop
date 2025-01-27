from src.product import Product


class Category:
    """
    Класс для представления категорий товаров, подсчета их кол-ва, а также подсчета кол-ва товаров в каждой категории
    """

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products_in_list(self):
        return self.__products

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        prod_str = ""
        for product in self.__products:
            prod_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return prod_str
