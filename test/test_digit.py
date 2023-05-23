import pytest
from src.kbt.digit import Digit


@pytest.mark.parametrize("test_input,expected",
                         [(" _ | ||_|", "0"), ("     |  |", "1"), (" _  _||_ ", "2"),
                          (" _  _| _|", "3"), ("   |_|  |", "4"), (" _ |_  _|", "5"),
                          (" _ |_ |_|", "6"), (" _   |  |", "7"), (" _ |_||_|", "8"),
                          (" _ |_| _|", "9")])
def test_get_number_mapper_ok(test_input, expected):
    new_digit = Digit(test_input)
    assert new_digit is not None
    assert new_digit != ""
    assert new_digit.digit == expected
    assert str(new_digit) == expected


def test_get_set_digit():
    dig_digit = " _ | ||_|"
    new_digit = Digit(dig_digit)
    new_digit.digit = 9
    assert new_digit.digit is not None
    assert new_digit.digit == 9


def test_get_set_digital_digit():
    old_dig_digit = " _ | ||_|"
    new_dig_digit = " _ | ||_|"
    new_digit = Digit(old_dig_digit)
    new_digit.digital_digit = new_dig_digit
    assert new_digit.digital_digit is not None
    assert new_digit.digital_digit == new_dig_digit
