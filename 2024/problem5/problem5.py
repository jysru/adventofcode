import re

file = "example.txt"
# file = "puzzle.txt"

rules_regex = r'(\d+)\|(\d+)'


def parse_file(file: str) -> list[str]:
    with open(file, "r") as f:
        data = f.readlines()
        data = [line.rstrip() for line in data]
    return data

if __name__ == "__main__":
    data = parse_file(file)
    print(data)

    rules = []
    for line in data:
        matches = re.findall(rules_regex, line)
        if len(matches) > 0:
            rules.append(matches[0])

    print(rules)
    # print(rules_numbers)



    