import enum
import numpy as np


file = "example.txt"
file = "puzzle.txt"


class Area:
    _obstacle_token: str = '#'
    _visited_token: str = 'X'
    _edge_token: str = 'E'

    def __init__(self, file: str) -> None:
        self.file = file
        self.parse()
        self.pad()

    def parse(self) -> None:
        with open(self.file, "r") as f:
            data = f.readlines()
            data = [list(line.rstrip()) for line in data]
        self.data = np.array(data)

    def pad(self) -> None:
        self.data = np.pad(self.data, 1, constant_values=Area._edge_token)

    def show(self) -> None:
        print(self.data)

    @property
    def visited(self) -> int:
        return np.sum(self.data == Area._visited_token)
    
    @property
    def obstacles(self) -> int:
        return np.sum(self.data == Area._obstacle_token)
    


class Direction(enum.IntEnum):
    R = 0
    D = 1
    L = 2
    U = 3


class Guard:
    _tokens: list[str] = ['^', '>', 'v', '<']

    def __init__(self, area: Area) -> None:
        self.area: Area = area
        self.direction: Direction = None
        self.position: tuple[int, int] = None
        self.out_of_bounds: bool = False
        self.steps_counter: int = 0
        self.turns_counter: int = 0
        self.moves_counter: int = 0
        self.find()

    def find(self) -> None:
        if np.any(self.area.data.flatten() == '^'):
            self.direction = Direction.U
            self.position = np.where(self.area.data == '^')
            print(self.position)
        elif np.any(self.area.data.flatten() == '>'):
            self.direction = Direction.R
            self.position = np.where(self.area.data == '>')
        elif np.any(self.area.data.flatten() == 'v'):
            self.direction = Direction.D
            self.position = np.where(self.area.data == 'v')
        elif np.any(self.area.data.flatten() == '<'):
            self.direction = Direction.L
            self.position = np.where(self.area.data == '<')
        else:
            IndexError("Could not find any guard!")
        self.assign_current_position()

    def assign_current_position(self) -> None:
        content = self.area.data[self.position[0], self.position[1]]
        if content == Area._edge_token:
            self.out_of_bounds = True
        else:
            self.area.data[self.position[0], self.position[1]] = Area._visited_token

    def play(self) -> None:
        while not self.out_of_bounds:
            self.step()

    def step(self) -> None:
        while self.look_ahead() == Area._obstacle_token:
            self.turn()
            self.turns_counter += 1
        self.move()
        self.moves_counter += 1
        self.steps_counter += 1

    def look_ahead(self) -> str:
        if self.direction == Direction.R:
            ahead = self.area.data[self.position[0], self.position[1] + 1]
        elif self.direction == Direction.D:
            ahead = self.area.data[self.position[0] + 1, self.position[1]]
        elif self.direction == Direction.L:
            ahead = self.area.data[self.position[0], self.position[1] - 1]
        elif self.direction == Direction.U:
            ahead = self.area.data[self.position[0] - 1, self.position[1]]
        else:
            IndexError("Could not find any guard!")
        return ahead

    def turn(self):
        self.direction = (self.direction + 1) % 4

    def move(self,):
        if self.direction == Direction.R:
            self.position = (self.position[0], self.position[1] + 1)
        elif self.direction == Direction.D:
            self.position = (self.position[0] + 1, self.position[1])
        elif self.direction == Direction.L:
            self.position = (self.position[0], self.position[1] - 1)
        elif self.direction == Direction.U:
            self.position = (self.position[0] - 1, self.position[1])
        else:
            IndexError("Could not find any guard!")
        self.assign_current_position()

    





if __name__ == "__main__":
    area = Area(file)
    area.show()
    print(f"\t Turn {-1}: Obstacles {area.obstacles}, Visited {area.visited}\n")

    guard = Guard(area)
    area.show()
    print(f"\n")

    guard.play()
    area.show()
    print(f"\n")

    print(area.visited)
