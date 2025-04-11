"""File to define Fish class."""

__author__ = "730567850"


class Fish:
    """Class for fishies."""

    age: int

    def __init__(self):
        """Initialize fishies."""
        self.age: int = 0
        return None

    def one_day(self):
        """Update fish age by one."""
        self.age += 1
        return None
