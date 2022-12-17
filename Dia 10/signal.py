x = 1
cycle = 1
signals = 0

def checkcycle(signals):
    if cycle == 20:
        signals += (20*x)
        print(20*x)
    elif cycle == 60:
        signals += (60*x)
        print(60*x)
    elif cycle == 100:
        signals += (100*x)
        print(100*x)
    elif cycle == 140:
        signals += (140*x)
        print(140*x)
    elif cycle == 180:
        signals += (180*x)
        print(180*x)
    elif cycle == 220:
        signals += (220*x)
        print(220*x) 
    return signals
    
with open("Dia 10/input.txt") as file:
    while True:
        line = file.readline()
        if not line: break
        line = line.split()
        if line[0] == "noop":
            cycle += 1
            signals = checkcycle(signals)
        elif line[0] == "addx":
            cycle += 1
            signals = checkcycle(signals)
            x += int(line[1])
            cycle += 1
            signals = checkcycle(signals)

print(signals)