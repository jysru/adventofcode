import numpy as np

def parse(file: str = "test_input.txt") -> list[list[int]]:
    with open(file) as f:
        lines = f.read().splitlines()

    dirs, nums = [], []
    for line in lines:
        dirs.append(line[0])
        nums.append(int(line[2:]))
    return dirs, nums



if __name__ == "__main__":
    dirs, nums = parse(file="test_input.txt")
    print(dirs, nums)

