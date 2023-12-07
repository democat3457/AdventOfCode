from lib import *

year, day = 2022, 4

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()

total = 0

for line in lines:
    if line:
        (l00, l01), (l10, l11) = map(lambda s: map(int, s.split("-")), line.split(","))

        if l00 <= l10 <= l01 or l00 <= l11 <= l01:
            total += 1
        elif l10 <= l00 <= l11 or l10 <= l01 <= l11:
            total += 1

ans(total)
