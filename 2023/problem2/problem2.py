import re


if __name__ == "__main__":
    filename = './example.txt'

    with open(filename) as file:
        lines = file.read().splitlines()

    for line in lines:
        id, draws = line.split(':')
        id = re.search(r'\d+', id)[0]
        print(id)

        subsets = re.findall(r'[\s*(\w+)\s*(\d+)]+', draws)
        # subsets = re.findall(r'[[\s*\w+\s*\d+]+;]+', draws)
        print(draws)
        print(subsets)



