import re
from collections import deque

def prepare_file(file: str) -> (list[str], list[int]):
    with open(file) as f:
        lines = f.read().splitlines()

        split_idx = 0
        for line in lines:
            if not line:
                break
            split_idx += 1

        crates = lines[0:split_idx]
        actions = lines[split_idx + 1:]

        moves = []
        for idx, line in enumerate(actions):
            res = re.findall("[0-9]+", line)
            moves.append(list(map(int, res)))
            print(moves[idx])

        return crates, moves

def prepare_stacks(crates: list[str], verbose: bool = False):
    stacks_number = len(re.findall("[0-9]+", crates[-1]))
    stacks_idx = []
    stacks_id = []
    for i in range(1, stacks_number+1):
        match = re.search(f"{i}", crates[-1])
        stacks_id.append(int(match.group()))
        stacks_idx.append(match.start())

    stacks = []
    for i in range(0, stacks_number):
        stacks.append(deque([]))

    for idx, stack in enumerate(stacks):
        for line in range(len(crates)-2, -1, -1):
            try:
                letter = crates[line][stacks_idx[idx]]
                if letter and (letter != (' ' or '')):
                    stacks[idx].append(letter)
            except:
                pass

    if verbose:
        for idx, stack in enumerate(stacks):
            print(f"Stack #{idx}: size {len(stack)}, {stack}")
    return stacks

def apply_moves(stacks: list[deque], moves: list[int], verbose: bool = False):
    for move in moves:
        for i in range(0, move[0]):
            moved_crates = stacks[move[1]-1].pop()
            stacks[move[2]-1].append(moved_crates)
    return stacks

def show_stacks(stacks: list[deque]) -> None:
    for idx, stack in enumerate(stacks):
        print(f"Stack #{idx}, size {len(stack)}, {stack}")

def get_stacks_tops(stacks: list[deque]):
    tops = []
    for stack in stacks:
        tops.append(stack[-1])
    return tops


if __name__ == "__main__":
    crates, moves = prepare_file(file="puzzle_input.txt")
    stacks = prepare_stacks(crates, verbose=False)
    new_stacks = apply_moves(stacks=stacks, moves=moves, verbose=True)
    show_stacks(new_stacks)
    print(f"Stacks tops = {get_stacks_tops(new_stacks)}")

