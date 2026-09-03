from product_class import Product


class Category:
    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @add_product.getter
    def add_product(self):
        return self.__products
