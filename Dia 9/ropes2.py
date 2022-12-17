with open("Dia 9/input.txt") as file:
    tailLenght = 9
    # initial position
    rope = [[0,0], #head
            [0,0], #1
            [0,0], #2
            [0,0], #3
            [0,0], #4
            [0,0], #5
            [0,0], #6
            [0,0], #7
            [0,0], #8
            [0,0]  #9
    ]
    tailPositions = []
    while True:
        line = file.readline()
        if not line: break

        line = line.split()
        direction = line[0]
        steps = int(line[1])

        for i in range(steps):
            if direction == "R":
                rope[0][0] += 1
            elif direction == "L":
                rope[0][0] -= 1
            elif direction == "U":
                rope[0][1] += 1
            elif direction == "D":
                rope[0][1] -= 1

            for tail in range(tailLenght):
                actual = rope[tail + 1]
                anterior = rope[tail]
                if abs(anterior[0]-actual[0]) > 1 and abs(anterior[1]-actual[1]) > 1:
                    if anterior[0] > actual[0] and anterior[1] > actual[1]:
                        actual[0] = anterior[0]-1
                        actual[1] = anterior[1]-1
                    elif anterior[0] > actual[0]:
                        actual[0] = anterior[0]-1
                        actual[1] = anterior[1]-1
                    elif anterior[1] > actual[1]:
                        actual[0] = anterior[0]+1
                        actual[1] = anterior[1]-1
                    else:
                        actual[0] = anterior[0]+1
                        actual[1] = anterior[1]+1
                        pass
                if abs(anterior[0]-actual[0]) > 1:
                    if anterior[0] > actual[0]:
                        actual[0] = anterior[0] - 1
                        actual[1] = anterior[1]
                    else:
                        actual[0] = anterior[0] + 1
                        actual[1] = anterior[1]
                if abs(anterior[1]-actual[1]) > 1:
                    if anterior[1] > actual[1]:
                        actual[1] = anterior[1] - 1
                        actual[0] = anterior[0]
                    else:
                        actual[1] = anterior[1] + 1
                        actual[0] = anterior[0]
            tailPositions.append([rope[-1][0], rope[-1][1]])

notduplicated = []
for position in tailPositions:
    if position not in notduplicated:
        notduplicated.append(position)
print(notduplicated.__len__())