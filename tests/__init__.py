import pytest


@pytest.fixture
def reset_category_counters():
    """Фикстура для сброса счетчиков категорий."""
    from src.categories import Category

    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0
