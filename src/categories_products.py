from typing import Optional, Dict

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
    def new_product(cls, product_data: Dict) -> 'Product':
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    def __str__(self) -> str:
        return (
            f"Товар: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Цена: {self.price} руб.\n"
            f"В наличии: {self.quantity} шт."
        )


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

    @property
    def products(self) -> str:
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
             for product in self.__products]
        )

    def __str__(self) -> str:
        return (
            f"Категория: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Товары в категории:\n{self.products}"
        )