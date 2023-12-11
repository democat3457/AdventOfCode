from lib import *

year, day = 2023, 11

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# """.splitlines()

lines = truthy_list(lines)

galaxies: list[tuple[int,int]] = []
empty_rows: list[int] = []
tmpcols: dict[int, bool] = {}
width = len(lines[0])

for i, line in enumerate(lines):
    empty = True
    for j, c in enumerate(line):
        if c == '#':
            galaxies.append((i,j))
            empty = False
            tmpcols[j] = False
    if empty:
        empty_rows.append(i)

empty_cols: list[int] = [ i for i in range(width) if i not in tmpcols ]

total = 0

for i, g1 in enumerate(galaxies):
    for g2 in galaxies[i+1:]:
        total += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])

# Part 01
# mult = 1

mult = 999999

for r in empty_rows:
    total += mult * sum(1 for a,b in galaxies if a < r) * sum(1 for a,b in galaxies if a > r)
for c in empty_cols:
    total += mult * sum(1 for a,b in galaxies if b < c) * sum(1 for a,b in galaxies if b > c)

ans(total)
