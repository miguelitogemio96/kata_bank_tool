from .account import Account


class FileAccounts:
    def __init__(self, accounts: list[Account] = []) -> None:
        self.__accounts = accounts

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, new_digit):
        self.__accounts = new_digit

    def __str__(self) -> str:
        return "\n".join([str(acc) for acc in self.__accounts])
