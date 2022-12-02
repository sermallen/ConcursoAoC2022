maxelf = []
actualelf = 0
with open("Dia 1/input.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        if line == "\n":
            maxelf.append(actualelf)
            actualelf = 0
        else:
            actualelf += int(line)

maxelf.sort(reverse=True)
print(maxelf[0] + maxelf[1] + maxelf[2])