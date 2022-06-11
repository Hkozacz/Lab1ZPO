from abc import ABC


class CarSpeed(ABC):
    speed = None

    @classmethod
    def get_max_speed(cls):
        return cls.speed

class Maluch(CarSpeed):
    speed = 100

class Ford(CarSpeed):
    speed = 190

class Porshe(CarSpeed):
    speed = 280

class Executor:
    strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self):
        self.strategy.get_max_speed()