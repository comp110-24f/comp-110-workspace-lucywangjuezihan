__author__ = "730774129"


def only_evens(a_list: list[int]) -> list[int]:
    """return a list that only return even numbers"""
    index = 0
    outcome_list: list[int] = []

    while index < len(a_list):
        if a_list[index] % 2 == 0:
            # when add an element in a list, simply
            # use the original_list_name.append(element)
            outcome_list.append(a_list[index])
        index += 1
    return outcome_list


def sub(b_list: list[int], start_index: int, end_index: int) -> list[int]:
    """generate a subset of the input list,
    between the start index and the end index - 1"""
    outcome_list: list[int] = []

    if len(b_list) == 0:
        return outcome_list
    if start_index >= len(b_list):
        return outcome_list
    if end_index <= 0:
        return outcome_list

    if start_index < 0:
        start_index = 0
    if end_index > len(b_list):
        end_index = len(b_list)

    for i in range(start_index, end_index):
        outcome_list.append(b_list[i])  # i represents the index of the list
    return outcome_list


def add_at_index(c_list: list[int], element: int, index: int) -> None:
    """modify the input list to place the element at the given index"""

    if index < 0 or index > len(c_list):
        raise IndexError("Index is out of bounds for the input list")
    # add space at the end of the list, then shift everything to the right
    # of the index to make space for the input element

    if index == len(c_list):
        c_list.append(element)
        return

    c_list.append(0)

    # start from the right side of the list to avoid overwriting
    for i in range(len(c_list) - 1, index, -1):
        c_list[i] = c_list[i - 1]
    c_list[index] = element
    return
