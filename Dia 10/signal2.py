x = 1
cycle = 0
crt = []

def printcrt():
    if x == cycle%40 or x-1 == cycle%40 or x+1 == cycle%40:
        crt.append("#")
    else:
        crt.append(".")

with open("Dia 10/input.txt") as file:
    while True:
        line = file.readline()
        if not line: break
        line = line.split()
        if line[0] == "noop":
            if x == cycle%40 or x-1 == cycle%40 or x+1 == cycle%40:
                crt.append("#")
            else:
                crt.append(".")
            cycle += 1
        elif line[0] == "addx":
            if x == cycle%40 or x-1 == cycle%40 or x+1 == cycle%40:
                crt.append("#")
            else:
                crt.append(".")
            cycle += 1
            if x == cycle%40 or x-1 == cycle%40 or x+1 == cycle%40:
                crt.append("#")
            else:
                crt.append(".")
            x += int(line[1])
            cycle += 1

row = [[],[],[],[],[],[]]
for i in range(40):
    row[0] += crt[i]
    row[1] += crt[i+40]
    row[2] += crt[i+80]
    row[3] += crt[i+120]
    row[4] += crt[i+160]
    row[5] += crt[i+200]

print(row[0])
print(row[1])
print(row[2])
print(row[3])
print(row[4])
print(row[5])
