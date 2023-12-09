import re
from enum import Enum

class Digits(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9

digits_regexp = r'[0-9]'
digits_words_regexp = r'[0-9]|one|two|three|four|five|six|seven|eight|nine'


def get_digits(string: str, include_words: bool = True) -> list[str]:
    regex = digits_words_regexp if include_words else digits_regexp
    return re.findall(regex, string, flags=0)


def words_to_digits(digits_list: list[str]) -> list[str]:
    for i, elem in enumerate(digits_list):
        if not elem.isdigit():
            enum = getattr(Digits, elem.upper())
            digits_list[i] = str(enum.value)
    return digits_list


if __name__ == "__main__":
    filename = './calibration_document.txt'

    with open(filename) as file:
        lines = file.read().splitlines()

    total = 0
    for line in lines:
        digits = get_digits(line, include_words=True)
        digits2 = words_to_digits(digits.copy())
        print(f"{digits} -> {digits2}")
        total += int(digits2[0] + digits2[-1])

    
    print(total)


