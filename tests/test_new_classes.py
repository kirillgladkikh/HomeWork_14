from src.categories_products import LawnGrass, Smartphone

# Создаем тестовые объекты
smartphone1 = Smartphone(
    "iPhone 15", "Флагманский смартфон", 99999.99, 10, 95.0, "iPhone 15", 256, "Black"  # efficiency  # memory
)

smartphone2 = Smartphone("Samsung S24", "Премиум-смартфон", 129999.99, 5, 97.5, "S24", 512, "White")

grass1 = LawnGrass("Газонная трава премиум", "Элитная смесь семян", 500.0, 100, "Нидерланды", "14 дней", "Зеленый")

grass2 = LawnGrass("Газонная трава эконом", "Базовая смесь семян", 300.0, 200, "Россия", "21 день", "Темно-зеленый")


# Тестирование класса Smartphone
def test_smartphone_init() -> None:
    # Проверяем инициализацию смартфона
    assert smartphone1.name == "iPhone 15"
    assert smartphone1.description == "Флагманский смартфон"
    assert smartphone1.price == 99999.99
    assert smartphone1.quantity == 10
    assert smartphone1.efficiency == 95.0
    assert smartphone1.model == "iPhone 15"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Black"


def test_smartphone_str() -> None:
    expected_str = "iPhone 15, 99999.99 руб. Остаток: 10 шт."
    assert str(smartphone1) == expected_str


def test_smartphone_add() -> None:
    # Проверяем сложение смартфонов
    assert smartphone1 + smartphone2 == (99999.99 * 10 + 129999.99 * 5)

    # Проверяем ошибку при сложении с другим классом
    try:
        smartphone1 + grass1
    except TypeError as e:
        assert str(e) == "Сложение возможно только между объектами класса Product"


# Тестирование класса LawnGrass
def test_lawn_grass_init() -> None:
    # Проверяем инициализацию газонной травы
    assert grass1.name == "Газонная трава премиум"
    assert grass1.description == "Элитная смесь семян"
    assert grass1.price == 500.0
    assert grass1.quantity == 100
    assert grass1.country == "Нидерланды"
    assert grass1.germination_period == "14 дней"
    assert grass1.color == "Зеленый"


def test_lawn_grass_str() -> None:
    expected_str = "Газонная трава премиум, 500.0 руб. Остаток: 100 шт."
    assert str(grass1) == expected_str


def test_lawn_grass_add() -> None:
    # Проверяем сложение газонной травы
    assert grass1 + grass2 == (500.0 * 100 + 300.0 * 200)

    # Проверяем ошибку при сложении с другим классом
    try:
        grass1 + smartphone1
    except TypeError as e:
        assert str(e) == "Сложение возможно только между объектами класса Product"
