import re


class ParseMonkeys:

    def __init__(self, file: str = "test_input.txt"):
        with open(file) as f:
            lines = f.read().splitlines()
            lines = [line for line in lines if line]

        self.parsed = []
        for i in range(0, int(len(lines) / 6)):
            self.parsed.append(self.parse(lines[i * 6:i * 6 + 6]))

    def parse(self, lines: list[str]) -> tuple[int, list[int], callable, int, int, int]:
        if len(lines) != 6:
            raise ValueError

        id = self.parse_id(lines[0])
        items = self.parse_items(lines[1])
        op = self.parse_operation(lines[2])
        test = self.parse_test(lines[3:])
        return id, items, op, test

    def parse_id(self, line: str) -> int:
        res = re.findall("[0-9]+", line)
        res = list(map(int, res))
        return res[0]

    def parse_items(self, line: str) -> list[int]:
        res = re.findall("[0-9]+", line)
        res = list(map(int, res))
        return res

    def parse_operation(self, line: str) -> list[str]:
        op = line.split("new = old ")
        op, val = op[-1].split(" ")
        if op[0] == "+":
            if val == "old":
                operation = lambda a: a + a
            else:
                operation = lambda a: a + int(val)
        elif op[0] == "*":
            if val == "old":
                operation = lambda a: a * a
            else:
                operation = lambda a: a * int(val)
        else:
            raise NotImplementedError

        return operation

    def parse_test(self, lines: list[str]) -> tuple[int, int, int]:
        if len(lines) != 3:
            raise ValueError
        div = self._parse_test_divider(lines[0])
        monkey_id_true = self._parse_test_monkey_id(lines[1])
        monkey_id_false = self._parse_test_monkey_id(lines[2])
        return div, monkey_id_true, monkey_id_false

    def _parse_test_divider(self, line: str) -> int:
        res = re.findall("[0-9]+", line)
        res = list(map(int, res))
        return res[0]

    def _parse_test_monkey_id(self, line: str) -> int:
        res = re.findall("[0-9]+", line)
        res = list(map(int, res))
        return res[0]

    def show(self):
        print("Parsing results:")
        for monkey in self.parsed:
            print(f"\tMonkey {monkey[0]}, start items {monkey[1]}, operation {monkey[2]}, test {monkey[3]}")


class Monkey:
    def __init__(self):
        self.id: int
        self.items: list[int]
        self.operation: callable(int)
        self.test: callable(int)
        self.divisor: int
        self.insp: int


if __name__ == "__main__":
    p = ParseMonkeys(file="test_input.txt")
    p.show()
    m = Monkey()

