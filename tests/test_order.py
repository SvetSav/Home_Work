import pytest

from src.order import AbstractBase, Order
from src.products import Product


class TestAbstractBase:
    """Тесты для абстрактного базового класса AbstractBase."""

    def test_abstract_base_is_abstract(self):
        """Тест, что AbstractBase является абстрактным классом."""
        with pytest.raises(TypeError):
            AbstractBase("Тест", "Описание")

    def test_order_inherits_from_base(self):
        """Тест, что Order наследуется от AbstractBase."""
        assert issubclass(Order, AbstractBase)


class TestOrder:
    """Тесты для класса Order."""

    def setup_method(self):
        """Создаем продукт для тестов."""
        self.product = Product("Телефон", "Смартфон", 50000.0, 10)

    def test_order_initialization(self):
        """Тест инициализации заказа."""
        order = Order(self.product, 2)

        assert order.product == self.product
        assert order.quantity == 2
        assert order.total_price == 100000.0
        assert order.name == "Заказ: Телефон"
        assert order.description == "Заказ товара Телефон в количестве 2 шт."

    def test_order_invalid_quantity(self):
        """Тест создания заказа с некорректным количеством."""
        with pytest.raises(ValueError, match="Количество товара должно быть больше 0"):
            Order(self.product, 0)

        with pytest.raises(ValueError, match="Количество товара должно быть больше 0"):
            Order(self.product, -1)

    def test_order_str_method(self):
        """Тест строкового представления заказа."""
        order = Order(self.product, 3)
        str_repr = str(order)

        assert "Заказ: Телефон" in str_repr
        assert "Товар: Телефон" in str_repr
        assert "Количество: 3 шт." in str_repr
        assert "Общая стоимость: 150000.0 руб." in str_repr

    def test_order_repr_method(self):
        """Тест repr представления заказа."""
        order = Order(self.product, 2)
        repr_str = repr(order)

        # Проверяем, что repr содержит Product(...) и количество
        assert "Order(Product(" in repr_str
        assert "Телефон" in repr_str
        assert "Смартфон" in repr_str
        assert "50000.0" in repr_str
        assert "10" in repr_str
        assert ", 2)" in repr_str

    def test_order_price_update(self):
        """Тест обновления цены заказа при изменении цены товара."""
        order = Order(self.product, 2)
        assert order.total_price == 100000.0

        self.product.price = 60000.0
        # Цена заказа не обновляется автоматически
        assert order.total_price == 100000.0

        # Создаем новый заказ с новой ценой
        order2 = Order(self.product, 2)
        assert order2.total_price == 120000.0
