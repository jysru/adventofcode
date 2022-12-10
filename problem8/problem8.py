import numpy as np

def parse(file: str = "test_input.txt") -> list[list[int]]:
    with open(file) as f:
        lines = f.read().splitlines()

    data = []
    for line in lines:
        tmp = []
        for idx, elt in enumerate(line):
            tmp.append(int(line[idx]))
        data.append(np.array(tmp))
    return np.array(data)


def get_vector(matrix: list[list[int]], index: int, axis: int = 0) -> list[int]:
    if axis == 0:
        return matrix[index]
    elif axis == 1:
        sz = matrix.shape
        return [matrix[i][index] for i in range(0, sz[1])]
    else:
        raise ValueError


def visibility(data: list[list[int]]) -> list[list[int]]:
    from_top = np.zeros(shape=data.shape, dtype=int)
    from_bottom = np.zeros(shape=data.shape, dtype=int)
    from_left = np.zeros(shape=data.shape, dtype=int)
    from_right = np.zeros(shape=data.shape, dtype=int)
    vis = np.zeros(shape=data.shape, dtype=int)

    for idx in range(0, len(data)):
        top = get_vector(matrix=data, index=idx, axis=1)
        left = get_vector(matrix=data, index=idx, axis=0)
        from_top[:, idx] = get_visibility(top)
        from_left[idx, :] = get_visibility(left)
        from_bottom[:, idx] = get_visibility(np.flip(top))
        from_right[idx, :] = get_visibility(np.flip(left))

    from_bottom = np.flipud(from_bottom)
    from_right = np.fliplr(from_right)
    return np.logical_or(np.logical_or(from_top, from_bottom), np.logical_or(from_left, from_right))


def get_visibility(vec):
    vec = np.array(vec)
    vis = np.zeros(shape=vec.shape)
    for idx in range(0, len(vec)):
        vis[idx] = 1 if all(vec[idx] > vec[0:idx]) else 0
    return vis


def score(data: list[list[int]]) -> list[list[int]]:
    sc = np.zeros(shape=data.shape, dtype=int)
    print(f"t \t b \t l \t r")
    for r in range(0, data.shape[0]):
        for c in range(0, data.shape[1]):
            row = get_vector(matrix=data, index=r, axis=1)
            col = get_vector(matrix=data, index=c, axis=0)
            to_top = get_score(row, r, direction=-1)
            to_bottom = get_score(row, r, direction=1)
            to_left = get_score(col, c, direction=-1)
            to_right = get_score(col, c, direction=1)
            print(f"{to_top} \t {to_bottom} \t {to_left} \t {to_right}")
            sc[r, c] = to_top * to_bottom * to_left * to_right
    return sc


def get_score(vector: list[int], idx: int, direction: int = 1) -> int:
    score = 0
    if direction == 1:
        for i in range(idx-1, -1, -1):
            if vector[i] >= vector[idx]:
                score += 1

    elif direction == -1:
        for i in range(idx+1, len(vector), 1):
            if vector[i] >= vector[idx]:
                score += 1

    else:
        raise ValueError
    return score


if __name__ == "__main__":
    data = parse(file="test_input.txt")
    print("Trees")
    print(data)

    vis_map = visibility(data)
    print("Visibility map")
    print(np.sum(vis_map))

    score_map = score(data)
    print("Score map")
    print(score_map)
    print(f"Max: {np.max(score_map)}")
