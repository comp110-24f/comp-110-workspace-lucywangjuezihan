"""Playing around the list"""

# Creating a list variable that's initially
my_numbers: list[float] = []

# Let's add ("append") a value to the end of the list!
my_numbers.append(1.5)
print(my_numbers)

# Make a list of numbers
game_points: list[int] = [102, 86, 94]
print(game_points[2])

# Changing the value of an item
game_points[1] = 72
print(game_points)

# the number is the index of the item that we wish to pop off
game_points.pop(1)
print(len(game_points))

# Can we change individual chars in strings this way?
my_name: str = "Izzi"

name_as_list: list[str] = list(my_name)
print(name_as_list)

name_as_list[3] = "y"
print(name_as_list)
name_as_list.append("e")
print(name_as_list)

# Insert an index in the middle of the a list
name_as_list.insert(4, "i")
print(name_as_list)

grocery_list: list[str] = ["banana", "apple", "carrot"]
grocery_list.append("beans")
print(grocery_list)
