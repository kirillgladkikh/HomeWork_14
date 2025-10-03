from src.categories_products import Category, Product
from src.load_data import load_data_from_json


# Загрузка данных из JSON
categories = load_data_from_json('data/products.json')

# Вывод информации о категориях и товарах
for category in categories:
    print(f'\n{category}')
    for product in category.products:
        print(f'\n{product}')

# Доступ к общей информации
print(f"\nВсего категорий: {Category.total_categories}")  # Выведет: 1
print(f"Всего товаров: {Category.total_products}")  # Выведет: 2
