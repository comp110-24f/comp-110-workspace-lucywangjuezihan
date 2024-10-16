__author__ = "730774129"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_expected_value() -> None:
    """test the find_and_remove_max function"""
    a: list[int] = [5, 8, 10, 3]
    assert find_and_remove_max(a) == 10


def test_find_and_remove_max_mutation() -> None:
    """test the find_and_remove_max function"""
    a: list[int] = [5, 8, 10, 3]
    find_and_remove_max(a)
    assert a == [5, 8, 3]


def test_find_and_remove_max_unconventional() -> None:
    """test the find_and_remove_max function"""
    a: list[int] = []
    assert find_and_remove_max(a) == -1
