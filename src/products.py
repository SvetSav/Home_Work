from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Абстрактный метод инициализации продукта."""
        pass

    @abstractmethod
    def __str__(self):
        """Абстрактный строковый метод."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод сложения."""
        pass

    @property
    @abstractmethod
    def price(self):
        """Абстрактный геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        """Абстрактный сеттер для цены."""
        pass


class PrintMixin:
    """Миксин для печати информации о создании объекта."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Инициализация миксина с печатью информации."""
        print(repr(self))


class Product(BaseProduct, PrintMixin):
    """Класс для представления продукта."""

    name: str
    description: str
    _price: float  # Приватный атрибут
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация продукта.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество в наличии
        Raises:
            ValueError: Если количество равно 0
        """
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self._price = price if price > 0 else 0  # Защита от отрицательной цены
        self.quantity = quantity
        PrintMixin.__init__(self)

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания нового продукта из словаря.

        Args:
            product_data: Словарь с данными продукта

        Returns:
            Product: Новый объект продукта
        """
        return cls(
            name=product_data.get("name", ""),
            description=product_data.get("description", ""),
            price=product_data.get("price", 0.0),
            quantity=product_data.get("quantity", 0),
        )

    @property
    def price(self):
        """
        Геттер для цены.

        Returns:
            float: Цена продукта
        """
        return self._price

    @price.setter
    def price(self, value: float):
        """
        Сеттер для цены с проверкой.

        Args:
            value: Новая цена
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    def __repr__(self) -> str:
        return f"Product('{self.name}', '{self.description}', {self._price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод сложения двух продуктов.
        Возвращает сумму произведений цены на количество.

        Args:
            other: Другой объект Product

        Returns:
            float: Общая стоимость товаров на складе

        Raises:
            TypeError: Если объекты разных классов
        """
        if not isinstance(other, Product):
            raise TypeError(f"Нельзя складывать товары разных классов: {type(self).__name__} и {type(other).__name__}")
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать товары разных классов: {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product, BaseProduct):
    """Класс для представления смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """
        Инициализация смартфона.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество в наличии
            efficiency: Производительность
            model: Модель
            memory: Объем встроенной памяти (ГБ)
            color: Цвет
        """

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return (
            f"Smartphone('{self.name}', '{self.description}', {self._price}, {self.quantity}, "
            f"{self.efficiency}, '{self.model}', {self.memory}, '{self.color}')"
        )

    def __str__(self) -> str:
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт. Модель: {self.model}, {self.memory}ГБ, {self.color}"


class LawnGrass(Product, BaseProduct):
    """Класс для представления газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """
        Инициализация газонной травы.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество в наличии
            country: Страна-производитель
            germination_period: Срок прорастания
            color: Цвет
        """

        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return (
            f"LawnGrass('{self.name}', '{self.description}', {self._price}, {self.quantity}, "
            f"'{self.country}', '{self.germination_period}', '{self.color}')"
        )

    def __str__(self) -> str:
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт. Производитель: {self.country}, срок прорастания: {self.germination_period}, цвет: {self.color}"
