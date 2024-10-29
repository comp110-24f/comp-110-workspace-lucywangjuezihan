"""Create Dictionary Utility Functions"""

__author__ = "730774129"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """inverts the keys and the values"""
    inverted_dict: dict[str, str] = {}  # initialize an empty dictionary

    # iterate each key-value pair in the input_dict dictionary
    for key in input_dict:

        # to check if the value already exists as a key in the inverted dictionary
        if input_dict[key] in inverted_dict:
            raise KeyError("error message of your choice here!")

        # invert value as a key and the key as its corresponding value
        inverted_dict[input_dict[key]] = key
    return inverted_dict


def favorite_color(colors_dict: dict[str, str]) -> str:
    """returns the color that appears most frequently"""
    # Create a new dictionary that store the name and count in order
    color_count: dict[str, int] = {}
    # Define the data type and inital values of the variables
    max_num: int = 0
    most_popular_color: str = ""

    for name in colors_dict:

        # The dictionary value (i.e. color) needs to be defined every time
        # after the key (i.e. name) is iterated
        color: str = colors_dict[name]

        # to check if the color's names repeatedly appear in the color_count dictionary
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

        # Iterate over the original key (i.e. names) one by one to maintain the order
        # Update the count after iteration and mutation of its values
        count: int = color_count[color]

        # Iterate each count (generated by iterating each name)
        # to check the color is more popular
        if count > max_num:
            most_popular_color = color
            max_num = count
    return most_popular_color


# Same logic as the second favorite_color function
def count(input_count_list: list[str]) -> dict[str, int]:
    """return a dictionary of the counts of each item in the input list"""
    item_count: dict[str, int] = {}

    for item in input_count_list:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    return item_count


def alphabetizer(input_alphabet_list: list[str]) -> dict[str, list[str]]:
    """return a dictionary of letters and lists of words that belong to that letter"""
    alphabet_dict: dict[str, list[str]] = {}

    for word in input_alphabet_list:
        first_letter = word[0].lower()

        if first_letter not in alphabet_dict:
            alphabet_dict[first_letter] = []
        alphabet_dict[first_letter].append(word)
    return alphabet_dict


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """update the attendance_log with new attendance info"""
    if day not in attendance_log:
        attendance_log[day] = []

    # avoid repeating the same name for within a day
    if student not in attendance_log[day]:
        attendance_log[day].append(student)
