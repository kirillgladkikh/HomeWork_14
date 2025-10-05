from src.categories_products import Product


def test_init() -> None:
    """Тест проверки корректности инициализации объекта"""
    product = Product(
        name="Смартфон", description="Современный смартфон с большим экраном", price=29999.99, quantity=10
    )

    # Проверяем, что все атрибуты установлены правильно
    assert product.name == "Смартфон", "Ошибка в имени продукта"
    assert product.description == "Современный смартфон с большим экраном", "Ошибка в описании"
    assert product.price == 29999.99, "Ошибка в цене"
    assert product.quantity == 10, "Ошибка в количестве"


def test_init_types() -> None:
    """Тест проверки типов данных при инициализации"""
    product = Product(
        name="Смартфон", description="Современный смартфон с большим экраном", price=29999.99, quantity=10
    )

    # Проверяем типы данных атрибутов
    assert isinstance(product.name, str), "Имя должно быть строкой"
    assert isinstance(product.description, str), "Описание должно быть строкой"
    assert isinstance(product.price, float), "Цена должна быть float"
    assert isinstance(product.quantity, int), "Количество должно быть целым числом"


def test_quantity() -> None:
    """Тест проверки количества товара"""
    # Проверяем начальное количество
    product = Product(
        name="Смартфон", description="Современный смартфон с большим экраном", price=29999.99, quantity=10
    )
    assert product.quantity == 10, "Ошибка в начальном количестве"


# Тестирование класса Product
def test_product_setup() -> None:
    # Создаем продукт внутри теста
    product = Product(name="Test Product", description="Test description", price=100.0, quantity=10)
    # Проверяем корректность создания
    assert product.name == "Test Product"
    assert product.description == "Test description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_price_getter() -> None:
    # Создаем продукт непосредственно в тесте
    product = Product(name="Test Product", description="Test description", price=100.0, quantity=10)
    assert product.price == 100.0


def test_price_setter_valid() -> None:
    product = Product(name="Test Product", description="Test description", price=100.0, quantity=10)
    product.price = 200.0
    assert product.price == 200.0


def test_price_setter_invalid() -> None:
    product = Product(name="Test Product", description="Test description", price=100.0, quantity=10)
    try:
        product.price = -10
    except Exception as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 100.0


def test_price_setter_zero() -> None:
    product = Product(name="Test Product", description="Test description", price=100.0, quantity=10)
    try:
        product.price = 0
    except Exception as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 100.0


def test_new_product_from_dict() -> None:
    product_data = {"name": "New Product", "description": "New description", "price": 50.0, "quantity": 5}
    new_product = Product.new_product(product_data)
    assert new_product.name == "New Product"
    assert new_product.price == 50.0
    assert new_product.quantity == 5


# Тесты для ДЗ 15.1 "Магические методы"
# Создаем тестовые объекты
product1 = Product("Смартфон", "Описание", 80, 15)
product2 = Product("Ноутбук", "Описание", 100, 10)


# Тестирование метода __str__
def test_str_method() -> None:
    # Проверяем первый продукт
    assert str(product1) == "Смартфон, 80 руб. Остаток: 15 шт."

    # Проверяем второй продукт
    assert str(product2) == "Ноутбук, 100 руб. Остаток: 10 шт."

    # Проверяем третий вариант
    product3 = Product("Планшет", "Описание", 50, 5)
    assert str(product3) == "Планшет, 50 руб. Остаток: 5 шт."


# Тестирование метода __add__
def test_add_method() -> None:
    # Проверяем сложение двух продуктов
    assert product1 + product2 == 80 * 15 + 100 * 10  # 1200 + 1000 = 2200

    # Проверяем сложение с самим собой
    assert product1 + product1 == 80 * 15 + 80 * 15  # 1200 + 1200 = 2400

    # Проверяем другой вариант
    assert product2 + product2 == 100 * 10 + 100 * 10  # 1000 + 1000 = 2000


# Тестирование обработки ошибок
def test_add_invalid_type() -> None:
    try:
        product1 + "строка"
    except TypeError as e:
        assert str(e) == "Сложение возможно только между объектами класса Product"

    try:
        product1 + 123
    except TypeError as e:
        assert str(e) == "Сложение возможно только между объектами класса Product"

    try:
        product1 + [1, 2, 3]
    except TypeError as e:
        assert str(e) == "Сложение возможно только между объектами класса Product"
