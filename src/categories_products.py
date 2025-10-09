from abc import ABC, abstractmethod
from typing import Dict, Optional


# ДЗ 16.2

# Базовый класс:
# Создан базовый абстрактный класс с именем BaseProduct, который является родительским для классов продуктов.
# Классы «Смартфон» и «Трава газонная» наследуются только от класса Product.
# Выделена общая для каждого продукта функциональность и описана в абстрактном классе.

class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Защищенный атрибут
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной")
        self._price = value

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: Dict) -> "BaseProduct":
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        pass


class Product(BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)
        self._price = price  # Переопределяем для приватности

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        super().price = value

    @classmethod
    def new_product(cls, product_data: Dict) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

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
        if isinstance(other, Product) and type(self) is type(other):  # ДОБАВЛЕНО ОГРАНИЧЕНИЕ
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Сложение возможно только между объектами класса Product")

# ДЗ 16.1

# Созданы два класса наследников класса Product: «Смартфон» (Smartphone) и «Трава газонная» (LawnGrass).
# Класс «Смартфон» (Smartphone) расширен атрибутами:
# производительность (efficiency), модель (model), объем встроенной памяти (memory), цвет (color).
# Класс «Трава газонная» (LawnGrass) расширен атрибутами:
# страна-производитель (country), срок прорастания (germination_period), цвет (color).

# Новый класс Smartphone
class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


# Новый класс LawnGrass
class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
        if isinstance(product, Product):  # ДОБАВЛЕНО ПРОВЕРКА ТИПА
            self.__products.append(product)
            Category.total_products += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    # Tеперь каждый продукт имеет реализованное строковое отображение.
    # Геттер оптимизирован, преобразовав объект продукта в строку.

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    # Добавляет метод __str__ в класс Category, который возвращает строку в указанном формате:
    # Название категории, количество продуктов: 200 шт.

    def __str__(self) -> str:
        # Подсчитываем общее количество товаров во всех продуктах категории
        total_quantity = sum(product.quantity for product in self.__products)
        # Формируем строку в требуемом формате
        return f"Категория: {self.name}, количество продуктов: {total_quantity} шт."
