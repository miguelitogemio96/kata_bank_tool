from .mapper import Mapper
from .file_accounts import FileAccounts
from .validator import Validator
from .exceptions import ProcessError


class ProcessHelper:
    @staticmethod
    def map_str_lines_to_valid_account_numbers(data: list[list[str]], lenght_account_numbers=9,
                                               *validation_funcs):
        try:
            accounts = Mapper.map_str_lines_to_account_numbers(data, lenght_account_numbers)
            Validator.apply_validations_to_Accounts(accounts, *validation_funcs)
            return str(FileAccounts(accounts))
        except Exception as e:
            raise ProcessError(f"Error during the main process, {e}")
