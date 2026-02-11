import pytest

from src.categories import Category, CategoryIterator
from src.products import Product


class TestCategory:
    """Тесты для класса Category."""

    @classmethod
    def setup_class(cls):
        """Сбрасываем счетчики перед началом тестов класса."""
        Category.category_count = 0
        Category.product_count = 0

    def setup_method(self):
        """Сбрасываем счетчики перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    @classmethod
    def teardown_class(cls):
        """Сбрасываем счетчики после тестов класса."""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization(self):
        """Тест корректности инициализации категории."""
        products = [
            Product("Телефон", "Смартфон", 50000.0, 10),
            Product("Ноутбук", "Игровой ноутбук", 100000.0, 5),
            Product("Планшет", "Графический планшет", 30000.0, 3),
        ]

        category = Category(name="Электроника", description="Электронные устройства", products=products)

        assert category.name == "Электроника"
        assert category.description == "Электронные устройства"
        # Проверяем через геттер
        assert "Телефон, 50000.0 руб. Остаток: 10 шт." in category.products
        assert "Ноутбук, 100000.0 руб. Остаток: 5 шт." in category.products

    def test_add_product_method(self):
        """Тест метода add_product."""
        category = Category("Электроника", "Техника", [])

        # Проверяем начальное состояние
        assert Category.product_count == 0
        assert len(category.products_list) == 0

        # Добавляем продукт
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        category.add_product(product)

        # Проверяем результат
        assert Category.product_count == 1
        assert len(category.products_list) == 1
        assert "Телефон, 50000.0 руб. Остаток: 10 шт." in category.products

    def test_products_getter_format(self):
        """Тест формата вывода геттера products."""
        products = [
            Product("Телефон", "Смартфон", 50000.0, 10),
            Product("Ноутбук", "Игровой ноутбук", 100000.0, 5),
        ]

        category = Category("Электроника", "Техника", products)

        products_str = category.products
        assert "Телефон, 50000.0 руб. Остаток: 10 шт." in products_str
        assert "Ноутбук, 100000.0 руб. Остаток: 5 шт." in products_str
        assert "\n" in products_str  # Проверяем перенос строки

    def test_private_products_attribute(self):
        """Тест, что _products является приватным."""
        category = Category("Тест", "Описание", [])

        # Прямой доступ к _products должен работать (внутри класса)
        assert hasattr(category, "_products")

    def test_category_count_increment(self):
        """Тест подсчета количества категорий."""
        products = [Product("Телефон", "Смартфон", 50000.0, 10)]

        assert Category.category_count == 0

        category1 = Category("Категория 1", "Описание 1", products)
        assert Category.category_count == 1
        assert category1.category_count == 1

        category2 = Category("Категория 2", "Описание 2", products)
        assert Category.category_count == 2
        assert category2.category_count == 2

    def test_product_count_increment(self):
        """Тест подсчета количества продуктов."""
        products1 = [Product("Телефон", "Смартфон", 50000.0, 10)]
        products2 = [
            Product("Ноутбук", "Игровой ноутбук", 100000.0, 5),
            Product("Планшет", "Графический планшет", 30000.0, 3),
        ]

        assert Category.product_count == 0

        category1 = Category("Категория 1", "Описание 1", products1)
        assert Category.product_count == 1
        assert category1.product_count == 1

        category2 = Category("Категория 2", "Описание 2", products2)
        assert Category.product_count == 3  # 1 + 2 = 3
        assert category2.product_count == 3

    def test_product_count_with_add_product(self):
        """Тест подсчета продуктов при использовании add_product."""
        category = Category("Электроника", "Техника", [])

        assert Category.product_count == 0

        # Добавляем первый продукт
        category.add_product(Product("Телефон", "Смартфон", 50000.0, 10))
        assert Category.product_count == 1

        # Добавляем второй продукт
        category.add_product(Product("Ноутбук", "Игровой ноутбук", 100000.0, 5))
        assert Category.product_count == 2

        # Создаем новую категорию с продуктами
        Category("Мебель", "Мебель для дома", [Product("Стул", "Офисный стул", 3000.0, 20)])
        assert Category.product_count == 3  # 2 + 1 = 3

    def test_category_access_counters_via_instance(self):
        """Тест доступа к счетчикам через экземпляр."""
        products = [
            Product("Телефон", "Смартфон", 50000.0, 10),
            Product("Ноутбук", "Игровой ноутбук", 100000.0, 5),
            Product("Планшет", "Графический планшет", 30000.0, 3),
        ]

        category = Category("Электроника", "Техника", products)

        assert category.category_count == 1
        assert category.product_count == 3

    def test_category_str_method(self):
        """Тест строкового представления категории (__str__)."""
        products = [
            Product("Телефон", "Смартфон", 50000.0, 10),
            Product("Ноутбук", "Игровой ноутбук", 100000.0, 5),
            Product("Планшет", "Графический планшет", 30000.0, 3),
        ]

        category = Category("Электроника", "Техника", products)

        # Общее количество: 10 + 5 + 3 = 18
        expected_str = "Электроника, количество продуктов: 18 шт."
        assert str(category) == expected_str

    def test_category_str_method_empty(self):
        """Тест строкового представления пустой категории."""
        category = Category("Пустая категория", "Нет товаров", [])

        expected_str = "Пустая категория, количество продуктов: 0 шт."
        assert str(category) == expected_str

    def test_category_total_quantity_property(self):
        """Тест свойства total_quantity."""
        products = [
            Product("Товар 1", "Описание 1", 100.0, 7),
            Product("Товар 2", "Описание 2", 200.0, 3),
            Product("Товар 3", "Описание 3", 300.0, 5),
        ]

        category = Category("Категория", "Описание", products)

        # 7 + 3 + 5 = 15
        assert category.total_quantity == 15

        # Добавляем ещё товар
        category.add_product(Product("Товар 4", "Описание 4", 400.0, 2))
        assert category.total_quantity == 17

    def test_category_iterator(self):
        """Тест итератора для перебора товаров в категории."""
        products = [
            Product("Товар 1", "Описание 1", 100.0, 5),
            Product("Товар 2", "Описание 2", 200.0, 3),
            Product("Товар 3", "Описание 3", 300.0, 7),
        ]

        category = Category("Категория", "Описание", products)

        # Проверяем, что можно итерироваться
        product_names = []
        for product in category:
            product_names.append(product.name)

        assert product_names == ["Товар 1", "Товар 2", "Товар 3"]

        # Проверяем, что итератор работает несколько раз
        product_names = [product.name for product in category]
        assert product_names == ["Товар 1", "Товар 2", "Товар 3"]

    def test_category_iterator_empty(self):
        """Тест итератора для пустой категории."""
        category = Category("Пустая", "Описание", [])

        # При итерации по пустой категории не должно быть элементов
        count = 0
        for _ in category:
            count += 1

        assert count == 0

    def test_category_iterator_class(self):
        """Тест класса CategoryIterator напрямую."""
        products = [
            Product("Товар 1", "Описание 1", 100.0, 5),
            Product("Товар 2", "Описание 2", 200.0, 3),
        ]

        category = Category("Категория", "Описание", products)
        iterator = CategoryIterator(category)

        # Проверяем __iter__
        assert iter(iterator) is iterator

        # Проверяем __next__
        assert next(iterator).name == "Товар 1"
        assert next(iterator).name == "Товар 2"

        # Проверяем StopIteration
        with pytest.raises(StopIteration):
            next(iterator)
