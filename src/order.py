from abc import ABC, abstractmethod

from src.products import Product


class AbstractBase(ABC):
    """Абстрактный базовый класс для сущностей с именем и описанием."""

    @abstractmethod
    def __init__(self, name: str, description: str):
        """Абстрактный метод инициализации."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Абстрактный геттер для имени."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Абстрактный геттер для описания."""
        pass


class Order(AbstractBase):
    """Класс для представления заказа."""

    def __init__(self, product: Product, quantity: int):
        """
        Инициализация заказа.

        Args:
            product: Товар в заказе
            quantity: Количество товара

        Raises:
            ValueError: Если количество меньше или равно 0
        """
        if quantity <= 0:
            raise ValueError("Количество товара должно быть больше 0")

        self._product = product
        self._quantity = quantity
        self._total_price = product.price * quantity

    @property
    def name(self) -> str:
        """Название заказа (совпадает с названием товара)."""
        return f"Заказ: {self._product.name}"

    @property
    def description(self) -> str:
        """Описание заказа."""
        return f"Заказ товара {self._product.name} в количестве {self._quantity} шт."

    @property
    def product(self) -> Product:
        """Геттер для товара."""
        return self._product

    @property
    def quantity(self) -> int:
        """Геттер для количества."""
        return self._quantity

    @property
    def total_price(self) -> float:
        """Геттер для общей стоимости."""
        return self._total_price

    def __str__(self) -> str:
        return f"{self.name}\nТовар: {self._product.name}\nКоличество: {self._quantity} шт.\nОбщая стоимость: {self._total_price} руб."

    def __repr__(self) -> str:
        return f"Order({self._product!r}, {self._quantity})"
