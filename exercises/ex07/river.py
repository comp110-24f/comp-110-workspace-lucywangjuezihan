"""File to define River class."""

__author__ = "730774129"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Define the River class and attributes."""

    day: int  # tells you what day of the river’s lifecycle you are modeling
    bears: list[Bear]  # a list of Bears that stores the river’s bear population
    fish: list[Fish]  # a list of Fish that stores the river’s fish population

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
        """Remove aging animals from the river."""
        # list[Bear] means a list of Bear objects from the Bear class
        survived_bear: list[Bear] = []
        # the line below means for each bear object from the self.bears list
        for bear in self.bears:
            if bear.age <= 5:
                survived_bear.append(bear)
        # assign copied list to self.bears so that it can be called outside of method
        self.bears = survived_bear

        survived_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                survived_fish.append(fish)
        self.fish = survived_fish

        return None

    def bears_eating(self):
        """Define the bears_eating method in the Bear class."""
        for bear in self.bears:  # loop through each bear in the self.bears list
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Define the check_hunger method in the Bear class."""
        survived_bear: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                survived_bear.append(bear)
        self.bears = survived_bear

        return None

    def repopulate_fish(self):
        """Define the repopulate_fish method in the Fish class."""
        for _ in range(0, len(self.fish) // 2 * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Each pair of Bear's will produce 1 offspring."""
        for _ in range(0, len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Print out the river status for the users."""
        print("~~~ Day " + str(self.day) + ": ~~~")
        print("Fish population: " + str(len(self.fish)))
        print("Bear population: " + str(len(self.bears)))
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
        """Run the one_river_day() method for 7 days or 1 week."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int):
        """Remove the frontmost amount of Fish from the River."""
        for i in range(0, amount):
            self.fish.pop(i)
