import os


class Tree(object):
    weights_lower = 0
    total_space = 70000000
    least_space = 30000000

    def __init__(self, name: str = "", subtree=None):
        self.name = name
        self.subtree = []
        self.files = []
        if subtree is not None:
            for sub in subtree:
                self.add_subtree(sub)

    def add_subtree(self, subtree, verbose: bool = False):
        if isinstance(subtree, Tree):
            if subtree.name not in self.subtree:
                if verbose:
                    print(f"Added subtree {subtree.name} in {self.name}")
                self.subtree.append(subtree)
        else:
            raise "Not a Tree instance!"

    def add_file(self, name: str, weight: float, verbose: bool = False):
        if verbose:
            print(f"Added file {name} in {self.name}")
        self.files.append({'name': name, 'weight': weight})

    def get_dirs_thinner_than(self, weight:int, level: int = 0, verbose: bool = False):
        if self.weight < weight:
            if verbose:
                print(level * "\t" + "- " + self.name + " (dir, size=" + str(self.weight) + ")")
            r = self.weight
            Tree.weights_lower = Tree.weights_lower + r
        level += 1
        for sub in self.subtree:
            sub.get_dirs_thinner_than(weight=weight, verbose=verbose, level=level)
        return Tree.weights_lower

    @property
    def weight(self):
        weight = 0
        for file in self.files:
            weight += int(file["weight"])
        for sub in self.subtree:
            weight += sub.weight
        return weight

    def __str__(self):
        return f"""
        Name: {self.name}
        Files: {self.files}
        File weight: {self.weight}
        Subtree: {[sub.name for sub in self.subtree]}
        """

    def show(self, level: int = 0):
        print(level*"\t" + "- " + self.name + " (dir, size=" + str(self.weight) + ")")
        for file in self.files:
            print((level+1)*"\t" + "- " + file["name"] + " (file, size=" + str(file["weight"]) + ")")
        level += 1
        for sub in self.subtree:
            sub.show(level=level)



def process_cd(line: str, cwd: str) -> str:
    if line[5:] == "/":
        return "\\"
    elif line[5:] == "..":
        return os.path.dirname(cwd)
    else:
        return os.path.join(cwd, line[5:])

def process_dirname(dirname: str):
    tup = dirname.split("\\")
    names = []
    for t in tup:
        if t:
            names.append(t)
    return names


if __name__ == "__main__":

    with open("puzzle_input.txt") as f:
        lines = f.read().splitlines()

    curdir = []
    level = 0
    root_tree = Tree(name="\\")
    current_tree = root_tree
    for idx, line in enumerate(lines):
        if line[0] == "$":
            if line[2:4] == "cd":
                newdir = process_cd(line, curdir)
                if newdir == "\\":
                    current_tree = root_tree
                else:
                    names = process_dirname(newdir)
                    current_tree = root_tree
                    for name in names:
                        subnames = []
                        for sub in current_tree.subtree:
                            subnames.append(sub.name)
                        idx = subnames.index(name)
                        current_tree = current_tree.subtree[idx]
                curdir = newdir
        else:
            if line[0:3] == "dir":
                current_tree.add_subtree(Tree(name=line[4:]))
            else:
                weight, name = line.split()
                current_tree.add_file(name=name, weight=weight)


#root_tree.show()
print(f"Sum of dir weights (at most 100k, include duplicates): {root_tree.get_dirs_thinner_than(weight=100_000, verbose=False)}")