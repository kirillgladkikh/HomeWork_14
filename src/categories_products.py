from typing import Optional

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Класс для представления товара.

        :param name: название товара
        :param description: описание товара
        :param price: цена товара (может содержать дробную часть)
        :param quantity: количество товара в наличии
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return (
            f"Товар: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Цена: {self.price} руб.\n"
            f"В наличии: {self.quantity} шт."
        )


class Category:
    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None):
        """
        Класс для представления категории товаров.

        :param name: название категории
        :param description: описание категории
        :param products: список товаров в категории (по умолчанию пустой)
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def add_product(self, product: Product) -> None:
        """Добавить товар в категорию."""
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    def __str__(self) -> str:
        products_list = "\n".join([f"  - {product.name}" for product in self.products])
        return f"Категория: {self.name}\n" f"Описание: {self.description}\n" f"Товары в категории:\n{products_list}"
