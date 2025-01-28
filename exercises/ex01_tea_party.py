"""Compute quantity of tea bags, quantity of treats, and cost for a cozy tea party contingent on number of guests."""

__author__: str = "730567850"


def main_planner(guests: int) -> None:
    """Call each function and produce printed output based on number of guests."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Compute quantity of tea bags."""
    return 2 * people


def treats(people: int) -> int:
    """Compute quantity of treats."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Compute total cost of tea and treats."""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
