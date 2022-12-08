class Matrix:

    def __init__(self, file: str = '', data: list[list[int]] = [], shape: tuple[int,int] = ()):
        self.data = None
        if data:
            if shape:
                self.data = self.generate(value=data, shape=shape)
            else:
                self.data = data
        else:
            self.data = self.parse(file)

    @staticmethod
    def parse(file: str = "test_input.txt") -> list[list[int]]:
        with open(file) as f:
            lines = f.read().splitlines()

        data = []
        for line in lines:
            tmp = []
            for idx, elt in enumerate(line):
                tmp.append(int(line[idx]))
            data.append(tmp)
        return data

    @staticmethod
    def generate(value: int, shape: tuple[int, int]) -> list[list[int]]:
        data = []
        for idx_row in range(0, shape[0]):
            tmp = []
            for idx_colin in range(0, shape[1]):
                tmp.append(value)
            data.append(tmp)
        return data

    def visibility(self):
        from_top = self._visibility_from_top()
        from_left = self._visibility_from_left()
        from_bottom = self._visibility_from_bottom()
        from_right = self._visibility_from_right()
        vis = self._visibility_compare([from_top, from_left, from_bottom, from_right])
        return Matrix(data=vis)

    def _visibility_from_top(self) -> list[list[int]]:
        vis = self.generate(value=0, shape=self.shape)
        for col in range(0, self.shape[1]):
            for row in range(0, self.shape[0]):
                if row == 0:
                    vis[row][col] = 1
                else:
                    if self.data[row][col] <= self.data[row-1][col]:
                        break
                    else:
                        vis[row][col] = 1
        return vis

    def _visibility_from_bottom(self) -> list[list[int]]:
        vis = self.generate(value=0, shape=self.shape)
        for col in range(self.shape[1]-1, -1, -1):
            for row in range(self.shape[0]-1, -1, -1):
                if row == self.shape[0]-1:
                    vis[row][col] = 1
                else:
                    if self.data[row][col] <= self.data[row-1][col]:
                        break
                    else:
                        vis[row][col] = 1
        return vis

    def _visibility_from_left(self) -> list[list[int]]:
        vis = self.generate(value=0, shape=self.shape)
        for row in range(0, self.shape[0]):
            for col in range(0, self.shape[1]):
                if col == 0:
                    vis[row][col] = 1
                else:
                    if self.data[row][col] <= self.data[row][col-1]:
                        break
                    else:
                        vis[row][col] = 1
        return vis

    def _visibility_from_right(self) -> list[list[int]]:
        vis = self.generate(value=0, shape=self.shape)
        for row in range(self.shape[0]-1, -1, -1):
            for col in range(self.shape[1]-1, -1, -1):
                if col == self.shape[1]-1:
                    vis[row][col] = 1
                else:
                    if self.data[row][col] <= self.data[row-1][col]:
                        break
                    else:
                        vis[row][col] = 1
        return vis

    def _visibility_compare(self, maps: list[list[list[int]]]) -> list[list[int]]:
        vis = maps[0]
        for page in range(1, len(maps)):
            for row in range(0, self.shape[0]):
                for col in range(0, self.shape[1]):
                    vis[row][col] = int(bool(vis[row][col]) or bool(maps[page][row][col]))
        return vis


    @property
    def shape(self) -> tuple[int, int]:
        if self.data:
            return len(self.data), len(self.data[0])
        else:
            return None

    @property
    def flattened(self) -> list[int]:
        if self.data:
            return [item for sublist in self.data for item in sublist]
        else:
            return None

    @property
    def numel(self) -> int:
        if self.shape:
            prod = 1
            for val in self.shape:
                prod *= val
            return prod
        else:
            return None

    def show(self):
        for line in self.data:
            tmp = []
            for idx, elt in enumerate(line):
                tmp.append(int(line[idx]))
            print(tmp)



if __name__ == "__main__":
    mat = Matrix(file="puzzle_input.txt")
    print(f"Forest:\n{mat.show()}")

    vis_map = mat.visibility()
    print(f"Visibility map:\n{vis_map.show()}")
    print(f"Number of visible trees: {sum(vis_map.flattened)}")

