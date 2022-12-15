from lib import *

year, day = 2022, 3

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()

total = 0

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for l0, l1, l2 in zip(lines[0::3], lines[1::3], lines[2::3]):
    l0 = set(l0)
    l1 = set(l1)
    l2 = set(l2)

    try:
        c = next(iter(l0.intersection(l1).intersection(l2)))
        total += s.index(c) + 1
    except:
        pass



ans(total)
