from src.exceptions import ZeroQuantityError
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

    def __str__(self):
        full_count = 0
        for product in self.__products:
            full_count += product.quantity
        return f"{self.name}, количество продуктов: {full_count} шт."

    @property
    def products_in_list(self):
        """
        Геттер, возвращающий приватный атрибут
        """
        return self.__products

    def add_product(self, product):
        """
        Метод, добавляющий продукт в список и увеличивающий счетчик кол-ва продуктов.
        """
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityError('Невозможно добавить товар с нулевым количеством')

            except ZeroQuantityError as er:
                print(str(er))

            else:
                self.__products.append(product)
                Category.product_count += 1
                print('Товар добавлен успешно')

            finally:
                print('Обработка добавления товара завершена')

        else:
            raise TypeError

    @property
    def products(self):
        """
        Геттер, который выводит список товаров в виде строк.
        """
        prod_str = ""
        for product in self.__products:
            prod_str += f"{str(product)}"
        return prod_str

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products))

        except ZeroDivisionError:
            return 0
