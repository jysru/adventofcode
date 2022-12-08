import numpy as np

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
            current_list = [self.data[i][col] for i in range(0, self.shape[1])]
            for row in range(0, self.shape[0]):
                if row == 0:
                    vis[row][col] = 1
                else:
                    if self.data[row][col] > max(current_list[0:row]):
                        vis[row][col] = 1
        return vis

    def _visibility_from_bottom(self) -> list[list[int]]:
        vis = self.generate(value=0, shape=self.shape)
        for col in range(self.shape[1]-1, -1, -1):
            current_list = [self.data[i][col] for i in range(0, self.shape[1])]
            for row in range(self.shape[0]-1, -1, -1):
                if row == self.shape[0]-1:
                    vis[row][col] = 1
                else:
                    if self.data[row][col] > max(current_list[row+1:self.shape[0]]):
                        vis[row][col] = 1
        return vis

    def _visibility_from_left(self) -> list[list[int]]:
        vis = self.generate(value=0, shape=self.shape)
        for row in range(0, self.shape[0]):
            current_list = [self.data[row][i] for i in range(0, self.shape[0])]
            for col in range(0, self.shape[1]):
                if col == 0:
                    vis[row][col] = 1
                else:
                    if self.data[row][col] > max(current_list[0:col]):
                        vis[row][col] = 1
        return vis

    def _visibility_from_right(self) -> list[list[int]]:
        vis = self.generate(value=0, shape=self.shape)
        for row in range(self.shape[0]-1, -1, -1):
            current_list = [self.data[row][i] for i in range(0, self.shape[0])]
            for col in range(self.shape[1]-1, -1, -1):
                if col == self.shape[1]-1:
                    vis[row][col] = 1
                else:
                    if self.data[row][col] > max(current_list[col+1:self.shape[1]]):
                        vis[row][col] = 1
        return vis

    def _visibility_compare(self, maps: list[list[list[int]]]) -> list[list[int]]:
        vis = maps[0]
        for page in range(1, len(maps)):
            for row in range(0, self.shape[0]):
                for col in range(0, self.shape[1]):
                    vis[row][col] = int(bool(vis[row][col]) or bool(maps[page][row][col]))
        return vis

    def score(self):
        scores = []
        to_top = self._score_to_top()
        print(self._score_to_bottom())




    def _score_to_top(self) -> list[list[int]]:
        data = np.array(self.data)
        vis = np.zeros(shape=self.shape, dtype=int)
        vis[1, :] = 1
        for col in range(0, self.shape[1]):
            for row in range(2, self.shape[0]):
                current = np.flip(data[:row, col])
                if data[row][col] == current[0]:
                    vis[row][col] = 1
                else:
                    max, idx = np.max(current), np.argmax(current)
                    if vis[row][col] > max:
                        vis[row][col] = row
                    else:
                        vis[row][col] = idx + 1
        return vis

    def _score_to_bottom(self) -> list[list[int]]:
        data = np.array(self.data)
        vis = np.zeros(shape=self.shape, dtype=int)
        vis[-2, :] = 1
        for col in range(0, self.shape[1]):
            for row in range(self.shape[0]-2, -1, -1):
                current = data[0:np.abs(row+1), col]
                print(row, current)
                # if data[row][col] == current[0]:
                #     vis[row][col] = 1
                # else:
                #     max, idx = np.max(current), np.argmax(current)
                #     if vis[row][col] > max:
                #         vis[row][col] = row
                #     else:
                #         vis[row][col] = idx + 1
        return vis

    def _score_to_left(self) -> list[list[int]]:
        vis = self.generate(value=0, shape=self.shape)
        for row in range(0, self.shape[0]):
            current_list = [self.data[row][i] for i in range(0, self.shape[0])]
            for col in range(0, self.shape[1]):
                if col == 0:
                    vis[row][col] = 1
                else:
                    if self.data[row][col] > max(current_list[0:col]):
                        vis[row][col] = 1
        return vis

    def _score_to_right(self) -> list[list[int]]:
        vis = self.generate(value=0, shape=self.shape)
        for row in range(self.shape[0]-1, -1, -1):
            current_list = [self.data[row][i] for i in range(0, self.shape[0])]
            for col in range(self.shape[1]-1, -1, -1):
                if col == self.shape[1]-1:
                    vis[row][col] = 1
                else:
                    if self.data[row][col] > max(current_list[col+1:self.shape[1]]):
                        vis[row][col] = 1
        return vis

    def _ind2sub(self, lin_idx: int):
        row = lin_idx // self.shape[0]
        col = lin_idx % self.shape[1]
        return row, col

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
    mat = Matrix(file="test_input.txt")
    print(f"Forest:\n{mat.show()}")

    # vis_map = mat.visibility()
    # print(f"Visibility map:\n{vis_map.show()}")
    # print(f"Number of visible trees: {sum(vis_map.flattened)}")

    mat.score()
