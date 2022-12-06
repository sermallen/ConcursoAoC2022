fulloverlaps = 0
with open("Dia 4/input.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        line = line.split(sep=",")
        pair1 = line[0].split("-")
        pair2 = line[1].split("-")

        if ((int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1])) 
         or (int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1]))):
            fulloverlaps += 1

print(fulloverlaps)        