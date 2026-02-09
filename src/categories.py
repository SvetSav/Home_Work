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
