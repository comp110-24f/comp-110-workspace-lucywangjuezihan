"""File to define Bear class."""

__author__ = "730774129"


class Bear:
    """Define the Bear class and attributes."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize the Bear class."""
        self.age: int = 0
        self.hunger_score: int = 0

        return None

    def one_day(self):
        """Define the one_day method in the Bear class."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Update the Bear's hunger_score based on num of fish it eats."""
        self.hunger_score += num_fish
