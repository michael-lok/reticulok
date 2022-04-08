import pytest

from reticulok.leetcode.medium import *


def test_int_to_roman():
    assert int_to_roman(1) == "I"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(3999) == "MMMCMXCIX"
