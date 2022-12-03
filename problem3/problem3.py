import itertools


def char2priority(char: str) -> int:
    if ord(char[0]) >= ord('a'):  # 97
        return ord(char[0]) - ord('a') + 1
    else:
        return ord(char[0]) - ord('A') + 27


def get_prios1(lines: list[str]) -> list[int]:
    lens = list(map(len, lines))

    commons = []
    for idx, line in enumerate(lines):
        str1 = line[:lens[idx] // 2]
        str2 = line[lens[idx] // 2:]
        commons.append(set(str1).intersection(str2))
    commons = list(itertools.chain(*commons))
    return list(map(char2priority, commons))


def get_prios2(lines: list[str]) -> list[int]:
    lens = list(map(len, lines))

    commons = []
    k = 0
    for i in range(0, len(lines) // 3):
        group = [lines[k + 0], lines[k + 1], lines[k + 2]]
        k += 3
        commons.append(set(group[0]).intersection(group[1]).intersection((group[2])))
    commons = list(itertools.chain(*commons))
    return list(map(char2priority, commons))


if __name__ == "__main__":
    # filename = "test_input.txt"
    filename = "puzzle_input.txt"

    with open(filename) as f:
        lines = f.read().splitlines()

    print(sum(get_prios1(lines)))
    print(sum(get_prios2(lines)))
