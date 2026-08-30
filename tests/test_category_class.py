import pytest
from src.category_class import Category

def test_category(category,product):
    assert category.name == "Смартфон"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category.products == [product]
    assert Category.category_count == 1
    assert Category.product_count == 1
