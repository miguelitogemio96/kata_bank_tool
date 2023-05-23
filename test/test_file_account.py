from src.kbt.file_accounts import FileAccounts
from src.kbt.helpers import numbers
from src.kbt.digit import Digit
from src.kbt.account import Account


DIG_NUMBERS = list(numbers.keys())


def test_file_accounts_empty():
    fa = FileAccounts()
    assert fa is not None
    assert isinstance(fa, FileAccounts)
    assert fa.accounts == []
    assert str(fa) == ""


def test_file_accounts_filled():
    list_digits = [Digit(dig_number) for dig_number in DIG_NUMBERS[:11]]
    accounts = [Account(list_digits[:9]), Account(list_digits[1:10])]
    fa = FileAccounts(accounts)
    assert fa is not None
    assert isinstance(fa, FileAccounts)
    assert fa.accounts == accounts
    assert str(fa) == "012345678 PENDING\n123456789 PENDING"
