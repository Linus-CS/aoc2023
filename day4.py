def get_matches(winning, selected):
    winning = sorted(winning)
    selected = sorted(selected)

    score = 0
    i = 0
    j = 0
    while i < len(winning) and j < len(selected):
        w = winning[i]
        s = selected[j]
        print(w, s)
        if w > s:
            j += 1
            continue

        if s > w:
            i += 1
            continue

        if w == s:
            score += 1
            i += 1
            j += 1

    return score


cards = {}
card = 0
with open("./input/day4.txt") as file:
    for line in file:
        card += 1
        cards[card] = 1 if card not in cards else cards[card] + 1
        stripped = line.split(":")[1]
        winning, selected = map(lambda x: x.strip(), stripped.split("|"))
        winning = list(map(int, filter(lambda x: x != "", winning.split(" "))))
        selected = list(
            map(int, filter(lambda x: x != "", selected.split(" "))))

        num_matches = get_matches(winning, selected)

        for i in range(card + 1, card + num_matches + 1):
            cards[i] = cards[card] if i not in cards else cards[i] + cards[card]

print(sum(cards.values()))
