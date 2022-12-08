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
        pass

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
    #mat = Matrix(data=1, shape=(3, 3))

    mat.show()
