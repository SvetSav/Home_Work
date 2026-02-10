from src import Category, Product
from src.utils import load_categories_from_json

if __name__ == "__main__":
    # Сбрасываем счетчики для чистой демонстрации
    Category.reset_counters()

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
    print(len(category1.products_list))  # Используем products_list для получения списка
    print(category1.category_count)
    print(category1.product_count)

    # Демонстрация геттера products
    print("\nСписок продуктов в категории 'Смартфоны':")
    print(category1.products)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products_list))
    print(category2.products)  # Выводим через геттер

    print(Category.category_count)
    print(Category.product_count)

    # Демонстрация add_product
    print("\n=== Демонстрация метода add_product ===")

    # Создаем новую категорию для демонстрации (не используем старую category1 повторно)
    category_demo = Category(
        "Демо-категория",
        "Категория для демонстрации добавления продукта",
        [product1, product2, product3],  # Те же продукты
    )

    print("До добавления продукта:")
    print(category_demo.products)
    print(f"Всего продуктов в системе: {Category.product_count}")

    # Создаем новый продукт для добавления
    product_new = Product("Новый смартфон", "Новая модель", 50000.0, 10)
    category_demo.add_product(product_new)

    print("\nПосле добавления продукта:")
    print(category_demo.products)
    print(f"Всего продуктов в системе: {Category.product_count}")

    # Демонстрация new_product
    print("\n=== Демонстрация класс-метода new_product ===")
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S24", "description": "512GB, Черный", "price": 200000.0, "quantity": 3}
    )
    print(f"Имя: {new_product.name}")
    print(f"Описание: {new_product.description}")
    print(f"Цена: {new_product.price}")
    print(f"Количество: {new_product.quantity}")

    # Демонстрация сеттера цены
    print("\n=== Демонстрация сеттера цены ===")
    test_product = Product("Тестовый продукт", "Для теста цены", 1000.0, 5)

    # Меняем на корректную цену
    test_product.price = 800
    print(f"Новая цена: {test_product.price}")

    # Пытаемся установить отрицательную цену
    test_product.price = -100
    print(f"Цена после попытки установить -100: {test_product.price}")

    # Пытаемся установить нулевую цену
    test_product.price = 0
    print(f"Цена после попытки установить 0: {test_product.price}")

    print("\n=== Загрузка из JSON файла ===")

    # Сбрасываем счетчики для демонстрации загрузки
    Category.reset_counters()

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
            print(f"Количество продуктов: {len(category.products_list)}")

            # Выводим продукты через геттер
            print("Продукты:")
            print(category.products)
    else:
        print("Не удалось загрузить данные из JSON файла.")
