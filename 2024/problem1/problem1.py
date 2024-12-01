import re

# file = 'example.txt'
file = 'puzzle.txt'
regex = r'[0-9]+'


if __name__ == '__main__':

    with open(file) as f:
        lines = f.readlines()
    
    left, right = [], []
    for line in lines:
        matches = re.findall(regex, line, flags=0)
        left.append(int(matches[0]))
        right.append(int(matches[1]))

    left = sorted(left)
    right = sorted(right)

    distance = 0
    for i in range(len(left)):
        distance += abs(right[i] - left[i])
    print(distance)


    similarity = 0
    for i in range(len(left)):
        similarity += left[i] * right.count(left[i])
    print(similarity)
