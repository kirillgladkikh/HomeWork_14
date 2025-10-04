import json
from unittest.mock import mock_open, patch

from src.categories_products import Category, Product
from src.load_data import load_data_from_json

# Подготавливаем тестовые данные
test_data = [
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
        ],
    },
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    },
]


def test_successful_load() -> None:
    # Создаем моковый файл с JSON данными
    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
        categories = load_data_from_json("test.json")

        # Проверяем количество категорий
        assert len(categories) == 2

        # Проверяем первую категорию
        smartphones = categories[0]
        assert isinstance(smartphones, Category)
        assert smartphones.name == "Смартфоны"
        assert (
            smartphones.description
            == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
        )

        # Проверяем количество товаров в первой категории
        assert len(smartphones.products) == 3

        # Проверяем первый товар в первой категории
        samsung = smartphones.products[0]
        assert isinstance(samsung, Product)
        assert samsung.name == "Samsung Galaxy C23 Ultra"
        assert samsung.description == "256GB, Серый цвет, 200MP камера"
        assert samsung.price == 180000.0
        assert samsung.quantity == 5

        # Проверяем второй товар в первой категории
        iphone = smartphones.products[1]
        assert isinstance(iphone, Product)
        assert iphone.name == "Iphone 15"
        assert iphone.price == 210000.0
        assert iphone.quantity == 8

        # Проверяем третий товар в первой категории
        xiaomi = smartphones.products[2]
        assert isinstance(xiaomi, Product)
        assert xiaomi.name == "Xiaomi Redmi Note 11"
        assert xiaomi.price == 31000.0
        assert xiaomi.quantity == 14

        # Проверяем вторую категорию
        tv = categories[1]
        assert isinstance(tv, Category)
        assert tv.name == "Телевизоры"
        assert (
            tv.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
        )

        # Проверяем товар во второй категории
        assert len(tv.products) == 1
        tv_product = tv.products[0]
        assert isinstance(tv_product, Product)
        assert tv_product.name == '55" QLED 4K'
        assert tv_product.price == 123000.0
        assert tv_product.quantity == 7


def test_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_data_from_json("non_existent_file.json")
        assert result == []


def test_invalid_json() -> None:
    with patch("builtins.open", mock_open(read_data="{invalid_json}")):
        result = load_data_from_json("invalid.json")
        assert result == []


def test_empty_file(capfd: object) -> None:
    with patch("builtins.open", mock_open(read_data="[]")):
        categories = load_data_from_json("empty.json")
        assert categories == []

        captured = capfd.readouterr()
        assert captured.out == ""
