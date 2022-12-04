with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()
    lines = [line.replace("-", ",").split(",") for line in lines]

fully_contained_pairs, overlapped_pairs = 0, 0
for idx, line in enumerate(lines):
    sect0 = set(range(int(line[0]), int(line[1])+1))
    sect1 = set(range(int(line[2]), int(line[3])+1))
    sub0, sup0 = sect0.issubset(sect1), sect0.issuperset(sect1)
    if any([sub0, sup0]):
        fully_contained_pairs += 1
    if not sect0.isdisjoint(sect1):
        overlapped_pairs += 1

print(f"Fully contained: {fully_contained_pairs}, overlaps: {overlapped_pairs}")