class Tree:
    def __init__(self, name, father, value):
        self.children = []
        self.name = name
        self.father = father
        self.value = value # if value==0: is a dir

with open("Dia 7/input.txt") as file:
    line = file.readline()
    root = Tree("/", None, 0)
    actual = root
    while True:
        line = file.readline()
        if not line: break
        line = line.split()

        if line[0] == "$" and line[1] == "cd":
            if line[2] == "..":
                actual = actual.father
            else:
                for children in actual.children:
                    if children.name == line[2]:
                        actual = children
                        break
        elif line[0] == "$" and line[1] == "ls":
            pass
        elif line[0] == "dir":
            actual.children.append(Tree(line[1], actual, 0))
        else:
            actual.children.append(Tree(line[1], actual, int(line[0])))

allvalues = []
def sumChildrens(father):
    for children in father.children:
        if children.value == 0:
            sumChildrens(children)
        father.value += children.value
    allvalues.append(father.value)

sumChildrens(root)

allvalues.sort()
availablespace = 70000000 - allvalues[-1]
for value in allvalues:
    if value + availablespace >= 30000000:
        print(value)
        break