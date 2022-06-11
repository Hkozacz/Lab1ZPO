from abc import ABC
from typing import Type


class Pracowac(ABC):
    message: str

    @classmethod
    def pracuj(cls) -> None:
        print(cls.message)


class NaprawaSamochodu(Pracowac):
    message = 'naprawa samochodu'


class RoznoszenieListow(Pracowac):
    message = 'Roznoszenie listow'


class Leczenie(Pracowac):
    message = 'Leczenie'


class Dojezdzac(ABC):
    message: str

    @classmethod
    def dojezdzaj(cls) -> None:
        print(cls.message)


class Samochod(Dojezdzac):
    message = 'Samochodem'


class Rower(Dojezdzac):
    message = 'Rowerem'


class SpedzanieWolnegoCzasu(ABC):
    message: str

    @classmethod
    def spedzaj_wolny_czas(cls) -> None:
        print(cls.message)


class LiteraturaPopularnoNaukowa(SpedzanieWolnegoCzasu):
    message = 'Czytanie'


class Silownia(SpedzanieWolnegoCzasu):
    message = 'Pakowanie'


class Pracownik:
    pracowac: Type[Pracowac]
    dojezdzac: Type[Dojezdzac]
    spedzanie_wolnego_czasu: Type[SpedzanieWolnegoCzasu]

    def __init__(self, zawod: str) -> None:
        self.zawod: str = zawod

    def set_pracowac(self, pracowac: Type[Pracowac]) -> None:
        self.pracowac = pracowac

    def set_dojezdzac(self, dojezdzac: Type[Dojezdzac]) -> None:
        self.dojezdzac = dojezdzac

    def set_spedzanie_wolnego_czasi(self, spedzanie_wolnego_czasu: Type[SpedzanieWolnegoCzasu]) -> None:
        self.spedzanie_wolnego_czasu = spedzanie_wolnego_czasu

    def pracuj(self) -> None:
        self.pracowac.pracuj()

    def dojezdzaj(self) -> None:
        self.dojezdzac.dojezdzaj()

    def spedzaj_wolny_czas(self) -> None:
        self.spedzanie_wolnego_czasu.spedzaj_wolny_czas()