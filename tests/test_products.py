import io
import sys

import pytest

from src.products import Product


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self):
        """Тест инициализации продуктов"""
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        assert product1.name == "Samsung Galaxy S23 Ultra"
        assert product1.description == "256GB, Серый цвет, 200MP камера"
        assert product1.price == 180000.0  # Используем геттер
        assert product1.quantity == 5

        assert product2.name == "Iphone 15"
        assert product2.description == "512GB, Gray space"
        assert product2.price == 210000.0
        assert product2.quantity == 8

        assert product3.name == "Xiaomi Redmi Note 11"
        assert product3.description == "1024GB, Синий"
        assert product3.price == 31000.0
        assert product3.quantity == 14

    def test_new_product_class_method(self):
        """Тест класс-метода new_product."""
        product_data = {
            "name": "Новый продукт",
            "description": "Описание нового продукта",
            "price": 15000.0,
            "quantity": 10,
        }

        product = Product.new_product(product_data)

        assert isinstance(product, Product)
        assert product.name == "Новый продукт"
        assert product.description == "Описание нового продукта"
        assert product.price == 15000.0
        assert product.quantity == 10

    def test_price_getter(self):
        """Тест геттера цены."""
        product = Product("Тест", "Описание", 1000.0, 5)

        # Проверяем что геттер работает
        assert product.price == 1000.0
        assert product._price == 1000.0  # Проверяем приватный атрибут

    def test_price_setter_valid(self):
        """Тест сеттера цены с корректным значением."""
        product = Product("Тест", "Описание", 1000.0, 5)

        # Меняем цену на корректное значение
        product.price = 1500.0

        assert product.price == 1500.0
        assert product._price == 1500.0

    def test_price_setter_invalid_zero(self):
        """Тест сеттера цены с нулевым значением."""
        product = Product("Тест", "Описание", 1000.0, 5)

        # Перехватываем вывод
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Пытаемся установить нулевую цену
        product.price = 0

        sys.stdout = sys.__stdout__

        # Проверяем что цена не изменилась
        assert product.price == 1000.0
        # Проверяем что сообщение выведено
        assert "Цена не должна быть нулевая или отрицательная" in captured_output.getvalue()

    def test_price_setter_invalid_negative(self):
        """Тест сеттера цены с отрицательным значением."""
        product = Product("Тест", "Описание", 1000.0, 5)

        # Перехватываем вывод
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Пытаемся установить отрицательную цену
        product.price = -100

        sys.stdout = sys.__stdout__

        # Проверяем что цена не изменилась
        assert product.price == 1000.0
        # Проверяем что сообщение выведено
        assert "Цена не должна быть нулевая или отрицательная" in captured_output.getvalue()

    def test_initialization_with_negative_price(self):
        """Тест инициализации с отрицательной ценой."""
        # При инициализации с отрицательной ценой, цена должна стать 0
        product = Product("Тест", "Описание", -100.0, 5)

        assert product.price == 0.0
        assert product._price == 0.0

    def test_product_str_method(self):
        """Тест строкового представления продукта (__str__)."""
        product = Product("iPhone 15", "Смартфон Apple", 120000.0, 10)

        expected_str = "iPhone 15, 120000.0 руб. Остаток: 10 шт."
        assert str(product) == expected_str

        product2 = Product("MacBook Pro", "Ноутбук Apple", 250000.0, 3)
        expected_str2 = "MacBook Pro, 250000.0 руб. Остаток: 3 шт."
        assert str(product2) == expected_str2

    def test_product_add_method(self):
        """Тест магического метода сложения продуктов (__add__)."""
        product1 = Product("Товар A", "Описание A", 100.0, 10)
        product2 = Product("Товар B", "Описание B", 200.0, 2)

        # 100 * 10 + 200 * 2 = 1000 + 400 = 1400
        assert product1 + product2 == 1400.0

        product3 = Product("Товар C", "Описание C", 50.0, 5)
        product4 = Product("Товар D", "Описание D", 30.0, 3)

        # 50 * 5 + 30 * 3 = 250 + 90 = 340
        assert product3 + product4 == 340.0

    def test_product_add_with_zero_quantity(self):
        """Тест сложения продуктов с нулевым количеством."""
        product1 = Product("Товар A", "Описание A", 100.0, 0)
        product2 = Product("Товар B", "Описание B", 200.0, 2)

        # 100 * 0 + 200 * 2 = 0 + 400 = 400
        assert product1 + product2 == 400.0

    def test_product_add_with_zero_price(self):
        """Тест сложения продуктов с нулевой ценой."""
        product1 = Product("Товар A", "Описание A", 0.0, 10)
        product2 = Product("Товар B", "Описание B", 200.0, 2)

        # 0 * 10 + 200 * 2 = 0 + 400 = 400
        assert product1 + product2 == 400.0

    def test_product_add_invalid_type(self):
        """Тест сложения продукта с объектом другого типа."""
        product = Product("Товар", "Описание", 100.0, 5)

        with pytest.raises(TypeError, match="Нельзя сложить Product и str"):
            product + "строка"

        with pytest.raises(TypeError, match="Нельзя сложить Product и int"):
            product + 10
