badges = []
with open("Dia 3/input.txt") as file:
    while True:
        line1 = file.readline()
        if not line1:
            break
        line2 = file.readline()
        line3 = file.readline()

        for item in line1:
            if item != "\n" and line2.count(item) != 0 and line3.count(item) != 0:
                badges.append(item)
                break
        

priority = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

sumPriorities = 0
for b in badges:
    sumPriorities += priority.index(b)+1

print(sumPriorities)
