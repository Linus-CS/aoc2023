

times = [53, 89, 76, 98]
distances = [313, 1090, 1214, 1201]
times = [53897698]
distances = [313109012141201]

# times = [7, 15, 30]
# distances = [9, 40, 200]

total = 1

for i in range(len(times)):
    l = 0
    r = times[i]

    distL = 0
    distR = 0
    while distL <= distances[i] or distR <= distances[i]:
        if distL <= distances[i]:
            l += 1
            distL = l * (times[i] - l)

        if distR <= distances[i]:
            r -= 1
            distR = r * (times[i] - r)

    total *= (r - l + 1)

print(total)
