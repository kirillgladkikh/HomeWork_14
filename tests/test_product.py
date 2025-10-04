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
# def test_product_setup():
#     product = Product(
#         name="Test Product",
#         description="Test description",
#         price=100.0,
#         quantity=10
#     )
#     return product
#
# def test_price_getter():
#     product = test_product_setup()
#     assert product.price == 100.0, "Тест не пройден: геттер цены работает некорректно"
#
# def test_price_setter_valid():
#     product = test_product_setup()
#     product.price = 200.0
#     assert product.price == 200.0, "Тест не пройден: валидная цена не установлена"
#
# def test_price_setter_invalid():
#     product = test_product_setup()
#     try:
#         product.price = -10
#     except Exception as e:
#         assert str(e) == "Цена не должна быть нулевая или отрицательная", "Тест не пройден: неверное сообщение об ошибке"
#     assert product.price == 100.0, "Тест не пройден: цена изменилась при недопустимом значении"
#
# def test_price_setter_zero():
#     product = test_product_setup()
#     try:
#         product.price = 0
#     except Exception as e:
#         assert str(e) == "Цена не должна быть нулевая или отрицательная", "Тест не пройден: неверное сообщение об ошибке"
#     assert product.price == 100.0, "Тест не пройден: цена изменилась при нулевом значении"
#
# def test_new_product_from_dict():
#     product_data = {
#         "name": "New Product",
#         "description": "New description",
#         "price": 50.0,
#         "quantity": 5
#     }
#     new_product = Product.new_product(product_data)
#     assert new_product.name == "New Product", "Тест не пройден: имя продукта не совпадает"
#     assert new_product.price == 50.0, "Тест не пройден: цена продукта не совпадает"
#     assert new_product.quantity == 5, "Тест не пройден: количество продукта не совпадает"

def test_product_setup():
    # Создаем продукт внутри теста
    product = Product(
        name="Test Product",
        description="Test description",
        price=100.0,
        quantity=10
    )
    # Проверяем корректность создания
    assert product.name == "Test Product"
    assert product.description == "Test description"
    assert product.price == 100.0
    assert product.quantity == 10

def test_price_getter():
    # Создаем продукт непосредственно в тесте
    product = Product(
        name="Test Product",
        description="Test description",
        price=100.0,
        quantity=10
    )
    assert product.price == 100.0

def test_price_setter_valid():
    product = Product(
        name="Test Product",
        description="Test description",
        price=100.0,
        quantity=10
    )
    product.price = 200.0
    assert product.price == 200.0

def test_price_setter_invalid():
    product = Product(
        name="Test Product",
        description="Test description",
        price=100.0,
        quantity=10
    )
    try:
        product.price = -10
    except Exception as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 100.0

def test_price_setter_zero():
    product = Product(
        name="Test Product",
        description="Test description",
        price=100.0,
        quantity=10
    )
    try:
        product.price = 0
    except Exception as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 100.0

def test_new_product_from_dict():
    product_data = {
        "name": "New Product",
        "description": "New description",
        "price": 50.0,
        "quantity": 5
    }
    new_product = Product.new_product(product_data)
    assert new_product.name == "New Product"
    assert new_product.price == 50.0
    assert new_product.quantity == 5
