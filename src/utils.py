import json
from typing import List

from src.categories import Category
from src.products import Product


def load_categories_from_json(file_path: str = "products.json") -> List[Category]:
    """
    Загружает категории и продукты из JSON файла.

    Args:
        file_path: Путь к JSON файлу с данными

    Returns:
        List[Category]: Список объектов Category
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка при чтении JSON файла {file_path}.")
        return []

    categories = []

    for category_data in data:
        # Создаем продукты для категории
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)

        # Создаем категории
        category = Category(name=category_data["name"], description=category_data["description"], products=products)
        categories.append(category)

    return categories
