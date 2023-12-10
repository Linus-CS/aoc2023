pipes = []
with open("input/day10.txt", "+r") as file:
    for line in file:
        pipes.append(line[:-1])


def check_above(i, j):
    if i > 0:
        tile = pipes[i - 1][j]
        if tile == "|" or tile == "F" or tile == "7":
            return True
    return False


def check_below(i, j):
    if i < len(pipes) - 1:
        tile = pipes[i + 1][j]
        if tile == "|" or tile == "J" or tile == "L":
            return True
    return False


def check_left(i, j):
    if j > 0:
        tile = pipes[i][j - 1]
        if tile == "-" or tile == "L" or tile == "F":
            return True
    return False


def check_right(i, j):
    if j < len(pipes[0]) - 1:
        tile = pipes[i][j + 1]
        if tile == "-" or tile == "J" or tile == "7":
            return True
    return False


def move(tile):
    y, x, momentum = tile
    match pipes[y][x]:
        case "|":
            if momentum == "U":
                return (y - 1, x, "U")
            return (y + 1, x, "D")
        case "-":
            if momentum == "L":
                return (y, x - 1, "L")
            return (y, x + 1, "R")
        case "L":
            if momentum == "D":
                return (y, x + 1, "R")
            return (y - 1, x, "U")
        case "J":
            if momentum == "D":
                return (y, x - 1, "L")
            return (y - 1, x, "U")
        case "7":
            if momentum == "U":
                return (y, x - 1, "L")
            return (y + 1, x, "D")
        case "F":
            if momentum == "U":
                return (y, x + 1, "R")
            return (y + 1, x, "D")


def determin_start_tile():
    start = (-1, -1)
    for i in range(len(pipes)):
        if pipes[i].__contains__("S"):
            for j in range(len(pipes[i])):
                if pipes[i][j] == "S":
                    start = (i, j)
                    break
            break
    return start


def replace_at(y, x, c):
    pipes[y] = pipes[y][:x] + c + pipes[y][x + 1:]


def initial(start):
    y, x = start
    directions = []
    if check_above(start[0], start[1]):
        directions.append((y - 1, x, "U"))
    if check_below(start[0], start[1]):
        directions.append((y + 1, x, "D"))
    if check_left(start[0], start[1]):
        directions.append((y, x - 1, "L"))
    if check_right(start[0], start[1]):
        directions.append((y, x + 1, "R"))
    match (directions[0][2], directions[1][2]):
        case ("U", "D"):
            start = (y, x, "U")
            replace_at(y, x, "|")
        case ("D", "R"):
            start = (y, x, "L")
            replace_at(y, x, "F")
        case ("D", "L"):
            start = (y, x, "R")
            replace_at(y, x, "7")
        case ("U", "R"):
            start = (y, x, "L")
            replace_at(y, x, "J")
        case ("U", "L"):
            start = (y, x, "R")
            replace_at(y, x, "L")
        case ("L", "R"):
            start = (y, x, "L")
            replace_at(y, x, "-")
    return (start, directions[0], directions[1])


start, first, second = initial(determin_start_tile())
# print(start, "->", pipes[start[0]][start[1]])
# print(first, "->", pipes[first[0]][first[1]])
# print(second, "->", pipes[second[0]][second[1]])

cnt = 1
first_tiles = [start]
second_tiles = []
while first[0] != second[0] or first[1] != second[1]:
    first_tiles.append(first)
    second_tiles.append(second)
    cnt += 1
    first = move(first)
    second = move(second)
second_tiles.append(second)


def find_neighbors(tile):
    y, x, momentum = tile
    symbol = pipes[y][x]

    match symbol:
        case "|":
            right = [(y, x + 1)]
            left = [(y, x - 1)]
            if x == len(pipes[0]) - 1:
                right = []
            if x == 0:
                left = []
            if momentum == "U":
                return (left, right)
            return (right, left)
        case "-":
            right = [(y - 1, x)]
            left = [(y + 1, x)]
            if y == 0:
                right = []
            if y == len(pipes) - 1:
                left = []
            if momentum == "L":
                return (left, right)
            return (right, left)
        case "F":
            left1 = (y, x - 1)
            left2 = (y - 1, x)
            final = []
            if x != 0:
                final.append(left1)
            if y != 0:
                final.append(left2)
            if momentum == "L":
                return ([], final)
            return (final, [])
        case "7":
            left1 = (y, x + 1)
            left2 = (y - 1, x)
            final = []
            if x != len(pipes[0]) - 1:
                final.append(left1)
            if y != 0:
                final.append(left2)
            if momentum == "R":
                return (final, [])
            return ([], final)
        case "L":
            left1 = (y, x - 1)
            left2 = (y + 1, x)
            final = []
            if x != 0:
                final.append(left1)
            if y != len(pipes) - 1:
                final.append(left2)
            if momentum == "L":
                return (final, [])
            return ([], final)
        case "J":
            left1 = (y, x + 1)
            left2 = (y + 1, x)
            final = []
            if x != len(pipes[0]) - 1:
                final.append(left1)
            if y != len(pipes) - 1:
                final.append(left2)
            if momentum == "R":
                return ([], final)
            return (final, [])

    return ([], [])


lefts = []
rights = []
for i in range(cnt):
    left, right = find_neighbors(first_tiles[i])
    lefts.extend(left)
    rights.extend(right)

    right, left = find_neighbors(second_tiles[i])
    lefts.extend(left)
    rights.extend(right)

combines = first_tiles
combines.extend(second_tiles)
combines = list(map(lambda x: (x[0], x[1]), combines))

lefts = set(filter(lambda x: x not in combines, lefts))
rights = set(filter(lambda x: x not in combines, rights))

min_x = len(pipes[0])
min_y = len(pipes)
max_x = 0
max_y = 0

for y, x in combines:
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    max_x = max(x, max_x)
    max_y = max(y, max_y)

not_pipe = []
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        tile = (y, x)
        if tile not in combines and tile not in lefts and tile not in rights:
            not_pipe.append((y, x))


def has_neigh(y, x):
    tile = (y - 1, x)
    if tile in lefts:
        return True
    tile = (y + 1, x)
    if tile in lefts:
        return True
    tile = (y, x - 1)
    if tile in lefts:
        return True
    tile = (y, x + 1)
    if tile in lefts:
        return True
    return False


changes = 1
while changes != 0:
    changes = 0
    dels = []
    for y, x in not_pipe:
        if has_neigh(y, x):
            changes += 1
            lefts.add((y, x))
            dels.append((y, x))

    not_pipe = list(filter(lambda e: e not in dels, not_pipe))


print(len(lefts))


def print_everything():
    for y, x in rights:
        replace_at(y, x, "I")
    for pipe in pipes:
        print(pipe)


# print_everything()
