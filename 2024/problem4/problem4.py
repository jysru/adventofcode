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


def word_in_list(data: np.ndarray, word: np.ndarray, add_reverse: bool = True) -> int:
    count = 0
    if np.all(data.flatten() == word.flatten()):
        count += 1
    if add_reverse:
        if np.all(data.flatten() == np.flip(word).flatten()):
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



if __name__ == "__main__":
    data = parse_file(file)
    data = pad_array(data, word)
    print(data)
    
    directions = ["r", "d", "l", "u", "dr", "dl", "ur", "ul"]
    # directions = ["ul"]

    counter = 0
    for i_row in range(len(word) - 1, data.shape[0] - (len(word) - 1)):
        for i_col in range(len(word) - 1, data.shape[1] - (len(word) - 1)):
            for direction in directions:
                vector = get_vector(data, (i_row, i_col), word, direction)
                if i_row == 4:
                    print(i_row, i_col, vector)
                counter += word_in_list(vector,  word, add_reverse=False)
            
    print(counter)

    # print(data)
    # print(data[0][1] * 3)

