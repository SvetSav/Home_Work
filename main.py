import json
from typing import List


class Product:
    """Класс для представления продукта."""

    name: str
    description: str
    price: float
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
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product(name={self.name!r}, description={self.description!r}, price={self.price}, quantity={self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    """Класс для представления категории товаров."""

    name: str
    description: str
    products: list

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории
        """
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчики при создании новой категории
        Category.category_count += 1
        Category.product_count += len(products)

    def __repr__(self) -> str:
        return f"Category(name={self.name!r}, description={self.description!r}, products={self.products})"

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self.products)}"


def load_categories_from_json(file_path: str = "products.json") -> List[Category]:
    """
    Загружает категории и продукты из JSON файла.

    Args:
        file_path: Путь к JSON файлу с данными

    Returns:
        List[Category]: Список объектов Category
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка при чтении JSON файла {file_path}.")
        return []

    categories = []

    for category_data in data:
        # Создаем продукты для категории
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)

        # Создаем категории
        category = Category(name=category_data["name"], description=category_data["description"], products=products)
        categories.append(category)

    return categories


if __name__ == "__main__":
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

    # Загружаем категории из JSON
    loaded_categories = load_categories_from_json()

    if loaded_categories:
        print(f"Загружено категорий: {len(loaded_categories)}")
        print(f"Всего категорий (после загрузки): {Category.category_count}")
        print(f"Всего продуктов (после загрузки): {Category.product_count}")

        # Выводим информацию о загруженных категориях
        for i, category in enumerate(loaded_categories, 1):
            print(f"\nКатегория {i}: {category.name}")
            print(f"Описание: {category.description}")
            print(f"Количество продуктов: {len(category.products)}")

            for product in category.products:
                print(f"  - {product.name}: {product.price} руб., остаток: {product.quantity} шт.")
    else:
        print("Не удалось загрузить данные из JSON файла.")
