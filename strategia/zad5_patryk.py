from abc import ABC


class TaxInterface(ABC):
    value = None

    @classmethod
    def get_tax(cls):
        return cls.value


class PolandTax(TaxInterface):
    value = 23

class UnitedKingdoms(TaxInterface):
    value = 20

class GermanTax(TaxInterface):
    value = 19


class Shop:

    def buy(self, client):
        print(f'tax = {client.tax.value}')


class Client:
    tax = None

    def set_tax(self, tax):
        self.tax = tax


if __name__ == '__main__':
    shop = Shop()
    client = Client()
    client.set_tax(GermanTax)
    shop.buy(client)
