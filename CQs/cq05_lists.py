"""Mutating functions."""

__author__ = "730774129"


def manual_append(list1: list[int], number1: int) -> None:
    """Append the number at the end of the list"""
    list1.append(number1)


def double(list2: list[int]) -> None:
    """multiplying every element in the list2 by 2"""
    index = 0

    while index < len(list2):  # use a while loop to mutate every item in the list
        list2[index] = list2[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
