from src.categories_products import Product, Category

if __name__ == "__main__":
    # Создаем продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Проверяем геттер products
    print("Список товаров в категории:")
    print(category1.products)

    # Добавляем новый продукт
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("\nОбновленный список товаров:")
    print(category1.products)

    # Тестируем создание продукта через класс-метод
    new_product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    new_product = Product.new_product(new_product_data)

    # Возвращает строку: Название продукта, X руб. Остаток: X шт.
    product = Product("Смартфон", "Описание", 80, 15)
    print(product)  # Выведет: Смартфон, 80 руб. Остаток: 15 шт.


    # Количество продуктов считается из общего числа всех продуктов на складе.
    category = Category(
        "Электроника",  # название категории
        "Описание категории электроники",  # описание категории
        [  # список продуктов
            Product("Смартфон", "Описание смартфона", 80, 15),
            Product("Ноутбук", "Описание ноутбука", 100, 10)
        ]
    )

    print(f"\n{category}")  # Электроника, количество продуктов: 25 шт.

    # Вычисляет общую стоимость товаров как произведение цены на количество для каждого продукта

    product_a = Product("Товар А", "Описание", 100, 10)  # 100 * 10 = 1000
    product_b = Product("Товар B", "Описание", 200, 2)  # 200 * 2 = 400

    # Возвращает сумму этих произведений
    total_cost = product_a + product_b  # Вернёт 1400

    print(f"\nОбщая стоимость товаров: {total_cost}")
