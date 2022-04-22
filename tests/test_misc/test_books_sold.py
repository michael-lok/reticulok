import pytest

from reticulok.misc import get_nth_highest_sold


def test_books_sold_correct():
    assert get_nth_highest_sold(
        [(3.99, 6), (9.99, 3), (8.99, 6), (4.25, 1)],
        2
    ) == (9.99, 3)
    assert get_nth_highest_sold(None, 4) == None
    assert get_nth_highest_sold(
        [(1.99, 10), (0.99, 9), (5.99, 9), (10.99, 10)],
        4
    ) == None
