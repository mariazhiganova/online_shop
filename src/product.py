class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """
        Выводит строковое отображение в заданном формате
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Складывает стоимость товаров определенной категории на складе
        """
        return (self.quantity * self.__price) + (other.quantity * other.__price)

    @property
    def price(self):
        """
        Геттер, возвращающий приватный атрибут
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер, позволяющий выяснить нужно ли менять цену и меняющий ее при необходимости
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            question = input(
                'Подтверждаете ли вы понижение стоимости? Если ДА введите "y", в противном случае введите "n".'
            )
            if question.lower() != "y":
                print("Вы отказались от изменения цены. Она останется прежней.")
            else:
                self.__price = new_price

    @classmethod
    def new_product(cls, prod_dict, products):
        """
        Класс-метод, принимающий параметры товара в списке и возвращающий созданный объект класса Product.
        """
        name = prod_dict.get("name")
        description = prod_dict.get("description")
        price = prod_dict.get("price")
        quantity = prod_dict.get("quantity")

        for product in products:
            if product.name == name:
                product.price = max(price, product.price)
                product.quantity += quantity
                return product

        new_prod = cls(name, description, price, quantity)
        products.append(new_prod)
        return new_prod
