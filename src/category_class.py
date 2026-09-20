from src.product_class import Product


class Category:
    """
    Класс содержащий категории продуктов
    """

    name: str
    description: str
    _products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = products

        Category.category_count += 1
        Category.product_count += len(products)


    def add_product(self, product):
        if isinstance(product, Product):
            self._products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_list(self):
        return "\n".join(str(product) for product in self._products)

    def __str__(self):
            total_quantity = sum(product.quantity for product in self._products)
            return f"{self.name}, количество продуктов: {total_quantity} шт."








