import re

file = "example.txt"
file = "puzzle.txt"

rules_regex = r'(\d+)\|(\d+)'


def parse_file(file: str) -> list[str]:
    with open(file, "r") as f:
        data = f.readlines()
        data = [line.rstrip() for line in data]
    return data

def get_rules(data: list[str]) -> list[tuple[int, int]]:
    rules = []
    for line in data:
        matches = re.findall(rules_regex, line)
        if len(matches) > 0:
            rules.append(tuple([int(elem) for elem in matches[0]]))
    return rules

def get_pages(data: list[str]) -> list[tuple[int]]:
    pages = []
    for line in data:
        if ',' in line:
            pages.append(tuple([int(elem) for elem in line.split(sep=',')]))
    return pages

if __name__ == "__main__":
    data = parse_file(file)
    rules = get_rules(data)
    pages = get_pages(data)

    print(rules)
    print(pages)


    valid_pages = []
    for page in pages:       
        _rules_check = []
        for rule in rules:
            if rule[0] in page and rule[1] in page:
                if page.index(rule[0]) > page.index(rule[1]):
                    _rules_check.append(False)
                else:
                    _rules_check.append(True)
            else:
                _rules_check.append(True)
        valid_pages.append(True if all(_rules_check) else False)

    print(valid_pages)


    middle_pages_sum = 0
    for i, page in enumerate(pages):
        if valid_pages[i]:
            middle_pages_sum += page[len(page)//2]

    print(middle_pages_sum)
    

    incorrect_pages = [list(page) for i, page in enumerate(pages) if not valid_pages[i]]
    print(incorrect_pages)

    corrected_pages = []
    for wrong_page in incorrect_pages:
        for k in range(50):
            for rule in rules:
                if rule[0] in wrong_page and rule[1] in wrong_page:
                    if wrong_page.index(rule[0]) > wrong_page.index(rule[1]):
                        wrong_page[wrong_page.index(rule[0])] = rule[1]
                        wrong_page[wrong_page.index(rule[1])] = rule[0]
        corrected_pages.append(wrong_page)
    print(corrected_pages)


    corr_middle_pages_sum = 0
    for i, page in enumerate(corrected_pages):
            corr_middle_pages_sum += page[len(page)//2]

    print(corr_middle_pages_sum)
    # print(rules_numbers)



    