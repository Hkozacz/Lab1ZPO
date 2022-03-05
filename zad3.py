class CarSpeed:
    speed: int

    @classmethod
    def get_max_speed(cls):
        return cls.speed


class Maluch(CarSpeed):
    speed = 100


class Ford(CarSpeed):
    speed = 190


class Porshe(CarSpeed):
    speed = 280