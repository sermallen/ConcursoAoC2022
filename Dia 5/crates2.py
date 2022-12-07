stacks = [
    ["H","B","V","W","N","M","L","P"],      # 1
    ["M","Q","H"],                          # 2
    ["N","D","B","G","F","Q","M","L"],      # 3
    ["Z","T","F","Q","M","W","G"],          # 4
    ["M","T","H","P"],                      # 5
    ["C","B","M","J","D","H","G","T"],      # 6
    ["M","N","B","F","V","R"],              # 7
    ["P","L","H","M","R","G","S"],          # 8
    ["P","D","B","C","N"]                   # 9
    ]

with open("Dia 5/input.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        splited = line.split()
        cuantity = int(splited[1])
        fRom = int(splited[3])
        to = int(splited[5])
        
        auxstack = []
        while(cuantity != 0):
            crate = stacks[fRom-1].pop()
            auxstack.append(crate)
            cuantity -= 1
        auxstack.reverse()
        for auxcrate in auxstack:
            stacks[to-1].append(auxcrate)

sol = ""
for stack in stacks:
    if stack.__len__() != 0:
        sol += stack[-1]

print(sol)