import re
from math import floor


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

    @staticmethod
    def _parse_test_divider(line: str) -> int:
        res = re.findall("[0-9]+", line)
        res = list(map(int, res))
        return res[0]

    @staticmethod
    def _parse_test_monkey_id(line: str) -> int:
        res = re.findall("[0-9]+", line)
        res = list(map(int, res))
        return res[0]

    def _callable_monkey_test(self, test: tuple[int, int, int]):
        call = lambda a: a

    def show(self):
        print("Parsing results:")
        for monkey in self.parsed:
            print(f"\tMonkey {monkey[0]}, start items {monkey[1]}, operation {monkey[2]}, test {monkey[3]}")


class Monkey:
    def __init__(self, id: int, items: list[int], operation: callable, test: callable) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test_tuple = test
        self.worry = None
        self.activity = 0

    def play_round(self, others, debug: bool = False):
        print(f"Monkey {self.id}'s round:")
        while (self.items):
            self.__inspect(debug=debug)
            self.__throw(others=others, debug=debug)

    def __inspect(self, debug: bool = False) -> int:
        if self.items:
            self.worry = self.items[0]
            self.activity += 1
            if debug: print(f"  Monkey inspects item with worry level {self.items[0]}")
            self.worry = self.operation(self.worry)
            if debug: print(f"    Worry level becomes {self.operation(self.items[0])}")
            self.worry = floor(self.worry/3)
            if debug: print(f"    Monkey gets bored with item. Worry level is divided by 3 to {self.worry}.")

    def __throw(self, others, debug: bool = False) -> None:
        other_id = self.__test(debug=debug)
        others[other_id].items.append(self.worry)
        self.items.pop(0)
        if debug: print(f"    Item with worry level {self.worry} is thrown to monkey {other_id}")
        self.worry = None

    def __test(self, debug: bool = False) -> int:
        if (self.worry % self.test_tuple[0] == 0):
            if debug: print(f"    Current worry level is divisible by {self.test_tuple[0]}")
            return self.test_tuple[1]    
        else:
            if debug: print(f"    Current worry level is not divisible by {self.test_tuple[0]}")
            return self.test_tuple[2]
            

    def __str__(self) -> str:
        return f"""
        Monkey {self.id}
        - Items: {self.items}
        - Operation: {self.operation}
        - Test: {self.test_tuple}
        - Activity: {self.activity}
        """


class MonkeyGroup:

    def __init__(self, monkeys: list[Monkey]) -> None:
        self.monkeys = monkeys

    def do_rounds(self, rounds: int = 20, debug: bool = False) -> None:
        for round in range(1, rounds+1):
            for monkey in self.monkeys:
                monkey.play_round(others=self.monkeys, debug=True)
            print(f"After round {round}:")
            self.check_items()

    def check_items(self) -> None:
        for monkey in self.monkeys:
            print(f"  Monkey {monkey.id}: {monkey.items}")

    @property
    def business_level(self):
        activities = sorted(self.get_activity(), reverse=True)
        return activities[0]*activities[1]

    def get_activity(self) -> list:
        return [monkey.activity for monkey in self.monkeys]

    def show_activity(self) -> None:
        for monkey in self.monkeys:
            print(f"Monkey {monkey.id} inspected items {monkey.activity} times")


if __name__ == "__main__":
    parse = ParseMonkeys(file="puzzle_input.txt")

    monkeys = []
    for monkey in parse.parsed:
        id, items, operation, test_tuple = monkey
        m = Monkey(id=id, items=items, operation=operation, test=test_tuple)
        monkeys.append(m)

    monkey_group = MonkeyGroup(monkeys=monkeys)
    monkey_group.do_rounds(rounds=20, debug=False)
    monkey_group.show_activity()
    print(monkey_group.get_activity())
    print(monkey_group.business_level)




