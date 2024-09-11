"""Input the number of guests and output the expected cost of the tea party."""

__author__: str = "730774129"


# When printing functions that outputs an int or float value,
# the data type needs to be changed to str first.
def main_planner(guests: int) -> None:
    """Call functions below to calculate the total cost based on # of guests."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """To calculate the number of tea bags needed based on the number of people."""
    return people * 2


# When calling another function in this function,
# use the key-word argument by putting the local variable,
# "=", and the argument in the parentheses.
def treats(people: int) -> int:
    """To calculate the number of treats needed based on the number of people."""
    return round(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """To calculate the total cost based on the counts of tea and treats."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
