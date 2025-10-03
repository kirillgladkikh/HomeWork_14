from src.categories_products import Product


def test_init():
    """ Тест проверки корректности инициализации объекта """
    product = Product(
        name="Смартфон",
        description="Современный смартфон с большим экраном",
        price=29999.99,
        quantity=10
    )

    # Проверяем, что все атрибуты установлены правильно
    assert product.name == "Смартфон", "Ошибка в имени продукта"
    assert product.description == "Современный смартфон с большим экраном", "Ошибка в описании"
    assert product.price == 29999.99, "Ошибка в цене"
    assert product.quantity == 10, "Ошибка в количестве"


def test_init_types():
    """ Тест проверки типов данных при инициализации """
    product = Product(
        name="Смартфон",
        description="Современный смартфон с большим экраном",
        price=29999.99,
        quantity=10
    )

    # Проверяем типы данных атрибутов
    assert isinstance(product.name, str), "Имя должно быть строкой"
    assert isinstance(product.description, str), "Описание должно быть строкой"
    assert isinstance(product.price, float), "Цена должна быть float"
    assert isinstance(product.quantity, int), "Количество должно быть целым числом"


def test_quantity():
    """ Тест проверки количества товара """
    # Проверяем начальное количество
    product = Product(
        name="Смартфон",
        description="Современный смартфон с большим экраном",
        price=29999.99,
        quantity=10
    )
    assert product.quantity == 10, "Ошибка в начальном количестве"
