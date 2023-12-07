from lib import *

year, day = 2022, 1

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()

totals = []
total = 0

for line in lines:
    try:
        i = int(line)
        total += i
    except:
        totals.append(total)
        total = 0

totals.sort(reverse=True)
ans(sum(totals[:3]))
