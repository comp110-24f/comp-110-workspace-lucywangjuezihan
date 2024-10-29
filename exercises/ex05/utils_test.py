__author__ = "730774129"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_return_value() -> None:
    """test the return value of the only_evens function"""
    a_list: list[int] = [1, 2, 3]
    assert only_evens(a_list) == [2]


def test_only_evens_no_mutation() -> None:
    """test the non-mutation nature of the only_evens function"""
    a_list: list[int] = [1, 2, 3]
    only_evens(a_list)
    assert a_list == [1, 2, 3]


def test_only_evens_edge_case() -> None:
    """test the edge case of the only_evens function"""
    a_list: list[int] = [3, 5, 7]
    assert only_evens(a_list) == []


def test_sub_return_value() -> None:
    """test the return value of the sub function"""
    b_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(b_list, 2, 4) == [3, 4]


def test_sub_no_mutation() -> None:
    """test the non-mutation nature of the sub function"""
    b_list: list[int] = [1, 2, 3, 4, 5]
    sub(b_list, 2, 4)
    assert b_list == [1, 2, 3, 4, 5]


def test_sub_edge_case() -> None:
    """test the edge case of the sub function"""
    b_list: list[int] = []
    assert sub(b_list, 0, 0) == []


def test_add_at_index_return_value() -> None:
    """test the return value of add_at_index function"""
    c_list: list[int] = [1, 2, 3]
    add_at_index(c_list, 2, 1)
    assert c_list == [1, 2, 2, 3]


def test_add_at_index_no_mutation() -> None:
    """test the mutation nature of the add_at_indexs function"""
    c_list: list[int] = [1, 2, 3]
    add_at_index(c_list, 4, 2)
    assert c_list == [1, 2, 4, 3]


def test_add_at_index_edge_case() -> None:
    """test the edge case of the add_at_index function"""
    c_list: list[int] = [3, 5, 7]
    add_at_index(c_list, 14, 2)
    assert c_list == [3, 5, 14, 7]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        c_list: list[int] = [3, 5, 7]
        add_at_index(c_list, 3, 4)
        # an IndexError is raised for the case
        # when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
