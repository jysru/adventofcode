from collections import deque

class Parser:

    def __init__(self, file: str = "test_input.txt"):
        self.file = file
        self.values = []

    def read(self):
        with open(self.file) as f:
            lines = f.read().splitlines()

        for line in lines:
            if line[0:4] == "noop":
                self.values.append(0)
            elif line[0:4] == "addx":
                self.values.append(int(line[5:]))
class Register:

    def __init__(self):
        self.X = [1]

    def process(self, commands: Parser):
        for val in commands.values:
            if val == 0:
                self.X.append(self.X[-1])
            else:
                self.X.append(self.X[-1])
                #self.X.append(self.X[-1])
                self.X.append(self.X[-1] + val)


if __name__ == "__main__":
    cmds = Parser(file="puzzle_input.txt")
    cmds.read()
    print(cmds.values)

    cpu = Register()
    cpu.process(commands=cmds)
    print(cpu.X)
    print(f"Cycles values: {[i-1 for i in range(21, 222, 40)]}")
    print(f"Register values: {[cpu.X[i-1] for i in range(20, 221, 40)]}")
    print(f"Signal strengths: {[cpu.X[i-1]*i for i in range(20, 221, 40)]}")
    print(f"Sum of signal strengths: {sum([cpu.X[i-1]*i for i in range(20, 221, 40)])}")