
rows = []
double_rows = []
with open("input/day11.txt", "+r") as file:
    i = 0
    for line in file:
        rows.append(line[:-1])
        if '#' not in rows[i]:
            double_rows.append(i)
        i += 1


def find_tags():
    tags = []
    for col in range(len(rows[0])):
        for row in range(len(rows)):
            if rows[row][col] == "#":
                tags.append([col, row])
    return tags


tags = find_tags()
new_tags = []
for t in tags:
    new_tags.append(t.copy())

factor = 1000000


def expand_xs(row):
    for i in range(len(tags)):
        if tags[i][1] > row:
            new_tags[i][1] += factor - 1


def expand_ys(col):
    for i in range(len(tags)):
        if tags[i][0] > col:
            new_tags[i][0] += factor - 1


for d_row in double_rows:
    expand_xs(d_row)

for col in range(len(rows[0])):
    should_double = True
    for row in range(len(rows)):
        if rows[row][col] == "#":
            should_double = False
            break
    if should_double:
        expand_ys(col)


def dist(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    return abs(x1 - x2) + abs(y1 - y2)


sum = 0
for i in range(len(new_tags)):
    for j in range(i + 1, len(new_tags)):
        sum += dist(new_tags[i], new_tags[j])

print(sum)


def print_all():
    for row in rows:
        print(row)
