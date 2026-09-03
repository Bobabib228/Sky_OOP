import pytest

from src.category_class import Category
from src.product_class import Product


@pytest.fixture
def category(product):
    return Category(
        "Смартфон",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product],
    )


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
