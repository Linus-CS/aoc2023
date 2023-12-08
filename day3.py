from functools import reduce
import re

lines = []
numbers = []
with open("./input/day3.txt", "+r") as file:
    lines = file.readlines()


def isSymbol(c):
    return c != '.' and (c < '0' or c > '9')


def containsSymbol(txt):
    return reduce(lambda acc, x: acc or isSymbol(x), txt, False)


def findGear(txt):
    for i in range(len(txt)):
        if txt[i] == '*':
            return i
    return -1


gears = {}

sum = 0
for i in range(len(lines)):
    line = lines[i]
    matches = re.finditer("[0-9]+", line)

    for num_match in matches:
        num = int(num_match.group())
        s = num_match.start()
        e = num_match.end() - 1
        l = max(0, s - 1)
        r = min(e + 2, len(lines[i - 1]) - 1)

        result = False
        if i > 0:
            gear = findGear(lines[i - 1][l:r])
            if gear != -1:
                pos = (i - 1, l + gear)
                gears[pos] = [num] if pos not in gears else gears[pos] + [num]

        gear = findGear(line[l:r])
        if gear != -1:
            pos = (i, l + gear)
            gears[pos] = [num] if pos not in gears else gears[pos] + [num]

        if i < len(lines) - 1:
            gear = findGear(lines[i + 1][l:r])
            if gear != -1:
                pos = (i + 1, l + gear)
                gears[pos] = [num] if pos not in gears else gears[pos] + [num]


for pair in gears.values():
    if len(pair) == 2:
        x, y = pair
        sum += x * y

print(sum)
