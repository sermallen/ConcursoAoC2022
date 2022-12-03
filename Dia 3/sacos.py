duplicatedItems = []
with open("Dia 3/input.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        ruckSize = int(line.__len__()/2)
        for i in range(ruckSize):
            if line.count(line[i], ruckSize) != 0:
                duplicatedItems.append(line[i])
                break

priority = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

sumPriorities = 0
for item in duplicatedItems:
    sumPriorities += priority.index(item)+1

print(sumPriorities)
