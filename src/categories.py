from typing import Iterator, List

from src.products import Product


class Category:
    """Класс для представления категории товаров."""

    name: str
    description: str
    _products: list  # Приватный атрибут

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0
    _all_products: List[Product] = []  # Список всех уникальных продуктов

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории
        """
        self.name = name
        self.description = description
        self._products = []

        # Добавляем продукты через тот же метод add_product
        for product in products:
            # Временно отключаем проверку на существование в категории для конструктора
            if product not in self._products:
                self._products.append(product)

                # Проверяем, не был ли уже учтен этот продукт глобально
                if product not in Category._all_products:
                    Category._all_products.append(product)
                    Category.product_count += 1

        # Увеличиваем счетчик категорий
        Category.category_count += 1

    def add_product(self, product):
        """
        Добавляет продукт в категорию.
        Можно добавить только объекты класса Product или его наследников.

        Args:
            product: Объект класса Product или его наследника для добавления

        Raises:
            TypeError: Если product не является экземпляром Product или его наследника
        """
        # Проверяем, что product является экземпляром Product или его наследника
        if not isinstance(product, Product):
            raise TypeError(f"Можно добавить только продукт или его наследника, а не {type(product).__name__}")

        # Если продукт уже есть в этой категории (тот же объект), не добавляем
        if product in self._products:
            print(f"Продукт '{product.name}' уже есть в категории '{self.name}'")
            return

        # Добавляем продукт в категорию
        self._products.append(product)

        # Проверяем, не был ли уже учтен этот продукт глобально
        if product not in Category._all_products:
            Category._all_products.append(product)
            Category.product_count += 1
            print(f"Добавлен новый продукт: {product.name}, всего продуктов: {Category.product_count}")

    @property
    def products(self):
        """
        Геттер для получения строкового представления продуктов.
        Теперь использует __str__ каждого продукта.

        Returns:
            str: Строка со всеми продуктами
        """
        return "\n".join(str(product) for product in self._products)

    @property
    def products_list(self):
        """
        Геттер для получения списка продуктов (для внутреннего использования).

        Returns:
            list: Список объектов Product
        """
        return self._products

    @property
    def total_quantity(self) -> int:
        """
        Подсчитывает общее количество товаров в категории.

        Returns:
            int: Суммарное количество всех товаров
        """
        return sum(product.quantity for product in self._products)

    @classmethod
    def reset_counters(cls):
        """
        Сбрасывает счетчики категорий и продуктов.
        """
        cls.category_count = 0
        cls.product_count = 0
        cls._all_products = []

    def __repr__(self) -> str:
        return f"Category(name={self.name!r}, description={self.description!r}, products_count={len(self._products)})"

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории с общим количеством товаров.
        Суммирует quantity всех продуктов в категории.
        """
        total = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total} шт."

    def __iter__(self) -> Iterator[Product]:
        """
        Возвращает итератор для перебора товаров в категории.
        """
        return CategoryIterator(self)


class CategoryIterator:
    """
    Итератор для перебора товаров в категории.
    """

    def __init__(self, category: "Category"):
        """
        Инициализация итератора.

        Args:
            category: Объект Category для итерации
        """
        self._category = category
        self._index = 0

    def __iter__(self) -> Iterator[Product]:
        """Возвращает сам итератор."""
        return self

    def __next__(self) -> Product:
        """Возвращает следующий товар в категории."""
        if self._index >= len(self._category._products):
            raise StopIteration
        product = self._category._products[self._index]
        self._index += 1
        return product
