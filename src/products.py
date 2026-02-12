class Product:
    """Класс для представления продукта."""

    name: str
    description: str
    _price: float  # Приватный атрибут
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self._price = price if price > 0 else 0  # Защита от отрицательной цены
        self.quantity = quantity

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
        return f"Product(name={self.name!r}, description={self.description!r}, price={self._price}, quantity={self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
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
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать товары разных классов: {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
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
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self) -> str:
        return (
            f"Smartphone(name={self.name!r}, description={self.description!r}, "
            f"price={self._price}, quantity={self.quantity}, "
            f"efficiency={self.efficiency}, model={self.model!r}, "
            f"memory={self.memory}, color={self.color!r})"
        )

    def __str__(self) -> str:
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт. Модель: {self.model}, {self.memory}ГБ, {self.color}"


class LawnGrass(Product):
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
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self) -> str:
        return (
            f"LawnGrass(name={self.name!r}, description={self.description!r}, "
            f"price={self._price}, quantity={self.quantity}, "
            f"country={self.country!r}, germination_period={self.germination_period!r}, "
            f"color={self.color!r})"
        )

    def __str__(self) -> str:
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт. Производитель: {self.country}, срок прорастания: {self.germination_period}, цвет: {self.color}"
