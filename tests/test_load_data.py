import unittest
from unittest.mock import mock_open, patch
import json
from typing import List
from src.categories_products import Category, Product
from src.load_data import load_data_from_json

# Подготавливаем тестовые данные
# Правильная структура тестовых данных
test_data = {
    "categories": [
        {
            "name": "Электроника",
            "description": "Электронные устройства",
            "products": [
                {
                    "name": "Телефон",
                    "description": "Смартфон",
                    "price": 25000,
                    "quantity": 10
                },
                {
                    "name": "Ноутбук",
                    "description": "Компьютер",
                    "price": 50000,
                    "quantity": 5
                }
            ]
        },
        {
            "name": "Бытовая техника",
            "description": "Домашние приборы",
            "products": [
                {
                    "name": "Холодильник",
                    "description": "Морозильник",
                    "price": 45000,
                    "quantity": 8
                }
            ]
        }
    ]
}


def load_data_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Проверяем структуру данных
            if 'categories' in data and isinstance(data['categories'], list):
                return data['categories']
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
    invalid_data = {
        "wrong_key": [
            {"name": "Test"}
        ]
    }
    with patch("builtins.open", mock_open(read_data=json.dumps(invalid_data))):
        categories = load_data_from_json("invalid.json")
        assert categories == [], "При отсутствии ключа categories должен возвращаться пустой список"

# Тест на некорректный формат данных
def test_invalid_data_format():
    invalid_data = "Это не JSON"
    with patch("builtins.open", mock_open(read_data=invalid_data)):
        categories = load_data_from_json("invalid.json")
        assert categories == [], "При некорректном формате должен возвращаться пустой список"
