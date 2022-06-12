import random


class Board:

    def __init__(self):
        self.listeners = []
        self.points = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        self.listeners.pop(listener.index(listener))

    def execute(self):
        pointer = random.randint(0, 100), random.randint(0, 100)
        self.points.append(pointer)
        for listener in self.listeners:
            listener.execute(self.points)


class Panel1:

    @staticmethod
    def execute(pointers):
        print('Liczba punktow: ', len(pointers))


class Panel2:

    @staticmethod
    def execute(pointers):
        print(pointers)


class Panel3:

    @staticmethod
    def execute(pointers):
        print('Wykres dla ')
        print(pointers)


if __name__ == '__main__':
    board = Board()
    panel1 = Panel1()
    panel2 = Panel2()
    panel3 = Panel3()

    for panel in [panel1, panel2, panel3]:
        board.add_listener(panel)

    for i in range(0, 15):
        board.execute()


