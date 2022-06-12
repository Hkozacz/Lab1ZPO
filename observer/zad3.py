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

    def __init__(self):
        self.listeners = []
        self.choices = {
            "1": bigger_than_zero,
            "2": equal_three,
            "3": is_even,
        }

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        self.listeners.pop(listener.index(listener))

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
                print("Wybierz: \n [1] x > 0 \n [2] x == 3 \n [3] x/2")
                listener = input()
                self.add_listener(self.choices[listener])
            self.trigger_listener(user_input)

    def trigger_listener(self, number):
        for listener in self.listeners:
            listener(number)


