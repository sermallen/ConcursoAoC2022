score = 0
with open("Dia 2/input.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        lineSplited = line.split()
        # election score
            # A,X: rock     +1
            # B,Y: paper    +2
            # C,Z: scissor  +3
        if lineSplited[1] == "X":
            score += 1
        elif lineSplited[1] == "Y":
            score += 2
        elif lineSplited[1] == "Z":
            score += 3

        # match score
            # win    +6
            # lose   +0
            # tie    +3
        
        # tie
        if ((lineSplited[0] == "A" and lineSplited[1] == "X")
         or (lineSplited[0] == "B" and lineSplited[1] == "Y")
         or (lineSplited[0] == "C" and lineSplited[1] == "Z")): 
            score += 3
        # win
        elif ((lineSplited[0] == "A" and lineSplited[1] == "Y")     # rock vs paper
            or(lineSplited[0] == "B" and lineSplited[1] == "Z")     # paper vs scissor
            or(lineSplited[0] == "C" and lineSplited[1] == "X")):   # scissor vs rock
            score += 6
        # lose do nothing

print(score)