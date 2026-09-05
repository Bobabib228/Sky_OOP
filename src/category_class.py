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
    def product_info(self):
        lines = []
        for p in self.__products:
            lines.append(f"{p.name}, Цена: {p.product_price} руб., Остаток: {p.quantity} шт.")
        return "\n".join(lines)




