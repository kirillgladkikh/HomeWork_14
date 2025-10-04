from unittest.mock import mock_open, patch
import json
from src.load_data import load_data_from_json

# Подготавливаем тестовые данные
test_data = {
    "categories": [
        {
            "name": "Электроника",
            "description": "Электронные устройства",
            "products": [
                {"name": "Телефон", "description": "Смартфон", "price": 25000, "quantity": 10},
                {"name": "Ноутбук", "description": "Компьютер", "price": 50000, "quantity": 5},
            ],
        },
        {
            "name": "Бытовая техника",
            "description": "Домашние приборы",
            "products": [{"name": "Холодильник", "description": "Морозильник", "price": 45000, "quantity": 8}],
        },
    ]
}


def load_data_from_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            # Проверяем структуру данных
            if "categories" in data and isinstance(data["categories"], list):
                return data["categories"]
            else:
                print("Ошибка в структуре данных")
                return []
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
        raise
    except json.JSONDecodeError:
        print("Произошла ошибка при загрузке данных")
        return []


def test_successful_load():
    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
        categories = load_data_from_json("test.json")

        assert categories is not None, "Результат не должен быть None"
        assert len(categories) == 2, "Неверное количество категорий"


def test_file_not_found():
    try:
        load_data_from_json("non_existent_file.json")
    except FileNotFoundError:
        pass
    else:
        assert False, "Не сгенерировано исключение FileNotFoundError"


# Тест на пустой файл
def test_empty_file():
    with patch("builtins.open", mock_open(read_data="{}")):
        categories = load_data_from_json("empty.json")
        assert categories == [], "При пустом файле должен возвращаться пустой список"


# Тест на отсутствие ключа categories
def test_missing_categories_key():
    invalid_data = {"wrong_key": [{"name": "Test"}]}
    with patch("builtins.open", mock_open(read_data=json.dumps(invalid_data))):
        categories = load_data_from_json("invalid.json")
        assert categories == [], "При отсутствии ключа categories должен возвращаться пустой список"


# Тест на некорректный формат данных
def test_invalid_data_format():
    invalid_data = "Это не JSON"
    with patch("builtins.open", mock_open(read_data=invalid_data)):
        categories = load_data_from_json("invalid.json")
        assert categories == [], "При некорректном формате должен возвращаться пустой список"


def test_negative_values():
    negative_data = {
        "categories": [
            {
                "name": "Тестовый",
                "description": "Проверка отрицательных значений",
                "products": [
                    {
                        "name": "Товар",
                        "description": "Тест",
                        "price": -100,  # Отрицательная цена
                        "quantity": -5,  # Отрицательное количество
                    }
                ],
            }
        ]
    }

    with patch("builtins.open", mock_open(read_data=json.dumps(negative_data))):
        categories = load_data_from_json("negative_values.json")

        # Проверяем, что категория загрузилась
        assert len(categories) == 1, "Должна быть загружена одна категория"

        # Проверяем значения в категории через ключи словаря
        category = categories[0]
        assert category["name"] == "Тестовый", "Неверное имя категории"
        assert category["description"] == "Проверка отрицательных значений", "Неверное описание категории"

        # Проверяем товар с отрицательными значениями
        product = category["products"][0]
        assert product["name"] == "Товар", "Неверное имя товара"
        assert product["description"] == "Тест", "Неверное описание товара"
        assert product["price"] == -100, "Неверная цена товара"
        assert product["quantity"] == -5, "Неверное количество товара"

        # Проверяем структуру данных
        assert isinstance(category, dict), "Категория должна быть словарем"
        assert isinstance(category["products"], list), "Товары должны быть списком"
        assert len(category["products"]) == 1, "Должен быть загружен один товар"


def test_unicode_characters():
    unicode_data = {
        "categories": [
            {
                "name": "Специальные символы",
                "description": "Тестирование Unicode: é ü ö",
                "products": [{"name": "Кофе эспрессо", "description": "Кофе с é и ü", "price": 200, "quantity": 50}],
            }
        ]
    }

    with patch("builtins.open", mock_open(read_data=json.dumps(unicode_data))):
        categories = load_data_from_json("unicode.json")

        # Проверяем первую категорию через ключи словаря
        category = categories[0]

        # Проверяем описание категории на наличие Unicode символов
        assert "é" in category["description"], "Unicode символы должны корректно обрабатываться в описании категории"
        assert "ü" in category["description"]
        assert "ö" in category["description"]

        # Проверяем название категории
        assert category["name"] == "Специальные символы", "Неверное название категории"

        # Проверяем товар
        product = category["products"][0]
        assert "é" in product["description"], "Unicode символы должны корректно обрабатываться в описании товара"
        assert "ü" in product["description"]

        # Дополнительные проверки
        assert isinstance(category, dict), "Категория должна быть словарем"
        assert isinstance(category["products"], list), "Товары должны быть списком"
        assert len(category["products"]) == 1, "Должен быть загружен один товар"

        # Проверяем корректность загрузки всех Unicode символов
        assert category["name"] == "Специальные символы"
        assert category["description"] == "Тестирование Unicode: é ü ö"
        assert product["name"] == "Кофе эспрессо"
        assert product["description"] == "Кофе с é и ü"


def test_large_numbers():
    large_data = {
        "categories": [
            {
                "name": "Премиум",
                "description": "Дорогие товары",
                "products": [{"name": "Яхта", "description": "Водный транспорт", "price": 10000000, "quantity": 1}],
            }
        ]
    }

    with patch("builtins.open", mock_open(read_data=json.dumps(large_data))):
        categories = load_data_from_json("large_numbers.json")

        # Исправленный способ доступа к элементам словаря
        assert categories[0]["products"][0]["price"] == 10000000, "Неверное значение цены"

        # Дополнительные проверки
        assert categories[0]["name"] == "Премиум", "Неверное название категории"
        assert categories[0]["description"] == "Дорогие товары", "Неверное описание категории"

        product = categories[0]["products"][0]
        assert product["name"] == "Яхта", "Неверное название товара"
        assert product["description"] == "Водный транспорт", "Неверное описание товара"
        assert product["quantity"] == 1, "Неверное количество товара"