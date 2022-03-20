def bigger_than_zero(number):
    if number > 0:
        print(f"Liczba {number} jest wieksza niz zero")


def equal_three(number):
    if number == 3:
        print(f"Liczba {number} jest rowna trzy")


def is_even(number):
    if number % 2 == 0:
        print(f"Liczba {number} jest podzielna przez dwa")


class Publisher:
    listeners_to_add = {
        "1": bigger_than_zero,
        "2": equal_three,
        "3": is_even,
    }
    listeners = []

    @classmethod
    def add_listener(cls, listener):
        cls.listeners.append(listener)

    @classmethod
    def remove_listener(cls, listener):
        cls.listeners.pop(listener.index(listener))

    @staticmethod
    def get_input():
        return input('Podaj liczbe: ')

    def run(self):
        while 1:
            try:
                user_input = int(self.get_input())
            except ValueError:
                break
            if user_input == 0:
                print("choose:", "[1] x > 0", "[2] x == 3", "[3] x/2", sep="\n")
                listener = input()
                self.add_listener(self.listeners_to_add[listener])
            self.trigger_listener(user_input)

    @classmethod
    def trigger_listener(cls, number):
        for listener in cls.listeners:
            listener(number)


