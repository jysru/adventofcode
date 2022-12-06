from collections import deque


def is_redundant(array: list[int]) -> bool:
    if len(array) == len(set(array)):
        return True
    else:
        return False


def find_redundancies_within_queue(arrays: list[str], queue_size: int) -> list[int]:
    starts = []
    for arr in arrays:
        reader = deque([])
        for idx, char in enumerate(arr):
            reader.append(char)
            if len(reader) > queue_size:
                reader.popleft()
                if is_redundant(reader):
                    starts.append(idx + 1)
                    break
    return starts


with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()
    print(f"Packet(s) start(s): {find_redundancies_within_queue(arrays=lines, queue_size=4)}")
    print(f"Message(s) start(s): {find_redundancies_within_queue(arrays=lines, queue_size=14)}")
