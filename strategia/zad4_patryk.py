from abc import ABC


class Flying(ABC):
    fly_text = None

    @classmethod
    def fly(cls):
        print(cls.fly_text)

class StandardFly(Flying):
    fly_text = 'latam'

class JetPackFly(Flying):
    fly_text = 'szybko latam'


class Duck:
    flying_class = StandardFly

    def ustawLatanieInterfejs(self, flying_class):
        self.flying_class = flying_class

    def lataj(self):
        self.flying_class.fly()

rubber_duck = Duck()
mr_duck = Duck()
extra_duck = Duck()
ducks = [rubber_duck, mr_duck, extra_duck]

for duck in ducks:
    duck.lataj()

rubber_duck.ustawLatanieInterfejs(JetPackFly)

for duck in ducks:
    duck.lataj()