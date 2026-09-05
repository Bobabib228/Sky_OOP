import pytest
from src.product_class import Product


def test_product(product, product_pattern, capsys):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.quantity == 5
    assert product.description == "256GB, Серый цвет, 200MP камера"

    product1 = Product.new_product(product_pattern)
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.quantity == 5
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.product_price == 180000.0
    product1.product_price = -1
    assert product1.product_price == 180000
    captured = capsys.readouterr()
    assert captured.out.strip()
    product1.product_price = 10
    assert product1.product_price == 10

