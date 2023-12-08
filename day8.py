from math import gcd


instructions = ""
nodes = {}
#
with open("input/day8.txt") as file:
    instructions = file.readline()[:-1]
    file.readline()

    for line in file:
        node, children = line.split(" = ")
        nodes[node] = children.replace("(", "").replace(")\n", "").split(", ")


def choose_next(node, instruction):
    if instruction == "L":
        return node[0]
    return node[1]


def find_Z(current):
    cnt = 0
    while current[2] != "Z":
        instruction = instructions[cnt % len(instructions)]
        current = choose_next(nodes[current], instruction)
        cnt += 1
    return cnt


def least_common_multiple(nums):
    lcm = 1
    for num in nums:
        lcm = lcm * num // gcd(lcm, num)
    return lcm


As = list(filter(lambda x: x[2] == "A", nodes.keys()))

Zs = []
for A in As:
    Zs.append(find_Z(A))

print(least_common_multiple(Zs))
