import json
import os
import tempfile

from src.categories import Category
from src.utils import load_categories_from_json


class TestJsonLoader:
    """Тесты для загрузки данных из JSON."""

    def setup_method(self):
        """Сбрасываем счетчики перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def create_test_json_file(self, data):
        """Создает временный JSON файл для тестирования."""
        temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8")
        json.dump(data, temp_file, ensure_ascii=False, indent=2)
        temp_file.close()
        return temp_file.name

    def test_load_categories_from_valid_json(self):
        """Тест загрузки из корректного JSON файла."""
        test_data = [
            {
                "name": "Тестовая категория",
                "description": "Описание тестовой категории",
                "products": [
                    {
                        "name": "Тестовый продукт 1",
                        "description": "Описание тестового продукта 1",
                        "price": 1000.0,
                        "quantity": 10,
                    },
                    {
                        "name": "Тестовый продукт 2",
                        "description": "Описание тестового продукта 2",
                        "price": 2000.0,
                        "quantity": 5,
                    },
                ],
            }
        ]

        # Создаем временный файл
        temp_file_path = self.create_test_json_file(test_data)

        try:
            # Загружаем данные
            categories = load_categories_from_json(temp_file_path)

            # Проверяем результаты
            assert len(categories) == 1
            assert Category.category_count == 1
            assert Category.product_count == 2

            category = categories[0]
            assert category.name == "Тестовая категория"
            assert category.description == "Описание тестовой категории"
            assert len(category.products) == 2

            # Проверяем продукты
            product1 = category.products[0]
            assert product1.name == "Тестовый продукт 1"
            assert product1.price == 1000.0
            assert product1.quantity == 10

            product2 = category.products[1]
            assert product2.name == "Тестовый продукт 2"
            assert product2.price == 2000.0
            assert product2.quantity == 5

        finally:
            # Удаляем временный файл
            os.unlink(temp_file_path)

    def test_load_categories_from_nonexistent_file(self):
        """Тест загрузки из несуществующего файла."""
        categories = load_categories_from_json("nonexistent_file.json")
        assert categories == []
        assert Category.category_count == 0
        assert Category.product_count == 0

    def test_load_categories_from_invalid_json(self):
        """Тест загрузки из некорректного JSON файла."""
        # Создаем файл с некорректным JSON
        temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8")
        temp_file.write("{invalid json")
        temp_file.close()

        try:
            categories = load_categories_from_json(temp_file.name)
            assert categories == []
            assert Category.category_count == 0
            assert Category.product_count == 0
        finally:
            os.unlink(temp_file.name)

    def test_load_categories_with_empty_products(self):
        """Тест загрузки категории без продуктов."""
        test_data = [{"name": "Пустая категория", "description": "Категория без продуктов", "products": []}]

        temp_file_path = self.create_test_json_file(test_data)

        try:
            categories = load_categories_from_json(temp_file_path)

            assert len(categories) == 1
            assert Category.category_count == 1
            assert Category.product_count == 0

            category = categories[0]
            assert category.name == "Пустая категория"
            assert len(category.products) == 0

        finally:
            os.unlink(temp_file_path)

    def test_load_multiple_categories_from_json(self):
        """Тест загрузки нескольких категорий из JSON."""
        test_data = [
            {
                "name": "Категория 1",
                "description": "Описание 1",
                "products": [
                    {"name": "Продукт 1", "description": "Описание продукта 1", "price": 100.0, "quantity": 1}
                ],
            },
            {
                "name": "Категория 2",
                "description": "Описание 2",
                "products": [
                    {"name": "Продукт 2", "description": "Описание продукта 2", "price": 200.0, "quantity": 2},
                    {"name": "Продукт 3", "description": "Описание продукта 3", "price": 300.0, "quantity": 3},
                ],
            },
        ]

        temp_file_path = self.create_test_json_file(test_data)

        try:
            categories = load_categories_from_json(temp_file_path)

            assert len(categories) == 2
            assert Category.category_count == 2
            assert Category.product_count == 3  # 1 + 2 = 3

            # Проверяем первую категорию
            assert categories[0].name == "Категория 1"
            assert len(categories[0].products) == 1

            # Проверяем вторую категорию
            assert categories[1].name == "Категория 2"
            assert len(categories[1].products) == 2

        finally:
            os.unlink(temp_file_path)
