import numpy as np


def parse(file: str = "test_input1.txt") -> list[list[int]]:
    with open(file) as f:
        lines = f.read().splitlines()

    dirs, nums = [], []
    for line in lines:
        dirs.append(line[0])
        nums.append(int(line[2:]))
    return dirs, nums


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


class Rope:

    def __init__(self, knots: int = 2, start: tuple[int, int] = (0, 0)):
        self.knots_number = knots
        self.start = start
        self.knots = [Position(x=start[0], y=start[1]) for i in range(0, self.knots_number)]
        self.knots_positions = [[Position(x=start[0], y=start[1])] for i in range(0, self.knots_number)]
        self.knots_min_positions = []
        self.knots_max_positions = []
        self.unique_positions = []

    def update_head(self, dir: str):
        sign = 1 if dir in {"R", "U"} else -1
        if dir in {"R", "L"}:
            self.knots[0].x += sign
        else:
            self.knots[0].y += sign
        self.knots_positions[0].append((self.knots[0].x, self.knots[0].y))

    def update_tails(self):
        for idx in range(1, self.knots_number):
            self.update_tail(ref_index=idx)
            self.knots_positions[idx].append((self.knots[idx].x, self.knots[idx].y))

    def update_tail(self, ref_index: int):
        dx, dy = self.knots[ref_index - 1] - self.knots[ref_index]
        if np.abs(dx) > 1:
            if np.abs(dy) > 0:
                self.knots[ref_index].y += np.sign(dy)
            self.knots[ref_index].x += np.sign(dx) * (np.abs(dx) - 1)
        if np.abs(dy) > 1:
            if np.abs(dx) > 0:
                self.knots[ref_index].x += np.sign(dx)
            self.knots[ref_index].y += np.sign(dy) * (np.abs(dy) - 1)

    def apply_moves(self, moves: tuple[list[str], list[int]]):
        dirs, nums = moves
        self.knots_positions = [[(knot.x, knot.y)] for i, knot in enumerate(self.knots)]

        for i in range(0, len(dirs)):
            for j in range(0, nums[i]):
                self.update_head(dir=dirs[i])
                self.update_tails()
        return self.knots_positions

    def count_positions(self):
        len_x = []
        len_y = []
        for knots_positions in self.knots_positions:
            min_x = np.min([pos[0] for pos in knots_positions])
            max_x = np.max([pos[0] for pos in knots_positions])
            min_y = np.min([pos[1] for pos in knots_positions])
            max_y = np.max([pos[1] for pos in knots_positions])
            self.knots_min_positions.append((min_x, max_x))
            self.knots_max_positions.append((min_y, max_y))
            len_x.append(max_x + 1 if min_x > 0 else max_x + np.abs(min_x) + 1)
            len_y.append(max_y + 1 if min_y > 0 else max_y + np.abs(min_y) + 1)

        for k in range(0, self.knots_number):
            counts = np.zeros(shape=(np.max(len_x), np.max(len_y)), dtype=int)
            for x, y in self.knots_positions[k]:
                counts[x + np.abs(min_x), y + np.abs(min_y)] += 1
            counts[np.where(counts >= 1)] = 1
            self.unique_positions.append(counts)
        return self.unique_positions


if __name__ == "__main__":
    moves = parse(file="test_input2.txt")
    knots = 10
    rope = Rope(knots=knots)
    pos = rope.apply_moves(moves)
    rope.count_positions()

    for i in range(0, knots):
        print(f"Counts for knot #{i}: {np.count_nonzero(rope.unique_positions[i])}")
        print(rope.unique_positions[i])
