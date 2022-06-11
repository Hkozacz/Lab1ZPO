from abc import ABC
from typing import Type


class CarSpeed(ABC):
    speed: int

    @classmethod
    def get_max_speed(cls) -> int:
        return cls.speed


class Maluch(CarSpeed):
    speed: int = 100


class Ford(CarSpeed):
    speed: int = 190


class Porshe(CarSpeed):
    speed: int = 280


class Context:
    strategy: Type[CarSpeed]

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.get_max_speed()