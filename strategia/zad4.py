import abc
from abc import ABC
from typing import Type


class FlyingStrategy(ABC):
    flying_message: str

    @classmethod
    def fly(cls):
        print(cls.flying_message)


class StandardFly(FlyingStrategy):
    flying_message = 'flutter flutter'


class JetPackFly(FlyingStrategy):
    flying_message = 'SIUUUUUUU'


class Duck:
    strategy: Type[FlyingStrategy] = None
    name: str = None

    def __init__(self, name: str):
        self.name = name
        self.strategy = StandardFly

    def set_fly_strategy(self, fly_strategy: Type[FlyingStrategy]):
        self.strategy = fly_strategy

    def fly(self):
        self.strategy.fly()


ducks = [Duck('Normal duck'), Duck('Rubber duck'), Duck('John')]


if __name__ == '__main__':
    [duck.fly() for duck in ducks]
    print('--------------')
    print('______________')
    ducks[1].set_fly_strategy(JetPackFly)
    [duck.fly() for duck in ducks]