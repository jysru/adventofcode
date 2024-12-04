import re
import numpy as np


file = "example.txt"
# file = "puzzle.txt"
word = list("XMAS")
pad_char = "."


def parse_file(file: str) -> np.ndarray:
    with open(file, "r") as f:
        data = f.readlines()
        data = [list(line.rstrip()) for line in data]
    return np.array(data)


def pad_array(data: np.ndarray, word: list) -> np.ndarray:
    pad_length = len(word) - 1
    if pad_length > 0:
        data = np.pad(data, pad_length, constant_values=pad_char)
    return data


def word_in_list(data: list, word: list, add_reverse: bool = True) -> int:
    count = 0
    if data == word:
        count += 1
    if add_reverse:
        if data == word.reverse():
            count += 1
    return count


def get_vector(data: list[list], coords: tuple[int, int], word: list, direction: str = 'r'):
    row, col = coords
    len_word = len(word)

    if direction == 0: # Starting from coordinate (included), direction is 0° (horizontal, towards the east)
        sublist = [data[row][col + i] for i in range(len_word)]
    if direction == 1: # Starting from coordinate (included), direction is 45° (vertical, towards the north-east)
        sublist = [data[row - i][col + i] for i in range(len_word)].reverse()
    if direction == 2: # Starting from coordinate (included), direction is 90° (vertical, towards north)
        sublist = [data[row - i][col] for i in range(len_word)].reverse()
    if direction == 3: # Starting from coordinate (included), direction is 135° (diagonal, towards north-west)
        sublist = [data[row - i][col - i] for i in range(len_word)].reverse()
    if direction == 4: # Starting from coordinate (included), direction is 180° (horizontal, towards the west)
        sublist = [data[row][col - i] for i in range(len_word)].reverse()
    if direction == 5: # Starting from coordinate (included), direction is -135° (vertical, towards the north-east)
        sublist = [data[row + i][col - i] for i in range(len_word)]
    if direction == 6: # Starting from coordinate (included), direction is -90° (vertical, towards the south)
        sublist = [data[row + i][col] for i in range(len_word)]
    if direction == 7: # Starting from coordinate (included), direction is -45° (vertical, towards the south-east)
        sublist = [data[row + i][col + i] for i in range(len_word)]
    else:
        ValueError('Invalid direction')

    return sublist



if __name__ == "__main__":
    data = parse_file(file)
    data = pad_array(data, word)
    print(data)
    
    directions = [0, 5, 6, 7]

    counter = 0
    for i_row in range(len(word) - 1, len(data) - (len(word) - 1)):
        for i_col in range(len(word) - 1, len(data[0]) - (len(word) - 1)):
            # for direction in range(8):
            for direction in directions:
                sublist = get_vector(data, (i_row, i_col), word, direction)
                counter += word_in_list(sublist,  word, add_reverse=True)
            
    print(counter)

    # print(data)
    # print(data[0][1] * 3)

