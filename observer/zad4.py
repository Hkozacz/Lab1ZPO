import abc
import random
from abc import ABC


class Board:
    pointers_list: list

    listeners: list

    def __init__(self):
        self.listeners = []
        self.pointers_list = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        self.listeners.pop(listener.index(listener))

    @staticmethod
    def generate_pointers():
        return random.randint(0, 100), random.randint(0, 100)

    def click(self):
        pointer = self.generate_pointers()
        self.pointers_list.append(pointer)
        for listener in self.listeners:
            listener.execute(self.pointers_list)


class Observer(ABC):

    @staticmethod
    @abc.abstractmethod
    def execute(pointers):
        raise NotImplemented


class Panel1(Observer):

    @staticmethod
    def execute(pointers):
        print('Liczba punktow: ', len(pointers))


class Panel2(Observer):

    @staticmethod
    def execute(pointers):
        print(pointers)


class Panel3(Observer):

    @staticmethod
    def execute(pointers):
        print('Tutaj bylby wykres slupkowy :)')


if __name__ == '__main__':
    board = Board()
    panel1 = Panel1()
    panel2 = Panel2()
    panel3 = Panel3()
    board.add_listener(panel1)
    board.add_listener(panel2)
    board.add_listener(panel3)

    board.click()
    board.click()
    board.click()
    board.click()
    board.click()
    board.click()

