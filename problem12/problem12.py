from queue import PriorityQueue
import numpy as np


class GraphParser:
    start_height = 0
    stop_height = 25
    ref = ord('a')

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
        for row, line in enumerate(self.height):
            for col, char in enumerate(line):
                if char == 'S':
                    self.height[row][col] = GraphParser.start_height
                elif char == 'E':
                    self.height[row][col] = GraphParser.stop_height
                else:
                    self.height[row][col] = ord(char) - GraphParser.ref


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
    

class GraphRunner:

    def __init__(self, parse: GraphParser) -> None:
        self.height: list[list[int]] = parse.height
        self.start: tuple[int, int] = parse.start
        self.stop: tuple[int, int] = parse.stop
        self.current: tuple[int, int] = parse.start
        self.visited: list[tuple[int, int, int]] = [parse.start]
        self.neighbours: list[tuple[int, int, int]] = [None, None, None, None] # Top, Left, Bottom, Right


    def find_path(self):
        self.get_neighbours()
        valid_neighbours = []
        for i, neighbour in enumerate(self.neighbours):
            if neighbour:
                if neighbour[2] in [self.current_value, self.current_value+1]:
                    valid_neighbours.append(neighbour)




    def get_neighbours(self):
        self.neighbours = [self.__get_top(), self.__get_left(), self.__get_bottom(), self.__get_right()]

    def __get_top(self) -> tuple[int, int, int]:
        if self.current[0] == 0: # We are at the top edge
            return None
        else:
            x, y = self.current[0]-1, self.current[1]
            return (x, y, self.height[x][y])
    
    def __get_bottom(self) -> tuple[int, int, int]:
        if self.current[0] == self.size[0]: # We are at the bottom edge
            return None
        else:
            x, y = self.current[0]+1, self.current[1]
            return (x, y, self.height[x][y])
        
    def __get_left(self) -> tuple[int, int, int]:
        if self.current[1] == 0: # We are at the left edge
            return None
        else:
            x, y = self.current[0], self.current[1]-1
            return (x, y, self.height[x][y])
    
    def __get_right(self) -> tuple[int, int, int]:
        if self.current[1] == self.size[1]: # We are at the right edge
            return None
        else:
            x, y = self.current[0], self.current[1]+1
            return (x, y, self.height[x][y])

    @property
    def size(self) -> tuple[int, int]:
        if self.height:
            return (len(self.height), len(self.height[0]))
        else:
            return None
        
    @property
    def current_value(self):
        return self.height[self.current[0]][self.current[1]]
        
        
    def __str__(self) -> str:
        return f"""
        Graph:
        - Size: {self.size[0]} x {self.size[1]}
        - Start coordinates: {self.start}
        - Stop coordinates: {self.stop}
        - Current coordinate: {self.current}
        - Current value: {self.current_value}
        - Neighbours coordinates: {self.neighbours}
        - Number of visits: {len(self.visited)}
        """
        



if __name__ == "__main__":
    file = "test_input.txt"
    parse = GraphParser(file=file)
    graph = GraphRunner(parse=parse)
    graph.get_neighbours()
    print(graph)