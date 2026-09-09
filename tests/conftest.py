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
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 5)


@pytest.fixture
def product2():
    return Product("iphone 13", "256GB, Серый цвет, super камера", 60000.0, 5)


@pytest.fixture
def product_pattern():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0, "quantity": 5}
