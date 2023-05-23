import pytest
from src.kbt.mapper import Mapper
from src.kbt.account import Account


def test_get_number_mapper_empty():
    data = []
    expected = []
    result = Mapper.map_lines_to_digits(data)
    assert result is not None
    assert isinstance(result, list)
    assert result == expected


@pytest.mark.parametrize("test_input,expected",
                         [([' _  _  _  _  _  _  _  _  _ ',
                            '| || || || || || || || ||_|',
                            '|_||_||_||_||_||_||_||_||_|', ""], "000000008 PENDING"),
                          (['    _  _     _  _  _  _  _ ',
                            '  | _| _||_||_ |_   ||_||_|',
                            '  ||_  _|  | _||_|  ||_| _|', ""], "123456789 PENDING"),
                          (['    _  _  _  _  _  _  _  _ ',
                            '| || || || || || || || || |',
                            '|_||_||_||_||_||_||_||_||_|', ""], "?00000000 PENDING"),
                          ([' _  _  _  _  _  _  _  _    ',
                            '| || || || || || || ||_   |',
                            '|_||_||_||_||_||_||_| _|  |', ""], "000000051 PENDING")])
def test_get_number_mapper(test_input, expected):
    result = Mapper.map_lines_to_digits(test_input)[0]
    account = Account(result)
    assert result is not None
    assert isinstance(result, list)
    assert result != []
    assert str(account) == expected
