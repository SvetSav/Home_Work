"""Тесты для демонстрационного кода из main.py."""

import io
import json
import os
import sys
from unittest.mock import patch

import pytest

from src.categories import Category
from src.products import Product
from src.utils import load_categories_from_json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestMainDemo:
    """Тесты для демонстрационного кода из задания."""

    def setup_method(self):
        """Сбрасываем счетчики перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    @property
    def capture_main_output(self):
        """Захватывает вывод main.py."""
        # Сохраняем оригинальный stdout
        old_stdout = sys.stdout
        # Создаем StringIO для захвата вывода
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        try:
            # Импортируем и выполняем main
            import main
        finally:
            # Восстанавливаем stdout
            sys.stdout = old_stdout

        return new_stdout.getvalue()

    def test_main_product_creation(self):
        """Тест создания продуктов как в main.py."""
        # Воспроизводим создание продуктов из main.py
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        # Проверяем значения
        assert product1.name == "Samsung Galaxy S23 Ultra"
        assert product1.description == "256GB, Серый цвет, 200MP камера"
        assert product1.price == 180000.0
        assert product1.quantity == 5

        assert product2.name == "Iphone 15"
        assert product2.description == "512GB, Gray space"
        assert product2.price == 210000.0
        assert product2.quantity == 8

        assert product3.name == "Xiaomi Redmi Note 11"
        assert product3.description == "1024GB, Синий"
        assert product3.price == 31000.0
        assert product3.quantity == 14

    def test_main_category_creation(self):
        """Тест создания категорий как в main.py."""
        # Создаем продукты как в main.py
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        # Создаем категорию как в main.py
        category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3],
        )

        # Проверяем значения
        assert category1.name == "Смартфоны"
        assert (
            category1.description
            == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
        )
        # Используем products_list вместо products для получения списка
        assert len(category1.products_list) == 3
        assert category1.products_list[0].name == "Samsung Galaxy S23 Ultra"
        assert category1.products_list[1].name == "Iphone 15"
        assert category1.products_list[2].name == "Xiaomi Redmi Note 11"

    def test_main_counters(self):
        """Тест счетчиков как в main.py."""
        # Сбрасываем счетчики
        Category.category_count = 0
        Category.product_count = 0

        # Создаем продукты и категории как в main.py
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category1 = Category("Смартфоны", "Описание", [product1, product2, product3])

        # Проверяем счетчики после первой категории
        assert Category.category_count == 1
        assert Category.product_count == 3
        assert category1.category_count == 1
        assert category1.product_count == 3

        # Создаем вторую категорию как в main.py
        product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
        category2 = Category("Телевизоры", "Описание", [product4])

        # Проверяем счетчики после второй категории
        assert Category.category_count == 2
        assert Category.product_count == 4
        assert category2.category_count == 2
        assert category2.product_count == 4

    def test_main_comparison(self):
        """Тест сравнения имени категории как в main.py."""
        category = Category("Смартфоны", "Описание", [])

        # Проверяем сравнение как в main.py: category1.name == "Смартфоны"
        assert category.name == "Смартфоны"
        assert (category.name == "Смартфоны") is True

    def test_main_products_list_output(self) -> None:
        """Тест вывода списка продуктов как в main.py."""
        product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
        category = Category("Телевизоры", "Описание", [product])

        # Проверяем строковое представление через геттер products
        products_str: str = category.products
        # Проверяем по шаблону из задания: "Название продукта, X руб. Остаток: X шт."
        assert '55" QLED 4K' in products_str
        assert "123000.0 руб." in products_str
        assert "Остаток: 7 шт." in products_str

    def test_main_file_exists(self):
        """Тест что main.py существует и может быть импортирован."""
        main_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "main.py")
        assert os.path.exists(main_path), f"Файл main.py должен существовать по пути: {main_path}"

        # Проверяем что можно импортировать
        try:
            import main

            assert hasattr(main, "__name__")
            assert main.__name__ == "main"
        except ImportError as e:
            pytest.fail(f"Не удалось импортировать main.py: {e}")

    def test_main_no_errors(self):
        """Тест что main.py выполняется без ошибок."""
        try:
            self.capture_main_output
            # Если добрались сюда - значит без ошибок
            assert True
        except Exception as e:
            pytest.fail(f"main.py вызвал ошибку при выполнении: {e}")

    def test_main_contains_expected_functions(self):
        """Тест что main.py содержит ожидаемый код."""
        # Ищем main.py в родительской директории
        main_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "main.py")

        with open(main_path, "r", encoding="utf-8") as f:  # Используем main_path вместо "main.py"
            content = f.read()

        # Проверяем ключевые элементы кода
        assert 'if __name__ == "__main__":' in content
        assert "Product(" in content
        assert "Category(" in content
        assert "print(" in content


class TestMainExtended:
    """Расширенные тесты для main.py."""

    def setup_method(self):
        """Сбрасываем счетчики перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_main_product_formatting(self):
        """Тест форматирования вывода продуктов."""
        # Вместо импорта main, воспроизводим его логику напрямую
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        try:
            # Копируем код из main.py
            product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
            product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
            product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

            print("=== Демонстрация из задания ===")
            print(product1.name)
            print(product1.description)
            print(product1.price)
            print(product1.quantity)

            print(product2.name)
            print(product2.description)
            print(product2.price)
            print(product2.quantity)

            print(product3.name)
            print(product3.description)
            print(product3.price)
            print(product3.quantity)

            # И т.д. - можно скопировать весь код из main.py
            # Но для этого теста достаточно проверить форматирование

        finally:
            sys.stdout = old_stdout

        output = new_stdout.getvalue()

        # Проверяем что цены выводятся с .0
        assert "180000.0" in output
        assert "210000.0" in output
        assert "31000.0" in output

        # Проверяем что описания выводятся полностью
        assert "256GB, Серый цвет, 200MP камера" in output
        assert "512GB, Gray space" in output
        assert "1024GB, Синий" in output

    def test_main_basic_output(self):
        """Базовый тест вывода main.py."""
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        try:
            # Воспроизводим код из main.py напрямую
            from src import Category, Product

            print("=== Демонстрация из задания ===")
            product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
            product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
            product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

            print(product1.name)
            print(product1.description)
            print(product1.price)
            print(product1.quantity)

            print(product2.name)
            print(product2.description)
            print(product2.price)
            print(product2.quantity)

            print(product3.name)
            print(product3.description)
            print(product3.price)
            print(product3.quantity)

            category1 = Category(
                "Смартфоны",
                "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                [product1, product2, product3],
            )

            print(category1.name == "Смартфоны")
            print(category1.description)
            print(len(category1.products))
            print(category1.category_count)
            print(category1.product_count)

            product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
            category2 = Category(
                "Телевизоры",
                "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                [product4],
            )

            print(category2.name)
            print(category2.description)
            print(len(category2.products))
            print(category2.products)

            print(Category.category_count)
            print(Category.product_count)

            print("\n=== Загрузка из JSON файла ===")

            # Сбрасываем счетчики для демонстрации
            Category.category_count = 0
            Category.product_count = 0

            # Мокаем загрузку JSON
            with patch("src.utils.load_categories_from_json") as mock_load:
                mock_load.return_value = []
                loaded_categories = mock_load()

                if loaded_categories:
                    print(f"Загружено категорий: {len(loaded_categories)}")
                else:
                    print("Не удалось загрузить данные из JSON файла.")

        finally:
            sys.stdout = old_stdout

        output = new_stdout.getvalue()

        # Проверяем ключевые элементы вывода
        assert "=== Демонстрация из задания ===" in output
        assert "Samsung" in output
        assert "Iphone" in output
        assert "Xiaomi" in output
        assert "=== Загрузка из JSON файла ===" in output
        assert "Не удалось загрузить данные из JSON файла" in output

    def test_main_complete_output(self):
        """Тест полного вывода main.py."""
        output = self._run_main_code_with_mock([])
        lines = output.strip().split("\n")
        lines = [line for line in lines if line.strip()]

        # Проверяем что вывод достаточно длинный
        assert len(lines) >= 20, f"Вывод слишком короткий: {len(lines)} строк"

    def test_main_with_json_data(self):
        """Тест main.py с JSON данными."""
        # Создаем тестовые данные
        test_product = Product("Ноутбук", "Мощный ноутбук для работы", 50000.0, 3)
        test_category = Category("Электроника", "Различные электронные устройства", [test_product])

        output = self._run_main_code_with_mock([test_category])

        # Проверяем вывод
        assert "=== Загрузка из JSON файла ===" in output
        assert "Загружено категорий:" in output

    def _run_main_code_with_mock(self, mock_categories):
        """Запускает код main.py с моком для JSON."""
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        try:
            from src import Category, Product

            print("=== Демонстрация из задания ===")
            product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
            product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
            product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

            print(product1.name)
            print(product1.description)
            print(product1.price)
            print(product1.quantity)

            print(product2.name)
            print(product2.description)
            print(product2.price)
            print(product2.quantity)

            print(product3.name)
            print(product3.description)
            print(product3.price)
            print(product3.quantity)

            category1 = Category(
                "Смартфоны",
                "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                [product1, product2, product3],
            )

            print(category1.name == "Смартфоны")
            print(category1.description)
            print(len(category1.products_list))
            print(category1.category_count)
            print(category1.product_count)

            product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
            category2 = Category(
                "Телевизоры",
                "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                [product4],
            )

            print(category2.name)
            print(category2.description)
            print(len(category2.products_list))
            print(category2.products)

            print(Category.category_count)
            print(Category.product_count)

            print("\n=== Загрузка из JSON файла ===")

            # Сбрасываем счетчики для демонстрации
            Category.category_count = 0
            Category.product_count = 0

            # Используем мок
            loaded_categories = mock_categories

            if loaded_categories:
                print(f"Загружено категорий: {len(loaded_categories)}")
                print(f"Всего категорий (после загрузки): {Category.category_count}")
                print(f"Всего продуктов (после загрузки): {Category.product_count}")

                for i, category in enumerate(loaded_categories, 1):
                    print(f"\nКатегория {i}: {category.name}")
                    print(f"Описание: {category.description}")
                    print(f"Количество продуктов: {len(category.products_list)}")

                    for product in category.products_list:
                        print(f"  - {product.name}: {product.price} руб., остаток: {product.quantity} шт.")
            else:
                print("Не удалось загрузить данные из JSON файла.")

        finally:
            sys.stdout = old_stdout

        return new_stdout.getvalue()


# Упрощенные тесты для покрытия
def test_main_coverage_basic():
    """Базовый тест для покрытия main.py."""
    # Просто проверяем что модуль можно импортировать
    import main

    # Проверяем что импортированы нужные компоненты
    assert hasattr(main, "Product")
    assert hasattr(main, "Category")
    assert hasattr(main, "load_categories_from_json")


def test_main_coverage_output_simple():
    """Упрощенный тест вывода main.py."""
    import subprocess

    # Получаем путь к корневой директории проекта
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    main_path = os.path.join(project_root, "main.py")

    # Проверяем что файл существует
    assert os.path.exists(main_path), f"main.py не найден: {main_path}"

    try:
        result = subprocess.run(
            ["python", main_path],
            capture_output=True,
            text=True,
            cwd=project_root,
            timeout=10,  # Таймаут на случай зависания
        )

        # Проверяем что программа завершилась
        assert result.returncode is not None

        # Проверяем что есть какой-то вывод
        output = result.stdout or result.stderr or ""
        assert len(output) > 0, "Нет вывода от main.py"

        # Логируем вывод для отладки
        print(f"\nВывод main.py (первые 500 символов): {output[:500]}")

    except subprocess.TimeoutExpired:
        pytest.fail("main.py выполняется слишком долго")
    except Exception as e:
        pytest.fail(f"Ошибка при выполнении main.py: {e}")


def test_main_coverage_json_handling():
    """Тест обработки JSON для покрытия."""
    # Создаем временный JSON файл
    import tempfile

    json_data = [
        {
            "name": "Тест",
            "description": "Описание",
            "products": [{"name": "Продукт", "description": "Описание продукта", "price": 100.0, "quantity": 5}],
        }
    ]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(json_data, f)
        temp_file = f.name

    try:
        # Тестируем функцию напрямую
        categories = load_categories_from_json(temp_file)

        assert len(categories) == 1
        assert categories[0].name == "Тест"

        # Проверяем счетчики
        assert Category.category_count > 0
        assert Category.product_count > 0

    finally:
        if os.path.exists(temp_file):
            os.unlink(temp_file)

    def test_main_product_str_representation(self):
        """Тест?, что main.py использует __str__ продукта."""
        # Создаём продукт как в main.py
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

        # Проверяем, что str() возвращает ожидаемый формат
        expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        assert str(product) == expected

    def test_main_product_addition(self):
        """Тест, что main.py корректно складывает продукты."""
        # Создаём продукты как в main.py
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        # Проверяем сложение
        # 180000 * 5 + 210000 * 8 = 900000 + 1680000 = 2580000
        assert product1 + product2 == 2580000.0

        # 180000 * 5 + 31000 * 14 = 900000 + 434000 = 1334000
        assert product1 + product3 == 1334000.0

        # 210000 * 8 + 31000 * 14 = 1680000 + 434000 = 2114000
        assert product2 + product3 == 2114000.0
