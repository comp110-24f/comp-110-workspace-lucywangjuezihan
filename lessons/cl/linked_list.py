"""Exploring linked list utils in class."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        # every Node object will have either a Node or None for the next attribute
        self.next = next

    def __str__(self) -> str:
        rest: str
        if self.next is None:  # Base case, when the recursive structure will end
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"  # print everything in the {} as strings


two: Node = Node(2, None)  # use positional arguments when creating objects in class
one: Node = Node(1, two)

# output: <__main__.Node object at 0x100633950>
# Python stores this Node object "one" at this registered address in the heap
print(one)  # output: 1 -> 2 -> None


def to_str(head: None | Node) -> str:
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
    if start > end:
        raise Exception("Start shouldn't be bigger than End")
    # Base Case
    if start == end:
        return None
    # Recursive case
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
    return Node(first, rest)


lots_of_nodes: Node | None = recursive_range(1, 100)
print(lots_of_nodes)
print(recursive_range(15, 1))
