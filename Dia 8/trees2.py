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
        tree = forest[i][j]
        if (i == 0 or i == x_size-1 or j == 0 or j == y_size-1): # edges
            pass
        else:
            treeview = 1
            for l in range(j-1, -1, -1): 
                if forest[i][l] >= tree:
                    treeview *= j-l
                    break
                elif l == 0:
                    treeview *= j-l
            for l in range(j+1, x_size):
                if forest[i][l] >= tree:
                    treeview *= l-j
                    break
                elif l == x_size-1:
                    treeview *= l-j
            for k in range(i-1, -1, -1):
                if forest[k][j] >= tree:
                    treeview *= i-k
                    break
                elif k == 0:
                    treeview *= i-k
            for k in range(i+1, y_size):
                if forest[k][j] >= tree:
                    treeview *= k-i
                    break
                elif k == y_size-1:
                    treeview *= k-i
            if treeview > sol: sol = treeview

print(sol)
