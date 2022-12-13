forest = []
with open("Dia 8/input.txt") as file:
    while True:
        line = file.readline()
        if not line: break
        line = line.split()
        line = line[0]
        forest.append(line)

sol = 0
y_size = forest.__len__()
x_size = forest[0].__len__()

for i in range(x_size):
    for j in range(y_size):
        visible = False
        if (i == 0 or i == x_size-1 or j == 0 or j == y_size-1): # edges
            sol += 1
        else:
            tree = forest[i][j]
            visible = True
            for l in range(j):
                if forest[i][l] >= tree:
                    visible = False
                    break
            if not visible:
                visible = True
                for l in range(x_size-1,j,-1):
                    if forest[i][l] >= tree:
                        visible = False
                        break
            if not visible:
                visible = True
                for k in range(i):
                    if forest[k][j] >= tree:
                        visible = False
                        break
            if not visible:
                visible = True
                for k in range(y_size-1,i,-1):
                    if forest[k][j] >= tree:
                        visible = False
                        break
        if visible: sol += 1

print(sol)
