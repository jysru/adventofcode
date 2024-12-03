import re

file = 'example.txt'
file = 'puzzle.txt'

extract_regex = r'mul\(\d{1,3},\d{1,3}\)'
numbers_regex = r'\b\d+\b'


if __name__ == '__main__':
    with open(file, 'r') as f:
        data = f.read()

    print(data)

    matches = re.findall(extract_regex, data, flags=0)
    print(matches)

    result = 0
    for match in matches:
        numbers = [int(s) for s in re.findall(numbers_regex, match)]
        result += numbers[0] * numbers[1]

    print(result)