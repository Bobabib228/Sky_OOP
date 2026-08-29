import pytest

from src.category_class import Category
from src.product_class import Product

@pytest.fixture
def category(products1):
    return Category(
        "Смартфон",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [products1])


@pytest.fixture
def products1():
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )