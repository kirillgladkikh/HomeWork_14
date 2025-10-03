# Проект "Домашнее задание 14"

## Описание:

Проект "Домашнее задание 14" - это код на Python покрытый тестами (см. раздел "Тесты").

Реализованы:
 - Product и Category. 
 - подгрузка данных по категориями и товарам из файла JSON.

Содержит функции:

### модуль [categories_products.py](src%2Fcategories_products.py):

class Product - Класс для представления товара.
    :param name: название товара
    :param description: описание товара
    :param price: цена товара (может содержать дробную часть)
    :param quantity: количество товара в наличии

class Category - Класс для представления категории товаров.
    :param name: название категории
    :param description: описание категории
    :param products: список товаров в категории (по умолчанию пустой)

### модуль [load_data.py](src%2Fload_data.py):

load_data_from_json - Загружает данные из JSON файла и создает объекты категорий и товаров.
    :param file_path: путь к JSON файлу
    :return: список объектов категорий

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/kirillgladkikh/homework_14.git
```

2. Зависимости указаны в файле [pyproject.toml](pyproject.toml).

3. Для установки всех зависимостей из pyproject.toml используйте:
```
poetry install
```

## Использование:

1. Перейдите в файл [main.py](main.py).
2. Запустите файл [main.py](main.py).

## Тесты

для модуля [categories_products.py](src%2Fcategories_products.py):
- [test_category.py](tests%2Ftest_category.py)
- [test_product.py](tests%2Ftest_product.py)

## Исходные данные:

- [products.json](data%2Fproducts.json)

## Документация:

Настоящий файл [README.md](README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).