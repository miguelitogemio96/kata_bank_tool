from .digit import Digit
from .exceptions import DataTypeError


class Account:
    def __init__(self, digits: list[Digit]) -> None:
        self.__digits = digits
        self.__account_number = self.__generate_account_number(digits)
        self.__amb = []
        self.__state = "PENDING"

    @property
    def account_number(self):
        return self.__account_number

    @property
    def digits(self):
        return self.__digits

    @property
    def state(self):
        return self.__state

    @property
    def amb(self):
        return self.__amb

    @state.setter
    def state(self, new_state):
        self.__state = new_state

    @account_number.setter
    def account_number(self, new_account_number):
        self.__account_number = new_account_number

    def __str__(self) -> str:
        if self.__state != "OK":
            if len(self.__amb) == 1:
                self.__account_number = self.__amb[0]
                self.__state = "OK"
            elif len(self.__amb) > 1:
                self.__state = "AMB"
                return f"{self.__account_number} {self.__state} {self.__amb}"

        return f"{self.__account_number} {self.__state}"

    @staticmethod
    def __generate_account_number(list_digits: list[Digit]):
        if list_digits is None or not isinstance(list_digits, list) or len(list_digits) == 0:
            raise DataTypeError(f"Empty or incorrect data generating Account Number: {list_digits}")
        return "".join([dig_acc.digit for dig_acc in list_digits])

    def replace_digit_at(self, char: str, pos: int) -> str:
        new_acc = [c for c in self.__account_number]
        new_acc[pos] = char
        return "".join(new_acc)

    def add_amb(self, acc_number: str):
        self.__amb.append(acc_number)
