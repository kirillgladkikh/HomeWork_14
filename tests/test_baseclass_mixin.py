from src.categories_products import LawnGrass, Product, Smartphone


def test_logging_mixin_init() -> None:
    # Проверяем, что в консоль выведена корректная информация о создании
    # Для этого можно использовать mock для sys.stdout
    from unittest.mock import patch

    with patch("builtins.print") as mock_print:
        Product(name="Mock Product", description="Mock description", price=200.0, quantity=10)
        mock_print.assert_called_with("Product('Mock Product', 'Mock description', 200.0, 10)")


def test_logging_mixin_repr() -> None:
    product = Product(name="Test Product", description="Test description", price=100.0, quantity=5)

    # Проверяем корректность работы метода __repr__
    expected_repr = "Product('Test Product', 'Test description', 100.0, 5)"
    assert repr(product) == expected_repr


def test_logging_mixin_with_smartphone() -> None:
    # Проверяем работу миксина с наследником Smartphone
    smartphone = Smartphone(
        name="iPhone 15",
        description="Latest model",
        price=100000.0,
        quantity=3,
        efficiency=95.0,
        model="iPhone 15",
        memory=256,
        color="Black",
    )

    # Проверяем, что базовые атрибуты доступны
    assert smartphone.name == "iPhone 15"
    assert smartphone.description == "Latest model"
    assert smartphone.price == 100000.0
    assert smartphone.quantity == 3

    # Проверяем дополнительные атрибуты Smartphone
    assert smartphone.efficiency == 95.0
    assert smartphone.model == "iPhone 15"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"


def test_logging_mixin_with_lawn_grass() -> None:
    # Проверяем работу миксина с наследником LawnGrass
    lawn_grass = LawnGrass(
        name="Газонная трава",
        description="Высококачественная трава",
        price=500.0,
        quantity=100,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )

    # Проверяем базовые атрибуты
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Высококачественная трава"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 100

    # Проверяем дополнительные атрибуты LawnGrass
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "14 дней"
    assert lawn_grass.color == "Зеленый"
