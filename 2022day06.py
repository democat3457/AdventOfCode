from lib import *

year, day = 2022, 6

puzzle_input = load(year, day)
line = puzzle_input.splitlines()[0]

for i in range(len(line)):
    if i < 13:
        continue

    if len(set(line[i-13:i+1])) == 14:
        ans(i)
        break
