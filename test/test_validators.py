import pytest
from src.kbt.validator import Validator
from src.kbt.account import Account
from src.kbt.digit import Digit
from src.kbt.file_accounts import FileAccounts


def apply_Checksum(account_number: str, mod=11) -> bool:
    length = len(account_number)
    total_sum = sum([(int(account_number[i]) * (length - i)) for i in range(length)])
    return total_sum % mod == 0


def is_in_db(acc_num: str):
    db_accs = ["000000000", "000000051", "123456789", "333393333", "777777177", "711111111"]
    return acc_num in db_accs


@pytest.mark.parametrize("test_input, expected",
                         [("222222222", False),
                          ("888888888", False),
                          ("012345678", False),
                          ("711111111", True),
                          ("490867715", True),
                          ("123456789", True)])
def test_checksum_validation(test_input, expected):
    empty_acc = Account([Digit("") for _ in range(9)])
    empty_acc.account_number = test_input
    result = Validator.is_valid_account_number(test_input, [apply_Checksum])
    assert result is not None
    assert result == expected


@pytest.mark.parametrize("test_input, expected",
                         [("000000000", True),
                          ("000000051", True),
                          ("123456789", True),
                          ("333393333", True),
                          ("777777177", True),
                          ("711111111", True),
                          ("111111111", False),
                          ("222222222", False),
                          ("333333333", False),
                          ("490867715", False),
                          ("777311233", False),
                          ("888888888", False)])
def test_is_in_database_validation(test_input, expected):
    empty_acc = Account([Digit("") for _ in range(9)])
    empty_acc.account_number = test_input
    result = Validator.is_valid_account_number(test_input, [is_in_db])
    assert result is not None
    assert result == expected


@pytest.mark.parametrize("test_input, expected",
                         [("222222222", False),
                          ("888888888", False),
                          ("012345678", False),
                          ("711111111", True),
                          ("490867715", False),  # Beacuse it's not in the DB
                          ("123456789", True)])
def test_apply_validations_acc_instance(test_input, expected):
    empty_acc = Account([Digit("") for _ in range(9)])
    empty_acc.account_number = test_input
    result = Validator.is_valid_account_instance(empty_acc, [apply_Checksum, is_in_db])
    assert result is not None
    assert result == expected


@pytest.mark.parametrize("test_input", [None, "", [], 711111111])
def test_apply_validation_error(test_input):
    with pytest.raises(Exception) as e:
        Validator.apply_validations_to_Accounts(test_input)
    assert "Empty or incorrect data applying validations to accounts" in str(e)


def test_apply_validation_list_accounts():
    accounts_values = ["000000051", "123456789", "333393333", "777777177", "111111111", "222222222"]
    empty_accs = [Account([Digit("") for _ in range(9)]) for _ in range(6)]
    for i in range(6):
        empty_accs[i].account_number = accounts_values[i]
    Validator.apply_validations_to_Accounts(empty_accs, apply_Checksum, is_in_db)
    fa = FileAccounts(empty_accs)
    assert empty_accs is not None
    assert fa is not None
    assert str(fa) is not None
    assert str(fa) == "000000051 OK\n123456789 OK\n333393333 OK\n777777177 OK\n711111111 OK\n"\
                      + "222222222 ERR"


def test_apply_validation_list_accounts_extra_validation():
    accounts_values = ["000000051", "123456789", "333393333", "777777177", "111111111", "222222222"]
    empty_accs = [Account([Digit("") for _ in range(9)]) for _ in range(6)]
    for i in range(6):
        empty_accs[i].account_number = accounts_values[i]
    Validator.apply_validations_to_Accounts(empty_accs, lambda acc_numb: acc_numb == "333393333")
    fa = FileAccounts(empty_accs)
    assert empty_accs is not None
    assert fa is not None
    assert str(fa) is not None
    assert str(fa) == "000000051 ERR\n123456789 ERR\n333393333 OK\n777777177 ERR\n"\
                      + "111111111 ERR\n222222222 ERR"
