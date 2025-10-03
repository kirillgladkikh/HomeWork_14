from src.categories_products import Category, Product

if __name__ == "__main__":
    # Создаем товары
    product1 = Product(
        name="Смартфон Apple iPhone 15",
        description="Современный смартфон с большим экраном",
        price=99999.99,
        quantity=10,
    )

    product2 = Product(
        name="Ноутбук MacBook Air", description="Легкий и производительный ноутбук", price=129999.99, quantity=5
    )

    # Создаем категорию
    electronics = Category(name="Электроника", description="Категория электронных устройств")

    # Добавляем товары в категорию
    electronics.add_product(product1)
    electronics.add_product(product2)

    # Выводим информацию
    print(electronics)
    print("\nИнформация о товаре:")
    print(product1)
    print("\nИнформация о товаре:")
    print(product2)
