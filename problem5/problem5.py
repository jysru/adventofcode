import re
from queue import LifoQueue

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

    stacks = list(map(LifoQueue, range(0, stacks_number)))
    for idx, stack in enumerate(stacks):
        for i in range(0, len(crates)-1):

            if stacks_idx[idx] > len(crates[i]):
                continue
            else:
                print(idx, crates[i][stacks_idx[idx]])
                stacks[idx].put(crates[i][stacks_idx[idx]])

    print(stacks[0].qsize())
    for i in range(0, stacks[0].qsize()-1):
        print(stacks[0].get())



crates, moves = prepare_file(file="test_input.txt")
prepare_stacks(crates)



