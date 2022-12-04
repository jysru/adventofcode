if __name__ == "__main__":
    filename = "test_input.txt"
    filename = "puzzle_input.txt"

    # File processing
    with open(filename) as f:
        lines = f.read().splitlines()
        lines = [line.replace("-", ",").split(",") for line in lines]

    # Sets processing
    fully_contained_pairs = 0
    for idx, line in enumerate(lines):
        sect0 = set(range(int(line[0]), int(line[1])+1))
        sect1 = set(range(int(line[2]), int(line[3])+1))
        sub0, sup0 = sect0.issubset(sect1), sect0.issuperset(sect1)
        if any([sub0, sup0]):
            fully_contained_pairs += 1

    print(fully_contained_pairs)

