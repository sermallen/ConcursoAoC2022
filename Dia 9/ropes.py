with open("Dia 9/input.txt") as file:
    # initial position
    Head = [0,0]
    Tail = [0,0]
    tailPositions = []
    while True:
        line = file.readline()
        if not line: break

        line = line.split()
        direction = line[0]
        steps = int(line[1])

        for i in range(steps):
            if direction == "R":
                Head[0] += 1
            elif direction == "L":
                Head[0] -= 1
            elif direction == "U":
                Head[1] += 1
            elif direction == "D":
                Head[1] -= 1

            if abs(Head[0]-Tail[0]) > 1:
                if Head[0] > Tail[0]:
                    Tail[0] = Head[0] - 1
                    Tail[1] = Head[1]
                else:
                    Tail[0] = Head[0] + 1
                    Tail[1] = Head[1]
            if abs(Head[1]-Tail[1]) > 1:
                if Head[1] > Tail[1]:
                    Tail[1] = Head[1] - 1
                    Tail[0] = Head[0]
                else:
                    Tail[1] = Head[1] + 1
                    Tail[0] = Head[0]
            
            tailPositions.append([Tail[0],Tail[1]])

notduplicated = []
for position in tailPositions:
    if position not in notduplicated:
        notduplicated.append(position)
print(notduplicated.__len__())