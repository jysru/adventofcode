import numpy as np


file = "example.txt"
file = "puzzle.txt"
word = np.array(list("XMAS"))
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


def word_in_list(data: np.ndarray, word: np.ndarray) -> int:
    count = 0
    if np.all(data.flatten() == word.flatten()):
        count += 1
    return count


def get_vector(data: np.ndarray, coords: tuple[int, int], word: list, direction: str = "r") -> np.ndarray:
    row, col = coords

    if direction == "r":
        vector = data[row, col:(col+len(word))]
    if direction == "l":
        vector = np.flip(data[row, (col-(len(word) - 1)):(col+1)])
    if direction == "u":
        vector = np.flip(data[(row-(len(word) - 1)):(row+1), col])
    if direction == "d":
        vector = data[row:(row+len(word)), col]
    if direction == "dr":
        matrix = data[row:(row+len(word)), col:(col+len(word))]
        vector = np.diag(matrix)
    if direction == "dl":
        matrix = data[row:(row+len(word)), (col-(len(word) - 1)):(col+1)]
        vector = np.diag(np.fliplr(matrix))
    if direction == "ur":
        matrix = data[(row-(len(word) - 1)):(row+1), col:(col+len(word))]
        vector = np.diag(np.flipud(matrix))
    if direction == "ul":
        matrix = data[(row-(len(word) - 1)):(row+1), (col-(len(word) - 1)):(col+1)]
        vector = np.flip(np.diag(matrix))
    else:
        ValueError('Invalid direction')

    return vector


def check_xmas_cross(data: np.ndarray, coords: tuple[int, int]) -> int:
    row, col = coords

    center = data[row, col]
    if center != 'A':
        return 0
    else:
        top_left = data[row - 1, col - 1]
        bottom_right = data[row + 1, col + 1]
        if (top_left == 'M' and bottom_right == 'S') or (top_left == 'S' and bottom_right == 'M'):
            top_right = data[row - 1, col + 1]
            bottom_left = data[row + 1, col - 1]
            if (top_right == 'M' and bottom_left == 'S') or (top_right == 'S' and bottom_left == 'M'):
                return 1
            else:
                return 0
        else:
            return 0



if __name__ == "__main__":
    data = parse_file(file)
    data = pad_array(data, word)
    print(data)
    
    directions = ["r", "d", "l", "u", "dr", "dl", "ur", "ul"]

    xmas_counter = 0
    xmas_cross_counter = 0
    for i_row in range(len(word) - 1, data.shape[0] - (len(word) - 1)):
        for i_col in range(len(word) - 1, data.shape[1] - (len(word) - 1)):
            xmas_cross_counter += check_xmas_cross(data, (i_row, i_col))

            for direction in directions:
                vector = get_vector(data, (i_row, i_col), word, direction)
                xmas_counter += word_in_list(vector, word, add_reverse=False)
            
    print(xmas_counter)
    print(xmas_cross_counter)
