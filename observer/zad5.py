import abc
import random
from abc import ABC


class StockMarket:

    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        self.listeners.pop(listener.index(listener))

    def change_price(self):
        for listener in self.listeners:
            listener.execute(random.randint(2000, 10000000))


class Company(ABC):

    def __init__(self):
        self.price: int = 0

    def execute(self, new_price: int):
        print('old price: ', self.price)
        self.price = new_price
        print('new price: ', self.price)


class Company1(Company):
    pass


class Company2(Company):
    pass


class Company3(Company):
    pass


if __name__ == '__main__':

    stock_market = StockMarket()
    company1 = Company1()
    company2 = Company2()
    company3 = Company3()
    stock_market.add_listener(company1)
    stock_market.add_listener(company2)
    stock_market.add_listener(company3)

    stock_market.change_price()
    stock_market.change_price()
    stock_market.change_price()
    stock_market.change_price()