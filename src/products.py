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
