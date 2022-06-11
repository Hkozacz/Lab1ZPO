from abc import ABC
from typing import Type


class TaxInterface(ABC):
    tax: int

    @classmethod
    def get_tax(cls) -> int:
        return cls.tax


class PolandTax(TaxInterface):
    tax = 23


class UKTax(TaxInterface):
    tax = 8


class GermanTax(TaxInterface):
    tax = 18


class Shop:
    map_tax = {
        'PL': PolandTax,
        'UK': UKTax,
        'GE': GermanTax,
    }

    def buy(self, client_country) -> None:
        tax_object = self.map_tax[client_country]
        print(f'You bought item, with tax: {tax_object.tax}')


class Client:
    country_of_origin: str
    shop = Type[Shop]

    def __init__(self, country_iso, shop) -> None:
        self.country_of_origin = country_iso
        self.shop = shop

    def buy_item(self) -> None:
        self.shop.buy(self.country_of_origin)


if __name__ == '__main__':
    biedronka = Shop()
    client = Client('PL', biedronka)
    client.buy_item()
