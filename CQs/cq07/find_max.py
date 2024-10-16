__author__ = "730774129"


def find_and_remove_max(a: list[int]) -> int:
    """find and return the largest number in the input list"""

    index: int = 1
    # when comparing values of every number, set the index to the 2nd number

    if len(a) == 0:
        return -1  # specify the edge case
    else:
        # to avoid edge case of no elements in an array, put it behind edge case testing
        # need to identify what the data type is for autograders to run
        number: int = a[0]
        while index < len(a):
            if number < a[index]:
                number = a[index]
            index += 1

    index = 0

    while index < len(a):
        if a[index] == number:
            a.pop(index)  # list.pop function requires the specific index of the element
        else:  # pop function pops the number and the latter number moves to the front
            index += 1

    # put the return function at the end bc everything goes behind it would be ignored
    return number
