# KATA BANK TOOL
It's a tool that allows you map lines of text of digital numbers format into account numbers, Also you can apply some validations(functions) to each account number. The output will be a entire text where in each line will be the account number in int format followed by the its state.

### State of an Account Number
- ERR if it is readable but it does't pass the validations.
- ILL if it is now readable.
- AMB is there is more that one posible account number that pass the validations(the tool tries to fix the account number if the result is ILL or ERR and show posibles valid account numbers).
- OK when the account number is readable and pass all the validations.

## How to setup
Before download the package, you need to be sure your pip is updated.
```bash
# Windows
py -m pip install --upgrade pip

# Linux/MAC OS
python3 -m pip install --upgrade pip
```

Then, you can install the package(could be inside a venv).
```bash
pip install -i https://test.pypi.org/simple/ kbt
```

## Examples of How To Use (Buggy Alpha Version)
Import the class and use the main method:
```python
from kata_bank_tool.processs_helper import ProcessHelper

output = ProcessHelper.map_str_lines_to_valid_account_numbers(data, lenght_account_numbers, *validations_functions)
```
Where we have the parameters:
- data(list[str]): The input list of strings that represents each line of text of the main file of account numbers.
- lenght_account_numbers(int): The size of the account numbers(8, 9....)
- *validations(function): Append any validations function(lambda function) that you want the tool applies to each account number.

### Note
The input has to be a list(array) of string, where each item represent a line of text of the entire file of accounts numbers:
```python
input_example = [
    " _  _  _  _  _  _  _  _  _ ",
    "| || || || || || || || || |",
    "|_||_||_||_||_||_||_||_||_|",
    "",
    "                           ",
    "  |  |  |  |  |  |  |  |  |",
    "  |  |  |  |  |  |  |  |  |",
    "",
    " _  _  _  _  _  _  _  _  _ ",
    " _| _| _| _| _| _| _| _| _|",
    "|_ |_ |_ |_ |_ |_ |_ |_ |_ ",
    "",
]
```

## Example of Use
in main.py file
```python
from kata_bank_tool.process_helper import ProcessHelper


input_example = [
    " _  _  _  _  _  _  _  _  _ ",
    "| || || || || || || || || |",
    "|_||_||_||_||_||_||_||_||_|",
    "",
    "                           ",
    "  |  |  |  |  |  |  |  |  |",
    "  |  |  |  |  |  |  |  |  |",
    "",
    " _  _  _  _  _  _  _  _  _ ",
    " _| _| _| _| _| _| _| _| _|",
    "|_ |_ |_ |_ |_ |_ |_ |_ |_ ",
    "",
]


def checksum(account_number: str, mod=11) -> bool:
    length = len(account_number)
    total_sum = sum([(int(account_number[i]) * (length - i)) for i in range(length)])
    return total_sum % mod == 0


def main():
    text = ProcessHelper.map_str_lines_to_valid_account_numbers(input_example, 9, checksum)
    print(text)


if __name__ == "__main__":
    main()

```
```bash
$python main.py

# Output:
000000000 OK
711111111 OK
222222222 ERR
```