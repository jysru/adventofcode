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

def prepare_stacks(crates: list[str]):
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
                    print(f"Put {letter} in LIFO stack #{idx}")
            except:
                pass

    for idx, stack in enumerate(stacks):
        print(f"Stack #{idx}: size {len(stack)}")
        print(f"{stack}")



crates, moves = prepare_file(file="test_input.txt")
prepare_stacks(crates)



