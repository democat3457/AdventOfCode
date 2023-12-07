from lib import *

year, day = 2023, 7

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# """.splitlines()

# Part 01
# ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

ranks = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def get_type(card: str):
    # Part 01
    # if True:
    if 'J' not in card:
        counts = tuple(sorted([card.count(c) for c in set(card)], reverse=True))
        types = [
            (5,),
            (4,1),
            (3,2),
            (3,1,1),
            (2,2,1),
            (2,1,1,1),
            (1,1,1,1,1),
        ]
        ret = types.index(counts)
    else:
        cs = set(card)
        cs.remove('J')
        min_ret = 1000
        for r in cs:
            new_card = card.replace('J', r)
            counts = tuple(sorted([new_card.count(c) for c in set(new_card)], reverse=True))
            types = [
                (5,),
                (4,1),
                (3,2),
                (3,1,1),
                (2,2,1),
                (2,1,1,1),
                (1,1,1,1,1),
            ]
            min_ret = min(min_ret, types.index(counts))
        if not len(cs):
            min_ret = 0
        ret = min_ret

    strength = tuple([(ranks.index(c)) for c in card])
    strength = ''.join(map(lambda x: str(x).rjust(2, '0'), strength))

    return ret, int(strength)

total = 0

lines = truthy_list(lines)
cards = []
for line in lines:
    card, bid = (line.split())
    bid = int(bid)
    t, s = get_type(card)
    cards.append((t, s, bid, card))

cards.sort(key=lambda t: t[0]*100000000000000 + t[1], reverse=True)
# print(cards)

for i, c in enumerate(cards):
    total += (i+1) * c[2]

ans(total)
