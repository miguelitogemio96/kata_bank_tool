import pytest
from src.kbt.digit import Digit
from src.kbt.account import Account
from src.kbt.helpers import numbers


DIG_NUMBERS = list(numbers.keys())


@pytest.mark.parametrize("test_input, expected",
                         [(DIG_NUMBERS[1:10], ("123456789", "PENDING")),
                          (DIG_NUMBERS[:9], ("012345678", "PENDING")),
                          ([*DIG_NUMBERS[1:9], "xyz"], ("12345678?", "PENDING")),])
def test_create_accounts(test_input, expected):
    list_digits = [Digit(dig_number) for dig_number in test_input]
    new_account = Account(list_digits)
    expected_acc, expected_state = expected
    assert new_account is not None
    assert new_account.amb == []
    assert len(new_account.digits) == len(test_input)
    assert new_account.account_number == expected_acc
    assert new_account.state == expected_state
    assert str(new_account) == f"{expected_acc} {expected_state}"


@pytest.mark.parametrize("test_input", [None, [], "Test", 1000])
def test_create_account_error(test_input):
    with pytest.raises(Exception) as e:
        Account(test_input)
    assert "Empty or incorrect data generating Account Number:" in str(e)
