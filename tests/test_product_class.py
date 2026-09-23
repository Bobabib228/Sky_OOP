import pytest
from abc import ABC
from src.product_class import Product, Smartphone, MixinRepr, BaseProduct


def test_product(product, product2, product_pattern, capsys):
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
    summ_product = product + product2
    assert summ_product == 390000.0
    assert Product.__mro__ == (Product, MixinRepr, BaseProduct, ABC, object)


def test_smartphone(smartphone1, smartphone2, product):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.quantity == 5
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.color == "Серый"
    assert smartphone1.product_price == 180000.0
    summ_smartphone = smartphone1 + smartphone2
    assert summ_smartphone == 2580000.0
    with pytest.raises(TypeError):
        print(smartphone1 + product)


def test_lawngrass(lawngrass1):
    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
