__author__ = 730774129
"""Practice while loop"""


def num_instances1(phrase: str, search_char: str) -> int:
    """return the count of occurrences of search_char in phrase"""
    condition: bool = True
    count: int = 0
    index: int = 0
    while condition:
        if index >= len(phrase):
            condition = False
        else:
            if search_char == phrase[index]:
                count = count + 1
        index = index + 1
    return count


def num_instances2(phrase: str, search_char: str) -> int:
    """Second version: return the count of occurrences of search_char in phrase"""
    count: int = 0
    index: int = 0
    while index <= (len(phrase) - 1):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count
