import json
from typing import List
from src.categories_products import Category, Product


def load_data_from_json(file_path: str) -> List[Category]:
    """
    Загружает данные из JSON файла и создает объекты категорий и товаров.

    :param file_path: путь к JSON файлу
    :return: список объектов категорий
    """
    try:
        # Открываем и читаем JSON файл
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        categories = []

        # Проходим по каждой категории из JSON
        for category_data in data:
            # Создаем список товаров для текущей категории
            products = []
            for product_data in category_data["products"]:
                # Создаем объект Product
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products.append(product)

            # Создаем объект Category с загруженными товарами
            category = Category(
                name=category_data["name"], description=category_data["description"], products=products
            )
            categories.append(category)

        return categories

    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка: не удалось декодировать JSON файл")
        return []
    except Exception as e:
        print(f"Произошла ошибка при загрузке данных: {str(e)}")
        return []
