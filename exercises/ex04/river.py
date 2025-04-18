"""File to define River class."""

__author__ = "730567850"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Class for river."""

    day: int
    bears: list  # type: ignore
    fish: list  # type: ignore

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages of fish."""
        surviving_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        """Determine number of fish bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Check the hunger of the bears."""
        surviving_bears: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Fish make more fish."""
        guppy = (len(self.fish) // 2) * 4
        count = 0
        while count < guppy:
            self.fish.append(Fish())
            count += 1
        return None

    def repopulate_bears(self):
        """Bears make more bears."""
        baby_bear = len(self.bears) // 2
        count = 0
        while count < baby_bear:
            self.bears.append(Bear())
            count += 1
        return None

    def view_river(self):
        """Print statements of bear and fish populations on day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Days in a week!"""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Remove fish from the river."""
        num_fish = len(self.fish)
        if num_fish < amount:
            amount = num_fish
        count = 0
        while count < amount:
            self.fish.pop(0)
            count += 1
        return None
