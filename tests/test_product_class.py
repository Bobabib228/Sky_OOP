import pytest
from src.product_class import Product

def test_product(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    assert product.quantity == 5
    assert product.description == "256GB, Серый цвет, 200MP камера"
