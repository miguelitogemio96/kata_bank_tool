from src.kbt.fixer import Fixer
from src.kbt.helpers import numbers
from src.kbt.digit import Digit
from src.kbt.account import Account
from src.kbt.validator import Validator


DIG_NUMS = list(numbers.keys())[0:11]


def apply_Checksum(account_number: str, mod=11) -> bool:
    length = len(account_number)
    total_sum = sum([(int(account_number[i]) * (length - i)) for i in range(length)])
    return total_sum % mod == 0


def is_in_db(acc_num: str):
    db_accs = ["000000000", "000000051", "123456789", "333393333", "777777177", "711111111"]
    return acc_num in db_accs


def test_fixer_ill():
    wrong_digit = "     |   "
    list_digits = [Digit(DIG_NUMS[i])
                   for i in [0, 0, 0, 0, 0, 0, 0, 5]] + [Digit(wrong_digit)]
    acc = Account(list_digits)
    acc.state = 'ILL'
    result = Fixer.find_valid_account(acc, Validator.is_valid_account_number)
    assert acc is not None
    assert isinstance(acc, Account)
    assert acc.account_number != ""
    assert '?' in acc.account_number
    assert acc.state == 'ILL'
    assert str(result) == "000000051 OK"


def test_fixer_err_1():
    list_digits = [Digit(DIG_NUMS[i]) for i in [0, 0, 0, 0, 0, 0, 0, 6, 1]]
    acc = Account(list_digits)
    acc.state = 'ERR'
    result = Fixer.find_valid_account(acc, Validator.is_valid_account_number, [is_in_db, apply_Checksum])
    assert acc is not None
    assert isinstance(acc, Account)
    assert acc.account_number != ""
    assert acc.account_number == "000000061"
    assert str(result) is not None
    assert acc.state == 'OK'
    assert str(result) == "000000051 OK"


def test_fixer_err_2():
    list_digits = [Digit(DIG_NUMS[i]) for i in [0, 0, 0, 0, 0, 0, 0, 0, 8]]
    acc = Account(list_digits)
    acc.state = 'ERR'
    result = Fixer.find_valid_account(acc, Validator.is_valid_account_number, [is_in_db, apply_Checksum])
    assert acc is not None
    assert isinstance(acc, Account)
    assert acc.account_number != ""
    assert acc.account_number == "000000008"
    assert acc.state == 'ERR'
    assert str(result) == "000000000 OK"
