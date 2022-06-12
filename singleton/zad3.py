import random
from abc import ABC


class Singleton(ABC):
    instance: object

    def __new__(cls, *args, **kwargs):
        if hasattr(cls, 'instance'):
            return
        cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance



class Multiton(ABC):

    instances: list
    max: int

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instances'):
            cls.instances = []
        if len(cls.instances) < cls.max:
            ins = super().__new__(cls)
            cls.instances.append(ins)
            return ins
        return


class Finances(Singleton):

    def __init__(self):
        self.periods = []

    def add_period(self, period):
        self.periods.append(period)

    def show_raport(self):
        text = []
        for period in self.periods:
           text.append(period.data)

        file = ' \n '.join(text)
        return file


class Period(Multiton):
    max = 12

    def __init__(self, name):
        self.name = name

    @property
    def data(self):
        return f'{self.name} = {random.randint(0, 412343)}'


if __name__ == '__main__':
    finances = Finances()

    finances2 = Finances()

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

    finances.show_raport()