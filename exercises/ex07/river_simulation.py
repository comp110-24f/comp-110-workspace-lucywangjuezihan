"""File to simulate and view the River environment."""

__author__ = "730774129"

from exercises.ex07.river import River

my_river: River = River(10, 2)  # use positional arguments

my_river.view_river()
my_river.one_river_week()
