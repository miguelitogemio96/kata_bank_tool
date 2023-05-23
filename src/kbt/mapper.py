from .digit import Digit
from .exceptions import MapperError
from .helpers import divide_by_lines
from .account import Account


class Mapper:
    def map_str_lines_to_account_numbers(data: list[list[str]], len_acc=8):
        data_in_digits = Mapper.map_lines_to_digits(data, len_acc)
        return [Account(dig_numbers) for dig_numbers in data_in_digits]

    @staticmethod
    def map_lines_to_digits(data: list[list[str]], len_acc=9, len_dig=3) -> list[list[Digit]]:
        try:
            data = divide_by_lines(data, 4)
            account_numbers = []
            for matrix_num in data:
                account_number = []
                for i in range(0, len_acc*len_dig, len_dig):
                    dig_number = matrix_num[0][i:i+3] + matrix_num[1][i:i+3] + matrix_num[2][i:i+3]
                    dig_number = dig_number if len(dig_number) == 9 else "   " + dig_number
                    account_number.append(Digit(dig_number))
                account_numbers.append(account_number)
        except Exception as e:
            raise MapperError('Error trying to map the input data into numbers')
        return account_numbers
