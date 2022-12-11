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


def parse(file: str = "test_input1.txt") -> list[list[int]]:
    with open(file) as f:
        lines = f.read().splitlines()

    dirs, nums = [], []
    for line in lines:
        dirs.append(line[0])
        nums.append(int(line[2:]))
    return dirs, nums

def apply_moves(moves: tuple[list[str], list[int]]):
    dirs, nums = moves
    head = Position(x=0, y=0)
    tails = [Position(x=0, y=0) for i in range(0, 9)]
    tails_xy = [[(t.x, t.y)] for i, t in enumerate(tails)]

    for i in range(0, len(dirs)):
        for j in range(0, nums[i]):
            update_head(head, dirs[i])
            for k, t in enumerate(tails):
                if k == 0:
                    update_tail(head, t)
                else:
                    update_tail(tails[k-1], t)
                tails_xy[k].append((tails[k].x, tails[k].y))
    return tails_xy

def count_positions(tails):
    min_x = np.min([tail[0] for tail in tails])
    max_x = np.max([tail[0] for tail in tails])
    min_y = np.min([tail[1] for tail in tails])
    max_y = np.max([tail[1] for tail in tails])

    len_x = max_x + 1 if min_x > 0 else max_x + np.abs(min_x) + 1
    len_y = max_y + 1 if min_y > 0 else max_y + np.abs(min_y) + 1
    counts = np.zeros(shape=(len_x, len_y), dtype=int)
    for x, y in tails:
        counts[x + np.abs(min_x), y + np.abs(min_y)] += 1
    counts[np.where(counts >= 1)] = 1
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
    moves = parse(file="test_input2.txt")
    tails = apply_moves(moves)
    print(tails)
    pos = count_positions(tails[-1])
    print(pos)
    print(f"Num pos = {np.count_nonzero(pos)}")


