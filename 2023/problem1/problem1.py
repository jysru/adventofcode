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

    solution_1, solution_2 = 0, 0
    for line in lines:
        digits1 = get_digits(line, include_words=False)
        solution_1 += int(digits1[0] + digits1[-1])

        digits2 = get_digits(line, include_words=True)
        digits2_words = words_to_digits(digits2.copy())
        print(f"{digits2} -> {digits2_words}")
        solution_2 += int(digits2_words[0] + digits2_words[-1])

    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")


