from .helpers import numbers


class Digit:
    def __init__(self, digital_digit: str) -> None:
        self.__digital_digit = digital_digit or ""
        self.__digit = self.__get_number_from_digital(digital_digit) or "?"

    @property
    def digit(self):
        return self.__digit

    @property
    def digital_digit(self):
        return self.__digital_digit

    @digit.setter
    def digit(self, new_digit):
        self.__digit = new_digit

    @digital_digit.setter
    def digital_digit(self, new_digital_digit):
        self.__digital_digit = new_digital_digit

    def __str__(self) -> str:
        return self.__digit

    @staticmethod
    def __get_number_from_digital(dig_number: str) -> str:
        if dig_number in numbers.keys():
            return str(numbers[dig_number])
