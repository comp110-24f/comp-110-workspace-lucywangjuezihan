"""Exploring linked list utils in class."""

from __future__ import annotations

__author__ = "730774129"


class Node:
    """Define the Node class and attributes."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """New Node with value and next attributes."""
        self.value = val
        # every Node object will have either a Node or None for the next attribute
        self.next = next

    # for magic method, the parameter can only have self
    # because when runnning it, it only prints or returns itself
    def __str__(self) -> str:
        """String magic method that returns and prints all strings."""
        rest: str
        if self.next is None:  # Base case, when the recursive structure will end
            rest = "None"
        else:
            rest = str(self.next)
        # f string below is the same as: str(self.value) + " -> " + str(rest)
        return f"{self.value} -> {rest}"  # print everything in the {} as strings


two: Node = Node(2, None)  # use positional arguments when creating objects in class
one: Node = Node(1, two)

# output: <__main__.Node object at 0x100633950>
# Python stores this Node object "one" at this registered address in the heap
print(one)  # output: 1 -> 2 -> None


def to_str(head: None | Node) -> str:
    """Define the to_str method in the Node class."""
    if head is None:
        return "None"
    else:
        # from this line, we know it's a recursive structure
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))


def last(head: Node) -> int:
    """Return the last value in a non-empty list."""
    if head.next is None:  # Base case
        return head.value
    else:
        return last(head.next)


print(last(one))  # output: 2
# print(last(None))  # edge case testing


def recursive_range(start: int, end: int) -> Node | None:
    """Define the recursive_range method in the Node class."""
    # Edge case
    if start > end:
        raise Exception("Start shouldn't be bigger than End")

    # Base case
    if start == end:
        return None

    # Recursive case
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
    return Node(first, rest)


lots_of_nodes: Node | None = recursive_range(1, 100)
print(lots_of_nodes)
# print(recursive_range(15, 1))


def value_at(head: Node | None, index: int) -> int:
    """To return the value of the Node stored at the given index."""
    # Edge case
    # Python prefers "is" when compares to None only, rather than "=="
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    # Base case
    elif index == 0:
        return head.value

    # Recursive case
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum value in the linked list."""
    max_value: int = 0

    # Edge case
    if head is None:
        raise ValueError("Cannot call max with None")

    else:
        max_value = head.value
        # Base case
        if head.next is None:
            return max_value

        # Recursive case
        else:
            if head.value >= max(head.next):
                return max_value
            else:
                return max(head.next)


# Use command + forward slash to comment out block codes

# The find_max function is the same as max function above
# def find_max(head: Node | None) -> int:
#     if head is None:
#         raise ValueError("Cannot call find_max with None")

#     if head.next is None:
#         return head.value

#     rest_max = find_max(head.next)
#     if head.value > rest_max:
#         return head.value
#     else:
#         return rest_max


def linkify(items: list[int]) -> Node | None:
    """Return a Linked List of Nodes with the same values in same order as input."""
    # Edge case
    if len(items) == 0:
        return None

    # When creating Node objects, write in the farmat of "Node(value, next)"
    # Convert the whole list of items into a list of Node
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Scale each node in the linked list by the given factor."""
    # Edge case: empty linked list
    if head is None:
        return None

    return Node(head.value * factor, scale(head.next, factor))
