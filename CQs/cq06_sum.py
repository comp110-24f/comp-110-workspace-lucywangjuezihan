"""Summing the elements of a list using different loops"""

__author__ = "730774129"


def w_sum(vals: list[float]) -> float:
    """returns the sum of all elements using while loop"""
    index = 0
    output = 0.0

    while index < len(vals):
        output += vals[index]
        # set an original value and then add the values of elements one by one
        index += 1
    return output


def f_sum(vals: list[float]) -> float:
    """returns the sum of all elements using for loop"""
    output = 0.0

    for i in vals:
        output += i  # i represents each element in the list
    return output


def f_range_sum(vals: list[float]) -> float:
    """returns the sum of all elements using for range loop"""
    output = 0.0

    for i in range(0, len(vals)):
        output += vals[i]  # i represents the index in the range
    return output
