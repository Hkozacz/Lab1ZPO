from abc import ABC
from typing import Type

class SpedzanieWolnegoCzasu(ABC):
    message = None

    @classmethod
    def spedzaj_wolny_czas(cls):
        print(cls.message)

class LiteraturaPopularnoNaukowa(SpedzanieWolnegoCzasu):
    message = 'Czytanie'

class Silownia(SpedzanieWolnegoCzasu):
    message = 'Pakowanie'

class Dojezdzac(ABC):
    message = None

    @classmethod
    def dojezdzaj(cls):
        print(cls.message)

class Samochod(Dojezdzac):
    message = 'Samochodem'


class Rower(Dojezdzac):
    message = 'Rowerem'

class Pracowac(ABC):
    message: str

    @classmethod
    def pracuj(cls):
        print(cls.message)

class NaprawaSamochodu(Pracowac):
    message = 'naprawa samochodu'

class RoznoszenieListow(Pracowac):
    message = 'Roznoszenie listow'

class Leczenie(Pracowac):
    message = 'Leczenie'

class Pracownik:
    pracowac: Type[Pracowac]
    dojezdzac: Type[Dojezdzac]
    spedzanie_wolnego_czasu: Type[SpedzanieWolnegoCzasu]

    def __init__(self, zawod):
        self.zawod = zawod

    def set_pracowac(self, pracowac):
        self.pracowac = pracowac

    def set_dojezdzac(self, dojezdzac):
        self.dojezdzac = dojezdzac

    def set_spedzanie_wolnego_czasi(self, spedzanie_wolnego_czasu):
        self.spedzanie_wolnego_czasu = spedzanie_wolnego_czasu

    def pracuj(self):
        self.pracowac.pracuj()

    def dojezdzaj(self):
        self.dojezdzac.dojezdzaj()

    def spedzaj_wolny_czas(self):
        self.spedzanie_wolnego_czasu.spedzaj_wolny_czas()