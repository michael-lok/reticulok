import pytest

from reticulok.leetcode.easy import *


def test_two_sum_correct():
    assert two_sum([1, 2, 4], 6) == [1, 2]


def test_two_sum_exception():
    with pytest.raises(ValueError):
        two_sum([1, 2, 4], 10)
