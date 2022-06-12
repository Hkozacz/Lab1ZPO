import random
from abc import ABC


class Stock:

    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        self.listeners.pop(listener.index(listener))

    def change_price(self):
        for listener in self.listeners:
            listener.new_price(random.randint(0, 100))


class Company(ABC):

    def __init__(self):
        self.price = 0

    def new_price(self, new_price: int):
        self.price = new_price


class CdProjekt(Company):
    pass


class EaGames(Company):
    pass


class Blizzard(Company):
    pass


if __name__ == '__main__':

    stock_market = Stock()
    cdp = CdProjekt()
    ea = EaGames()
    blizz = Blizzard()
    for company in [cdp, ea, blizz]:
        stock_market.add_listener(company)

    for i in range(0, 10):
        stock_market.change_price()
