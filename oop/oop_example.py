"""
Example of uisng OOP in Python 3
"""
import sys
import abc

print(sys.version_info)

if sys.version_info >= (3,4):
    ABC = abc.ABC
else:
    ABC = abc.ABCMeta('ABC', (), {})
# superclass
# class names are cammel case, methods and attribute are snakesace, constants are all Upper case


class AbstractOrder(abc.ABC):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def order_detail(self):
        pass

    def hello_from_parent(self):
        print("Hello from Parent class Abstract")


class Order(AbstractOrder):

    # Global class attribute
    _in_stock = 10

    # method oveloading - use default values
    def __init__(self, num_items=0, name=None):

        # num public
        # _num protected/private (preferred to be private. Subclass can use but users of class shouldn't use it)
        # __num_protected private - only for this class can't subclass
        super().__init__(name=name)
        #super(Order, self).__init__(name=name) Python 2 and 3 compatible
        self.num_items = num_items
        self._in_stock -= self.num_items

    # instance method
    def order_detail(self):
        return "Ordered {} items".format(self.num_items)

    # class method. Only knows global variables. Was not initialized. This is a static method in C++
    @classmethod
    def class_method(cls):
        print("In stock: {}".format(Order._in_stock))

    # pretty useless
    @staticmethod
    def static_method():
        print("Doesn't know its class")


class StoreOrder(Order):

    def __init__(self, num_items = 0, name=None):
        super().__init__(num_items=num_items, name=None)

    # method override
    def order_detail(self):
        return "Ordered {} items".format(self.num_items)

order = Order(3, 'Sarah')
order2 = StoreOrder(2, 'Mohe')

for order in (order, order2):
    print(order.order_detail())

print(order.static_method(), 'preferred: ', Order.static_method())

print(order.hello_from_parent())
print("You shohldn't do this: ", Order._in_stock)
try:
    order = AbstractOrder('Sarah')
except Exception as err:
    print(err)


