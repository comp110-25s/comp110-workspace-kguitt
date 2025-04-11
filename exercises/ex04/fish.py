"""File to define Fish class."""

__author__ = "730567850"


class Fish:
    age: int

    def __init__(self):
        self.age: int = 0
        return None

    def one_day(self):
        self.age += 1
        return None
