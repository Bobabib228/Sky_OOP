class Product:
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
    def product_price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return self.__price
        else:
            self.__price = value
            return self.__price