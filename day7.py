FIVE_KIND = 7
FOUR_KIND = 6
FULL_HOUSE = 5
THREE_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1


def determine_type(hand):
    card_map = {}
    jokers = 0
    for c in hand:
        if c == "J":
            jokers += 1
            continue
        card_map[c] = 1 if c not in card_map else card_map[c] + 1

    if jokers == 5:
        return FIVE_KIND

    match len(card_map):
        case 1:
            return FIVE_KIND
        case 2:
            if list(card_map.values()).__contains__(4):
                return FOUR_KIND
            if jokers >= 2:
                return FOUR_KIND
            if jokers == 1 and list(card_map.values()).__contains__(3):
                return FOUR_KIND
            return FULL_HOUSE

        case 3:
            if list(card_map.values()).__contains__(3):
                return THREE_KIND
            if jokers >= 1:
                return THREE_KIND
            return TWO_PAIR
        case 4:
            return ONE_PAIR
        case _:
            return HIGH_CARD


def convert_to_hex(hand):
    hand = hand.replace("T", "a")
    hand = hand.replace("J", "1")
    hand = hand.replace("Q", "c")
    hand = hand.replace("K", "d")
    hand = hand.replace("A", "e")
    return int(hand, 16)


def read_hands():
    hands = []
    with open("input/day7.txt", "+r") as file:
        for line in file:
            hand, bid = line.split(" ")
            hands.append(
                (determine_type(hand), convert_to_hex(hand), int(bid)))
    return hands


hands = read_hands()
sorted_hands = sorted(hands)
result = 0
rank = 1
for hand in sorted_hands:
    print(hand[0], hex(hand[1]))
    result += rank * hand[2]
    rank += 1

print(result)
