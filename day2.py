import re

red = 12
green = 13
blue = 14

sum = 0
game = 0
with open("./input/day2.txt", "+r") as file:
    for line in file:
        game += 1
        half = line.split(":")[1]
        sets = half.split(";")
        maxRed, maxGreen, maxBlue = (0, 0, 0)
        for set in sets:
            stripped = set.strip()
            nRed = re.search("[0-9]+ red", stripped)
            nGreen = re.search("[0-9]+ green", stripped)
            nBlue = re.search("[0-9]+ blue", stripped)
            if nRed != None:
                n = int(nRed.group().split(" ")[0])
                maxRed = max(maxRed, n)

            if nGreen != None:
                n = int(nGreen.group().split(" ")[0])
                maxGreen = max(maxGreen, n)

            if nBlue != None:
                n = int(nBlue.group().split(" ")[0])
                maxBlue = max(maxBlue, n)

        power = maxRed * maxGreen * maxBlue
        sum += power

print(sum)
