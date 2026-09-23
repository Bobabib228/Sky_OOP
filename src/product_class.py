from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class MixinRepr:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"{self}")

class Product(MixinRepr, BaseProduct):
    """
    Класс содержащий Продукты
    """

    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, "
            f"{self.price}, {self.quantity})"
        )

    @classmethod
    def new_product(cls, lst):
        return cls(lst["name"], lst["description"], lst["price"], lst["quantity"])

    @property
    def product_price(self):
        return self._price

    @product_price.setter
    def product_price(self, val: float):
        if val <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return self._price
        else:
            self._price = val
            return self._price

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError
        else:
            return (self._price * self.quantity) + (other._price * other.quantity)


class Smartphone(Product):

    def __init__(self,name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self,name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color



pr1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)