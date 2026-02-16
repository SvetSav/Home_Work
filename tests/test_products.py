import io
import os
import sys

import pytest

from src.products import BaseProduct, LawnGrass, Product, Smartphone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestBaseProduct:
    """Тесты для абстрактного базового класса BaseProduct."""

    def test_base_product_is_abstract(self):
        """Тест, что BaseProduct является абстрактным классом."""
        with pytest.raises(TypeError):
            BaseProduct("Тест", "Описание", 100.0, 5)

    def test_product_inherits_from_base(self):
        """Тест, что Product наследуется от BaseProduct."""
        assert issubclass(Product, BaseProduct) is True

    def test_smartphone_inherits_from_base(self):
        """Тест, что Smartphone наследуется от BaseProduct через Product."""
        assert issubclass(Smartphone, BaseProduct) is True

    def test_lawn_grass_inherits_from_base(self):
        """Тест, что LawnGrass наследуется от BaseProduct через Product."""
        assert issubclass(LawnGrass, BaseProduct) is True


class TestPrintMixin:
    """Тесты для миксина PrintMixin."""

    def test_product_creation_prints_repr(self):
        """Тест, что при создании Product печатается repr."""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        Product("Тест", "Описание", 100.0, 5)

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        assert output == "Product('Тест', 'Описание', 100.0, 5)"

    def test_smartphone_creation_prints_repr(self):
        """Тест, что при создании Smartphone печатается repr."""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        Smartphone("Samsung", "Описание", 50000.0, 5, 95.5, "S23", 256, "Черный")

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        assert output == "Smartphone('Samsung', 'Описание', 50000.0, 5, 95.5, 'S23', 256, 'Черный')"

    def test_lawn_grass_creation_prints_repr(self):
        """Тест, что при создании LawnGrass печатается repr."""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        LawnGrass("Трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        assert output == "LawnGrass('Трава', 'Описание', 500.0, 20, 'Россия', '7 дней', 'Зеленый')"


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

    def test_product_add_method_same_class(self):
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

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов: Product и str"):
            product + "строка"

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов: Product и int"):
            product + 10


class TestSmartphone:
    """Тесты для класса Smartphone."""

    def test_smartphone_initialization(self):
        """Тест инициализации смартфона."""
        smartphone = Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5,
            95.5,
            "S23 Ultra",
            256,
            "Серый",
        )

        assert smartphone.name == "Samsung Galaxy S23 Ultra"
        assert smartphone.description == "256GB, Серый цвет, 200MP камера"
        assert smartphone.price == 180000.0
        assert smartphone.quantity == 5
        assert smartphone.efficiency == 95.5
        assert smartphone.model == "S23 Ultra"
        assert smartphone.memory == 256
        assert smartphone.color == "Серый"

    def test_smartphone_inheritance(self):
        """Тест наследования от Product."""
        smartphone = Smartphone("Samsung Galaxy S23 Ultra", "Описание", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")

        assert isinstance(smartphone, Product)
        assert isinstance(smartphone, Smartphone)

    def test_smartphone_str_method(self):
        """Тест строкового представления смартфона."""
        smartphone = Smartphone("Samsung Galaxy S23 Ultra", "Описание", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")

        expected_str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт. Модель: S23 Ultra, 256ГБ, Серый"
        assert str(smartphone) == expected_str

    def test_smartphone_repr_method(self):
        """Тест repr представления смартфона."""
        smartphone = Smartphone("Samsung Galaxy S23 Ultra", "Описание", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
        repr_str = repr(smartphone)
        assert "Smartphone" in repr_str
        assert "Samsung Galaxy S23 Ultra" in repr_str
        assert "95.5" in repr_str  # Проверяем значение efficiency
        assert "'S23 Ultra'" in repr_str  # Проверяем модель
        assert "256" in repr_str  # Проверяем память
        assert "'Серый'" in repr_str  # Проверяем цвет

    def test_smartphone_add_same_class(self):
        """Тест сложения двух смартфонов."""
        smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "Описание", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
        smartphone2 = Smartphone("Iphone 15", "Описание", 210000.0, 8, 98.2, "15", 512, "Gray space")

        # 180000 * 5 + 210000 * 8 = 900000 + 1680000 = 2580000
        assert smartphone1 + smartphone2 == 2580000.0

    def test_smartphone_price_setter_inheritance(self):
        """Тест наследования сеттера цены."""
        smartphone = Smartphone("Samsung Galaxy S23 Ultra", "Описание", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")

        smartphone.price = 200000.0
        assert smartphone.price == 200000.0

        captured_output = io.StringIO()
        sys.stdout = captured_output
        smartphone.price = -100
        sys.stdout = sys.__stdout__

        assert smartphone.price == 200000.0
        assert "Цена не должна быть нулевая или отрицательная" in captured_output.getvalue()


class TestLawnGrass:
    """Тесты для класса LawnGrass."""

    def test_lawn_grass_initialization(self):
        """Тест инициализации газонной травы."""
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

        assert grass.name == "Газонная трава"
        assert grass.description == "Элитная трава для газона"
        assert grass.price == 500.0
        assert grass.quantity == 20
        assert grass.country == "Россия"
        assert grass.germination_period == "7 дней"
        assert grass.color == "Зеленый"

    def test_lawn_grass_inheritance(self):
        """Тест наследования от Product."""
        grass = LawnGrass("Газонная трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")

        assert isinstance(grass, Product)
        assert isinstance(grass, LawnGrass)

    def test_lawn_grass_str_method(self):
        """Тест строкового представления газонной травы."""
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

        expected_str = (
            "Газонная трава, 500.0 руб. Остаток: 20 шт. Производитель: Россия, срок прорастания: 7 дней, цвет: Зеленый"
        )
        assert str(grass) == expected_str

    def test_lawn_grass_repr_method(self):
        """Тест repr представления газонной травы."""
        grass = LawnGrass("Газонная трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")
        repr_str = repr(grass)
        assert "LawnGrass" in repr_str
        assert "Газонная трава" in repr_str
        assert "'Россия'" in repr_str  # Проверяем страну
        assert "'7 дней'" in repr_str  # Проверяем срок прорастания
        assert "'Зеленый'" in repr_str  # Проверяем цвет

    def test_lawn_grass_add_same_class(self):
        """Тест сложения двух продуктов газонной травы."""
        grass1 = LawnGrass("Газонная трава", "Элитная трава", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

        # 500 * 20 + 450 * 15 = 10000 + 6750 = 16750
        assert grass1 + grass2 == 16750.0


class TestProductAdditionRestrictions:
    """Тесты для ограничений сложения разных классов."""

    def test_add_product_and_smartphone(self):
        """Тест сложения Product и Smartphone."""
        product = Product("Обычный товар", "Описание", 100.0, 5)
        smartphone = Smartphone("Смартфон", "Описание", 50000.0, 2, 90.0, "X", 128, "Черный")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов: Product и Smartphone"):
            _ = product + smartphone

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов: Smartphone и Product"):
            _ = smartphone + product

    def test_add_product_and_lawn_grass(self):
        """Тест сложения Product и LawnGrass."""
        product = Product("Обычный товар", "Описание", 100.0, 5)
        grass = LawnGrass("Трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов: Product и LawnGrass"):
            _ = product + grass

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов: LawnGrass и Product"):
            _ = grass + product

    def test_add_smartphone_and_lawn_grass(self):
        """Тест сложения Smartphone и LawnGrass."""
        smartphone = Smartphone("Смартфон", "Описание", 50000.0, 2, 90.0, "X", 128, "Черный")
        grass = LawnGrass("Трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов: Smartphone и LawnGrass"):
            _ = smartphone + grass

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов: LawnGrass и Smartphone"):
            _ = grass + smartphone

    def test_smartphone_price_setter_inheritance(self):
        """Тест наследования сеттера цены."""
        smartphone = Smartphone("Samsung Galaxy S23 Ultra", "Описание", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")

        # Устанавливаем корректную цену
        smartphone.price = 200000.0
        assert smartphone.price == 200000.0

        # Пытаемся установить отрицательную цену
        captured_output = io.StringIO()
        sys.stdout = captured_output
        smartphone.price = -100
        sys.stdout = sys.__stdout__

        assert smartphone.price == 200000.0
        assert "Цена не должна быть нулевая или отрицательная" in captured_output.getvalue()
