from decimal import Decimal

import pytest

from src.categories_products import Category, Product


def test_category_init() -> None:
    # Тест 1: Создание категории без товаров
    category1 = Category("Электроника", "Электронные устройства")
    assert category1.name == "Электроника"
    assert category1.description == "Электронные устройства"

    # Проверяем, что список товаров пустой
    # Так как products возвращает строку, проверяем её длину
    assert category1.products == ""  # Пустая строка означает отсутствие товаров

    # Альтернативный вариант проверки через приватный атрибут
    # assert category1._products == []


def test_category_count() -> None:
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


# Тестирование класса Category
def reset_counters() -> None:
    Category.total_categories = 0
    Category.total_products = 0


def test_category_setup() -> None:
    # Сбрасываем счётчики перед тестом
    reset_counters()

    # Создаём продукты
    product1 = Product(name="Product 1", description="Desc 1", price=100.0, quantity=10)

    # Создаём категорию
    category = Category(name="Test Category", description="Test description", products=[product1])

    # Проверяем корректность создания
    assert category.name == "Test Category"
    assert category.description == "Test description"

    # Проверяем количество товаров через splitlines
    products_list = category.products.splitlines()
    assert len(products_list) == 1  # Теперь проверяем список строк

    assert Category.total_categories == 1
    assert Category.total_products == 1


def test_add_product() -> None:
    # Сбрасываем счётчики
    reset_counters()

    # Создаём продукты и категорию
    product1 = Product(name="Product 1", description="Desc 1", price=100.0, quantity=10)

    product2 = Product(name="Product 2", description="Desc 2", price=200.0, quantity=20)

    category = Category(name="Test Category", description="Test description", products=[product1])

    # Добавляем продукт
    category.add_product(product2)

    # Проверяем количество товаров через splitlines
    products_list = [line for line in category.products.splitlines() if line.strip()]
    assert len(products_list) == 2  # Теперь проверяем список строк

    assert Category.total_products == 2


def test_total_categories() -> None:
    # Сбрасываем счётчики
    reset_counters()

    # Создаём первую категорию
    Category(name="Category 1", description="Desc 1")

    # Создаём вторую категорию
    Category(name="Category 2", description="Desc 2")

    assert Category.total_categories == 2


def test_total_products() -> None:
    # Сбрасываем счётчики
    reset_counters()

    # Создаём категорию с одним продуктом
    category = Category(
        name="Test Category",
        description="Test description",
        products=[Product(name="Product 1", description="Desc 1", price=100.0, quantity=10)],
    )

    assert Category.total_products == 1

    # Добавляем второй продукт
    category.add_product(Product(name="Product 2", description="Desc 2", price=200.0, quantity=20))

    assert Category.total_products == 2


# Тесты для ДЗ 15.1 "Магические методы"

# Создаем тестовые объекты
product1 = Product("Смартфон", "Описание", 80, 15)
product2 = Product("Ноутбук", "Описание", 100, 10)
product3 = Product("Планшет", "Описание", 50, 5)

# Создаем категории для тестирования
category1 = Category("Электроника", "Описание категории", [product1, product2])

category2 = Category("Компьютеры", "Описание категории", [product2, product3])


# Тестирование геттера products
def test_products_getter() -> None:
    # Проверяем вывод списка продуктов
    expected_output = "Смартфон, 80 руб. Остаток: 15 шт.\n" "Ноутбук, 100 руб. Остаток: 10 шт."
    assert category1.products == expected_output

    # Проверяем другой вариант
    expected_output2 = "Ноутбук, 100 руб. Остаток: 10 шт.\n" "Планшет, 50 руб. Остаток: 5 шт."
    assert category2.products == expected_output2

    # Проверяем пустую категорию
    empty_category = Category("Пустая", "Описание")
    assert empty_category.products == ""


# Тесты для ДЗ 17.1:


# Создаем тестовые продукты один раз для всех тестов
@pytest.fixture
def product1():
    return Product(name="Продукт 1", description="Описание 1", price=100.0, quantity=1)


@pytest.fixture
def product2():
    return Product(name="Продукт 2", description="Описание 2", price=200.0, quantity=1)


@pytest.fixture
def product3():
    return Product(name="Продукт 3", description="Описание 3", price=300.0, quantity=1)


def test_middle_price_empty_category():
    """Тест для пустой категории"""
    category = Category(name="Тестовая категория", description="Описание")
    assert category.middle_price() == 0.0


def test_middle_price_single_product(product1):
    """Тест для категории с одним продуктом"""
    category = Category(name="Тестовая категория", description="Описание", products=[product1])
    assert category.middle_price() == Decimal("100.0")


def test_middle_price_multiple_products(product1, product2, product3):
    """Тест для категории с несколькими продуктами"""
    category = Category(name="Тестовая категория", description="Описание", products=[product1, product2, product3])
    expected_price = (100.0 + 200.0 + 300.0) / 3
    assert category.middle_price() == expected_price


def test_middle_price_with_zero_price(product1):
    """Тест для категории с продуктом с нулевой ценой"""
    zero_price_product = Product(name="Бесплатный продукт", description="Бесплатный", price=0.0, quantity=1)
    category = Category(name="Тестовая категория", description="Описание", products=[zero_price_product, product1])
    expected_price = (0.0 + 100.0) / 2
    assert category.middle_price() == expected_price


def test_middle_price_with_decimal_prices():
    """Тест для категории с ценами, содержащими десятичные дроби"""
    decimal_product1 = Product(name="Продукт 1", description="Описание", price=100.5, quantity=1)
    decimal_product2 = Product(name="Продукт 2", description="Описание", price=200.75, quantity=1)
    category = Category(
        name="Тестовая категория", description="Описание", products=[decimal_product1, decimal_product2]
    )
    expected_price = (100.5 + 200.75) / 2
    assert category.middle_price() == expected_price
