from types import FunctionType as func_type
from .account import Account
from .helpers import numbers, type_character_dig_number, posible_numbers


class Fixer:
    @staticmethod
    def find_valid_account(acc: Account, is_valid: func_type,
                           extraValidations: list[func_type] = []):
        if acc.state == 'ILL':
            Fixer.try_fix_ill(acc, is_valid, extraValidations)
        if acc.state == "ERR":
            Fixer.try_fix_err(acc, is_valid, extraValidations)
        return acc

    @staticmethod
    def try_fix_ill(acc: Account, is_valid, extraValidations) -> None:
        ill_index = acc.account_number.find("?")
        ill_digit = acc.digits[ill_index].digital_digit
        for i in range(len(ill_digit)):
            if ill_digit[i] != " ":
                new_digit = ill_digit[:i] + " " + ill_digit[i+1:]
                Fixer.verify_add_fixed_account(new_digit, acc, ill_index,
                                               is_valid, extraValidations)

        for i, char in type_character_dig_number.items():
            new_digit = list(ill_digit)
            if ill_digit[i] == " ":
                new_digit[i] = char
                new_digit = "".join(new_digit)
                Fixer.verify_add_fixed_account(new_digit, acc, ill_index,
                                               is_valid, extraValidations)

    @staticmethod
    def try_fix_err(acc: Account, is_valid, extraValidations) -> None:
        for i in range(len(acc.account_number)):
            new_curr = list(acc.account_number)
            for try_digit in posible_numbers[acc.account_number[i]]:
                new_curr[i] = try_digit
                curr_joined = "".join(new_curr)
                if is_valid(curr_joined, extraValidations):
                    acc.add_amb(curr_joined)

    @staticmethod
    def verify_add_fixed_account(new_digit: str, acc: Account, ill_index: int,
                                 is_valid, extraValidations):
        if new_digit in numbers.keys():
            new_acc = acc.replace_digit_at(str(numbers[new_digit]), ill_index)
            if is_valid(new_acc, extraValidations):
                acc.add_amb(new_acc)
