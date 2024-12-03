import re

file = 'example2.txt'
file = 'puzzle.txt'

extract_regex = r'mul\(\d{1,3},\d{1,3}\)'
numbers_regex = r'\b\d+\b'


if __name__ == '__main__':
    with open(file, 'r') as f:
        data = f.read()

    dos = [(m.start(), m.end(), 'do') for m in re.finditer(r"do\(\)", data)]
    donts = [(m.start(), m.end(), 'dont') for m in re.finditer(r"don't\(\)", data)]
    statuses = sorted(dos + donts, key=lambda x: x[0])
    print(statuses)

    enabled_data = ""
    _idx = 0
    _enabled = True

    for status in statuses:
        if _enabled:
            enabled_data += data[_idx:status[0]]
        _enabled = True if status[-1] == 'do' else False
        _idx = status[1]

    # Add final string part if enabled
    if _enabled:
        enabled_data += data[_idx:-1]

    # matches = re.findall(extract_regex, data, flags=0)
    matches = re.findall(extract_regex, enabled_data, flags=0)

    result = 0
    for match in matches:
        numbers = [int(s) for s in re.findall(numbers_regex, match)]
        result += numbers[0] * numbers[1]

    print(result)