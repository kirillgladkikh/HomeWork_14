from typing import Dict, Optional


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Делаем атрибут цены приватным
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: Dict) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __str__(self) -> str:
        return (
            f"Товар: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Цена: {self.price} руб.\n"
            f"В наличии: {self.quantity} шт."
        )

    # Для класса Product добавить строковое отображение в следующем виде: Название продукта, 80 руб. Остаток: 15 шт.
    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    # Для класса Product переопределен магический метод сложения __add__, который принимает два аргумента:
    # self и второй объект.
    # Метод возвращает сумму произведений цены на количество у двух объектов.
    #
    # Для удобства работы с продуктами реализовать возможность их складывать.
    # Логика сложения должна работать так, чтобы в итоге у вас получалась полная стоимость всех товаров на складе.
    # Например, для товара А с ценой 100 рублей и количеством на складе 10 и товара B с ценой 200 рублей
    # и количеством на складе 2
    # результатом выполнения операции А + B должно стать значение, полученное из 100 × 10 + 200 × 2 = 1400.
    def __add__(self, other) -> float:
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Сложение возможно только между объектами класса Product")


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []  # Делаем атрибут приватным

        Category.total_categories += 1
        Category.total_products += len(self.__products)

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.total_products += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    # Tеперь каждый продукт имеет реализованное строковое отображение.
    # Геттер оптимизирован, преобразовав объект продукта в строку.
    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    # def __str__(self) -> str:
    #     return f"Категория: {self.name}\n" f"Описание: {self.description}\n" f"Товары в категории:\n{self.products}"

    # Добавляет метод __str__ в класс Category, который возвращает строку в указанном формате:
    # Название категории, количество продуктов: 200 шт.
    def __str__(self) -> str:
        # Подсчитываем общее количество товаров во всех продуктах категории
        total_quantity = sum(product.quantity for product in self.__products)
        # Формируем строку в требуемом формате
        return f"Категория: {self.name}, количество продуктов: {total_quantity} шт."
