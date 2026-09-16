from src.product_class import Product


class Category:
    """
    Класс содержащий категории продуктов
    """

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
    def products_list(self):
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
            total_quantity = sum(product.quantity for product in self.__products)
            return f"{self.name}, количество продуктов: {total_quantity} шт."





