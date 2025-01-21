class Category:
    """
    Класс для представления категорий товаров, подсчета их кол-ва, а также подсчета кол-ва товаров в каждой категории
    """

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
