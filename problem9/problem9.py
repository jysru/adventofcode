import numpy as np

class Position:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"


def parse(file: str = "test_input.txt") -> list[list[int]]:
    with open(file) as f:
        lines = f.read().splitlines()

    dirs, nums = [], []
    for line in lines:
        dirs.append(line[0])
        nums.append(int(line[2:]))
    return dirs, nums

def apply_moves(moves: tuple[list[str], list[int]]):
    dirs, nums = moves
    start = Position(x=0, y=0)
    head = Position(x=0, y=0)
    tail = Position(x=0, y=0)

    tails = [(tail.x, tail.y)]
    for i in range(0, len(dirs)):
        for j in range(0, nums[i]):
            update_head(head, dirs[i])
            update_tail(head, tail)
            tails.append((tail.x, tail.y))
    return tails

def count_positions(tails):
    min_x = np.min([tail[0] for tail in tails])
    max_x = np.max([tail[0] for tail in tails])
    min_y = np.min([tail[1] for tail in tails])
    max_y = np.max([tail[1] for tail in tails])

    counts = np.zeros(shape=(max_x+1, max_y+1), dtype=int)
    for x, y in tails:
        counts[x, y] += 1

    return counts
def update_head(head, dir):
    sign = 1 if dir in {"R", "U"} else -1
    if dir in {"R", "L"}:
        head.x += sign
    else:
        head.y += sign

def update_tail(head, tail):
    dx, dy = head - tail
    if np.abs(dx) > 1:
        if np.abs(dy) > 0:
           tail.y += np.sign(dy)
        tail.x += np.sign(dx) * (np.abs(dx) - 1)
    if np.abs(dy) > 1:
        if np.abs(dx) > 0:
            tail.x += np.sign(dx)
        tail.y += np.sign(dy) * (np.abs(dy) - 1)


if __name__ == "__main__":
    moves = parse(file="test_input.txt")
    tails = apply_moves(moves)
    print(tails)
    pos = count_positions(tails)
    print(pos)
    print(f"Num pos = {np.count_nonzero(pos)}")


