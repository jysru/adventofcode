from queue import PriorityQueue
import numpy as np


class Graph:
    start_height = 0
    stop_height = 0

    def __init__(self, file: str) -> None:
        self.file: str = file
        self.height: list[list[int]] = None
        self.start: tuple[int, int]
        self.stop: tuple[int, int]

        self.__parse()
        self.__start_stop_coords()
        self.__convert()
        

    def __parse(self) -> None:
        with open(self.file) as f:
            lines = f.read().splitlines()

        self.height = []
        for row, line in enumerate(lines):
            self.height.append([])
            for _, char in enumerate(line):
                self.height[row].append(char)


    def __start_stop_coords(self):
        for row, line in enumerate(self.height):
            for col, char in enumerate(line):
                if char == 'S':
                    self.start = (row, col)
                elif char == 'E':
                    self.stop = (row, col)


    def __convert(self) -> None:
        pass


    @property
    def size(self) -> tuple[int, int]:
        if self.height:
            return (len(self.height), len(self.height[0]))
        else:
            return None
        

    def __str__(self) -> str:
        return f"""
        Graph:
        - Size: {self.size[0]} x {self.size[1]}
        - Start coordinates: {self.start}
        - Stop coordinates: {self.stop}
        - Map: {self.height}
        """


if __name__ == "__main__":
    file = "test_input.txt"
    graph = Graph(file=file)
    print(graph)