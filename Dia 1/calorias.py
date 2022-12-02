maxelf = 0
actualelf = 0
with open("Dia 1/input.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        if line == "\n":
            if maxelf < actualelf:
                maxelf = actualelf
            actualelf = 0
        else:
            actualelf += int(line)

print(maxelf)