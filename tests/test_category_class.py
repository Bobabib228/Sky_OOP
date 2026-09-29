import pytest

from src.category_class import Category


def test_category(category, product):
    assert category.name == "Смартфон"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert Category.category_count == 1
    assert Category.product_count == 1
    category_str = str(category)
    assert category_str == "Смартфон, количество продуктов: 5 шт."
    product.quantity = 0
    print(product.quantity)
    assert category.middle_price() == 0


def test_category_raises_add_product(category, product):
    with pytest.raises(TypeError) as err:
        category.add_product("ewrewr")
