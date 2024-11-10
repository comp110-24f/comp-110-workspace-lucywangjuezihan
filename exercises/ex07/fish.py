"""File to define Fish class."""

__author__ = "730774129"


class Fish:
    """Define the Fish class and attributes."""

    age: int

    def __init__(self):
        """Initialize the Fish class."""
        self.age: int = 0
        return None

    def one_day(self):
        """Define the one_day method in the Fish class."""
        self.age += 1
        return None
