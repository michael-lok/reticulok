import pytest

from reticulok.leetcode.easy import *


def test_two_sum_correct():
    assert two_sum([1, 2, 4], 6) == [1, 2]
    assert two_sum([3, 4, 6, 2, 1, 9, 4, 2], 15) == [2, 5]


def test_two_sum_exception():
    with pytest.raises(ValueError):
        two_sum([1, 2, 4], 10)
