class Product:
    """
    Класс содержащий Продукты
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, lst):
        return cls(lst["name"], lst["description"], lst["price"], lst["quantity"])

    @property
    def product_price(self):
        return self.__price

    @product_price.setter
    def product_price(self, val: float):
        if val <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return self.__price
        else:
            self.__price = val
            return self.__price

    def __add__(self, other):
        return (self.__price * self.quantity) + (other.__price * other.quantity)




pr1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 5)
pr2 = Product("Iphone 13", "256GB, Серый цвет, super камера", 60000.0, 5)
tr = pr1 + pr2
print(tr)
