score = 0
with open("Dia 2/input.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        lineSplited = line.split()

        # match score
            # X: lose   +0
            # Y: tie    +3
            # Z: win    +6
        # election score
            # A: rock     +1
            # B: paper    +2
            # C: scissor  +3
        # tie
        if lineSplited[1] == "Y":
            score += 3
            if lineSplited[0] == "A":
                score += 1
            elif lineSplited[0] == "B":
                score += 2
            elif lineSplited[0] == "C":
                score += 3
        # win
        elif lineSplited[1] == "Z":
            score += 6
            if lineSplited[0] == "A":   # need paper
                score += 2
            elif lineSplited[0] == "B": # need scissor
                score += 3
            elif lineSplited[0] == "C": # need rock
                score += 1
        # lose
        elif lineSplited[1] == "X":
            if lineSplited[0] == "A":   # need scissor
                score += 3
            elif lineSplited[0] == "B": # need rock
                score += 1
            elif lineSplited[0] == "C": # need paper
                score += 2

print(score)