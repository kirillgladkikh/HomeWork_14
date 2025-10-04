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
def reset_counters():
    Category.total_categories = 0
    Category.total_products = 0


def test_category_setup():
    # Сбрасываем счётчики перед тестом
    reset_counters()

    # Создаём продукты
    product1 = Product(
        name="Product 1",
        description="Desc 1",
        price=100.0,
        quantity=10
    )

    product2 = Product(
        name="Product 2",
        description="Desc 2",
        price=200.0,
        quantity=20
    )

    # Создаём категорию
    category = Category(
        name="Test Category",
        description="Test description",
        products=[product1]
    )

    # Проверяем корректность создания
    assert category.name == "Test Category"
    assert category.description == "Test description"
    assert len(category._products) == 1
    assert Category.total_categories == 1
    assert Category.total_products == 1


def test_add_product():
    # Сбрасываем счётчики
    reset_counters()

    # Создаём продукты и категорию
    product1 = Product(
        name="Product 1",
        description="Desc 1",
        price=100.0,
        quantity=10
    )

    product2 = Product(
        name="Product 2",
        description="Desc 2",
        price=200.0,
        quantity=20
    )

    category = Category(
        name="Test Category",
        description="Test description",
        products=[product1]
    )

    # Добавляем продукт
    category.add_product(product2)
    assert len(category._products) == 2
    assert Category.total_products == 2


def test_total_categories():
    # Сбрасываем счётчики
    reset_counters()

    # Создаём первую категорию
    Category(
        name="Category 1",
        description="Desc 1"
    )

    # Создаём вторую категорию
    Category(
        name="Category 2",
        description="Desc 2"
    )

    assert Category.total_categories == 2


def test_total_products():
    # Сбрасываем счётчики
    reset_counters()

    # Создаём категорию с одним продуктом
    category = Category(
        name="Test Category",
        description="Test description",
        products=[
            Product(
                name="Product 1",
                description="Desc 1",
                price=100.0,
                quantity=10
            )
        ]
    )

    assert Category.total_products == 1

    # Добавляем второй продукт
    category.add_product(
        Product(
            name="Product 2",
            description="Desc 2",
            price=200.0,
            quantity=20
        )
    )

    assert Category.total_products == 2