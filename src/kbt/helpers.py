def divide_by_lines(data: list[str], lines: int) -> list:
    try:
        divided_data = [data[i:i+lines-1] for i in range(0, len(data), lines)]
        return divided_data
    except Exception as e:
        raise Exception(f'Error trying to divide the data in {lines}, {e}')


numbers = {
    " _ | ||_|": 0,
    "     |  |": 1,
    " _  _||_ ": 2,
    " _  _| _|": 3,
    "   |_|  |": 4,
    " _ |_  _|": 5,
    " _ |_ |_|": 6,
    " _   |  |": 7,
    " _ |_||_|": 8,
    " _ |_| _|": 9,
    "  |  |": 1,
    "|_|  |": 4,
}

posible_numbers = {
    "0": ["8"],
    "1": ["7"],
    "2": [],
    "3": ["9"],
    "4": [],
    "5": ["9", "6"],
    "6": ["5", "8"],
    "7": ["1"],
    "8": ["0", "9", "6"],
    "9": ["8", "5", "3"]
}

type_character_dig_number = {
    0: " ",
    1: "_",
    2: " ",
    3: "|",
    4: "_",
    5: "|",
    6: "|",
    7: "_",
    8: "|",
}
