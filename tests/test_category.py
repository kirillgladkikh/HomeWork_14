from typing import Optional, List
from src.categories_products import Category, Product


def test_category_init():
    # Тест 1: Создание категории без товаров
    category1 = Category("Электроника", "Электронные устройства")
    assert category1.name == "Электроника"
    assert category1.description == "Электронные устройства"
    assert category1.products == []
    assert Category.total_categories == 1
    assert Category.total_products == 0

    # Тест 2: Создание категории с товарами
    product1 = Product(
        name="Телефон",
        description="Смартфон последней модели",
        price=29999,
        quantity=10
    )

    category2 = Category("Электроника", "Электронные устройства")
    category2.add_product(product1)

    assert category2.products[0].name == "Телефон"
    assert category2.products[0].description == "Смартфон последней модели"
    assert category2.products[0].price == 29999
    assert category2.products[0].quantity == 10
    assert Category.total_categories == 2
    assert Category.total_products == 1

    # Тест 3: Проверка сброса счетчиков при создании новых категорий
    Category.total_categories = 0
    Category.total_products = 0
    category3 = Category("Бытовая техника", "Техника для дома")
    assert Category.total_categories == 1
    assert Category.total_products == 0


def test_category_count():
    # Очищаем счетчик перед тестом
    Category.total_categories = 0

    # Создаем несколько категорий для проверки подсчета
    Category("Категория 1", "Описание 1")
    Category("Категория 2", "Описание 2")
    Category("Категория 3", "Описание 3")

    # Проверяем общее количество категорий
    assert Category.total_categories == 3, f"Ожидалось 3, получено {Category.total_categories}"

    # Дополнительно проверяем, что счетчик сбрасывается корректно
    Category.total_categories = 0
    assert Category.total_categories == 0
