seeds = []
mappings = []

# 7
actual = "./input/day5.txt"
test = "test.txt"
file_path = actual

with open(file_path, "+r") as file:
    seeds = list(
        map(int, file.readline().split(":")[1].strip().split(" ")))

    file.readline()
    file.readline()
    current = []
    for line in file:
        if line == "\n":
            mappings.append(current)
            current = []
            file.readline()
            continue

        dest, src, n = map(int, line.split(" "))
        current.append((dest, src, n))
    mappings.append(current)


def find_mapping(value, n, mapping):
    news = []
    vend = value + n - 1
    for (dest, src, m) in mappings[mapping]:
        sen = src + m - 1
        if value <= sen and vend >= src:
            cutoff = src - value
            if cutoff > 0:
                news.extend(find_mapping(value, cutoff, mapping))
                news.extend(find_mapping(src, n - cutoff, mapping))
                break

            cutoff = vend - sen
            if cutoff > 0:
                news.extend(find_mapping(sen + 1, cutoff, mapping))
                news.extend(find_mapping(value, n - cutoff, mapping))
                break

            news.append([dest + (value - src), n])
            break

    if len(news) == 0:
        return [(value, n)]
    return news


min_loc = 0xfffffffffffff
for i in range(0, len(seeds), 2):
    seed, n = (seeds[i], seeds[i + 1])
    next = [(seed, n)]
    for j in range(len(mappings)):
        current = next
        next = []
        for see, m in current:
            next.extend(find_mapping(see, m, j))
    for final in next:
        min_loc = min(min_loc, final[0])

print(min_loc)
