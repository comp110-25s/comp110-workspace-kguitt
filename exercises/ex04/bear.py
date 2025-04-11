"""File to define Bear class."""

__author__ = "730567850"


class Bear:
    """Class for bears."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize bears info."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Increase value of age attribute by one and decrease hunger score by one each day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Update hunger score to increase by number of fish nom nom nom."""
        self.hunger_score += num_fish
        return None
