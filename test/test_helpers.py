import pytest
from src.kbt.helpers import divide_by_lines, numbers


def test_divide_by_lines_error():
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    with pytest.raises(Exception) as e:
        divide_by_lines(data, None)
    assert "Error trying to divide the data in None" in str(e)


def test_divide_by_lines_error():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
    length = 4
    result = divide_by_lines(data, length)
    assert result is not None
    assert result == expected, "Result has to be like expected"


@pytest.mark.parametrize("test_input,expected",
                         [(" _ | ||_|", 0), ("     |  |", 1), (" _  _||_ ", 2), (" _  _| _|", 3),
                          ("   |_|  |", 4), (" _ |_  _|", 5), (" _ |_ |_|", 6), (" _   |  |", 7),
                          (" _ |_||_|", 8), (" _ |_| _|", 9)])
def test_numbers_invalid(test_input, expected):
    result = numbers[test_input]
    assert result is not None
    assert result == expected, "Result has to be like expected"
