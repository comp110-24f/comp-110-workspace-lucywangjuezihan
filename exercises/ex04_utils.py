"""explore list utilities"""

__author__ = "730774129"


def all(list_all: list[int], number1: int) -> bool:
    """to see if all the ints in the list are the same as the given int"""
    index = 0

    if len(list_all) == 0:
        return False  # the condition when the list is empty needs to be specified

    while index < len(list_all):
        if list_all[index] != number1:
            return False  # the output will be False unless every index is correct
        index += 1
    return True


def max(list_max: list[int]) -> int:
    """return the largest integer from a list of integers"""

    if len(list_max) == 0:
        raise ValueError("max() arg is an empty List")

    # assign the max value to the first element and then compare
    max_value: int = list_max[0]
    # the index starts from the second element for comparison
    index = 1

    while index < len(list_max):
        if list_max[index] > max_value:
            max_value = list_max[index]
        index += 1  # the index should be raised after checking each number
    return max_value  # the return value needs to be outside of the if loop


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This function will return 'True' if lists are equal"""

    if len(list1) == 0 and len(list2) == 0:
        return True

    if len(list1) == 0 or len(list2) == 0:
        return False

    index = 0

    if len(list1) == len(list2):
        while index < len(list1):
            # use the if function for False if everything else
            # needs to be met in order for the boolean to be True
            if list1[index] != list2[index]:
                return False
            index += 1
        return True
    else:
        return False


def extend(a: list[int], b: list[int]) -> None:
    """append elements from list4 to the end of list3"""

    index = 0

    while index < len(b):
        a.append(b[index])  # an_array.append(number)
        index += 1
