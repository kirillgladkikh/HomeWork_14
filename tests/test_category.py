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


# Тестирование метода __str__
def test_str_method() -> None:
    # Проверяем первую категорию
    assert str(category1) == "Категория: Электроника, количество продуктов: 25 шт."

    # Проверяем вторую категорию
    assert str(category2) == "Категория: Компьютеры, количество продуктов: 15 шт."

    # Проверяем категорию с одним продуктом
    single_product_category = Category("Аксессуары", "Описание", [product3])
    assert str(single_product_category) == "Категория: Аксессуары, количество продуктов: 5 шт."

    # Проверяем пустую категорию
    empty_category = Category("Пустая", "Описание")
    assert str(empty_category) == "Категория: Пустая, количество продуктов: 0 шт."
