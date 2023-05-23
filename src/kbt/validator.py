from .exceptions import DataTypeError
from .account import Account
from .fixer import Fixer
from types import FunctionType as func


class Validator:
    def apply_validations_to_Accounts(accounts: list[Account], *validations: list[func]) -> None:
        if not accounts or not isinstance(accounts, list):
            raise DataTypeError(f"Empty or incorrect data applying validations to accounts")
        for account in accounts:
            if Validator.is_valid_account_instance(account, validations):
                account.state = "OK"
                continue
            account.state = "ILL" if '?' in account.account_number else "ERR"
            Fixer.find_valid_account(account, Validator.is_valid_account_number, validations)

    @staticmethod
    def is_valid_account_instance(acc: Account, validations: list[func] = []) -> bool:
        if acc is None or not isinstance(acc, Account) or len(acc.account_number) == 0:
            raise DataTypeError(
                f"Empty or incorrect data applying validations to account instance: {acc}"
                )
        return '?' not in acc.account_number and Validator.is_valid_account_number(
            acc.account_number, validations)

    @staticmethod
    def is_valid_account_number(account_number: str, validations: list) -> bool:
        if '?' in account_number: return False
        list_validations = list(validations)
        answers = [validation(account_number) for validation in list_validations]
        return sum(answers) == len(validations)
