class ElvesDataFile:
    lines_suffix = "\n"

    def __init__(self, file: str):
        self.filename = file
        self.all_lines = None
        self.empty_indexes = None
        self.non_empty_lines = None

    def process(self):
        self.read_all_lines()
        self.remove_empty_lines()
        self.get_empty_lines_indexes()

    def read_all_lines(self) -> list[str]:
        with open(self.filename) as f:
            self.all_lines = f.readlines()
        self.__remove_suffix_from_lines(suffix=ElvesDataFile.lines_suffix)

    def __remove_suffix_from_lines(self, suffix: str = "\n") -> list[str]:
        self.all_lines = [line.replace(suffix, "") for line in self.all_lines]
        return self.all_lines

    def remove_empty_lines(self):
        self.non_empty_lines = [line for line in self.all_lines if line]
        return self.non_empty_lines

    def get_empty_lines_indexes(self) -> list[int]:
        self.empty_indexes = [index for index, line in enumerate(self.all_lines) if not line]
        return self.empty_indexes

    @staticmethod
    def convert_strlist_to_intlist(strlist: list[str]) -> list[int]:
        return [float(line) for line in strlist]

    def __str__(self):
        return f"""
        Filename = {self.filename}
        All lines = {self.all_lines}
        Non empty lines = {self.non_empty_lines}
        Empty lines indexes = {self.empty_indexes}
        """



class Elves:

    def __init__(self, elves_data: ElvesDataFile):
        self.input_data = elves_data
        self.calories_per_elf = []
        self.total_calories_per_elf = []

    @property
    def number(self):
        return len(self.input_data.empty_indexes) + 1

    @property
    def calories_list(self):
        return self.input_data.convert_strlist_to_intlist(self.input_data.non_empty_lines)

    @property
    def total_calories(self):
        return sum(self.calories_list)

    @property
    def thinnest_elf_calories(self):
        return min(self.total_calories_per_elf)

    @property
    def thinnest_elf_index(self):
        return self.total_calories_per_elf.index(self.thinnest_elf_calories)

    @property
    def fattest_elf_calories(self):
        return max(self.total_calories_per_elf)

    @property
    def fattest_elf_index(self):
        return self.total_calories_per_elf.index(self.fattest_elf_calories)

    @property
    def detected_calories(self):
        return sum(self.total_calories_per_elf)

    def inspect(self, verbose: bool = False):
        current = []
        for line in self.input_data.all_lines:
            if line:
                current.append(line)
            else:
                current = [int(val) for val in current]
                self.calories_per_elf.append(current)
                current = []

        # Append the last elf as well...
        current = [int(val) for val in current]
        self.calories_per_elf.append(current)

        for elf in self.calories_per_elf:
            self.total_calories_per_elf.append(sum(elf))


    def __str__(self):
        return f"""
        Number of elves: {self.number}
        Total calories: {self.total_calories} cals
        Thinnest elf: number {self.thinnest_elf_index} with {self.thinnest_elf_calories} cals
        Fattest elf: number {self.fattest_elf_index} with {self.fattest_elf_calories} cals
        Detected calories: {self.detected_calories} cals
        Total calories per elf: {self.total_calories_per_elf}
        """


if __name__ == "__main__":
    data = ElvesDataFile(file='elves_calories.txt')
    #data = ElvesDataFile(file='elves_calories_example.txt')
    data.process()
    print(data)

    elves = Elves(elves_data=data)
    elves.inspect(verbose=True)
    print(elves)








