import io
import random
from abc import ABC


class Multiton(ABC):

    _instances: list
    _max_instances: int

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instances', None):
            cls._instances = []
        if len(cls._instances) < cls._max_instances:
            ins = super().__new__(cls)
            cls._instances.append(ins)
            return ins
        return


class Singleton(ABC):
    _instance: object

    def __new__(cls, *args, **kwargs):
        if getattr(cls, '_instance', None):
            return
        cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Finances(Singleton):

    def __init__(self):
        self.periods = []

    def add_period(self, period):
        self.periods.append(period)

    def generate_file(self):
        file_string = 'Sprawozdanie finansowe: '
        for period in self.periods:
            file_string = f'{file_string} \n {period.data}'

        file = io.BytesIO(file_string.encode('utf-8'))
        print(file.read())
        return file


class Period(Multiton):
    _max_instances = 12

    def __init__(self, name):
        self.name = name

    @property
    def data(self):
        return f'W okresie {self.name} zarobiono: {random.randint(0, 412343)}'


if __name__ == '__main__':
    finances = Finances()

    finances2 = Finances()
    assert finances2 is None

    period1 = Period('styczen')
    period2 = Period('luty')
    period3 = Period('marzec')
    period4 = Period('kwiecien')
    period5 = Period('maj')
    period6 = Period('czerwiec')
    period7 = Period('lipiec')
    period8 = Period('sierpiec')
    period9 = Period('wrzesien')
    period10 = Period('pazdziernik')
    period11 = Period('listopad')
    period12 = Period('grudzien')
    period13 = Period('dodatkowy')
    assert period13 is None

    finances.add_period(period1)
    finances.add_period(period2)
    finances.add_period(period3)
    finances.add_period(period4)
    finances.add_period(period5)
    finances.add_period(period6)
    finances.add_period(period7)
    finances.add_period(period8)
    finances.add_period(period9)
    finances.add_period(period10)
    finances.add_period(period11)
    finances.add_period(period12)

    finances.generate_file()