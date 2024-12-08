from lib import *

year, day = 2024, 8

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# """.splitlines()

total = 0

antennas = defaultdict(list)

grid = Grid(lines)
for c in grid:
    if grid[c] != '.':
        antennas[grid[c]].append(c)

antinodes = set()

for freq, lst in antennas.items():
    for el1, el2 in itertools.combinations(lst, 2):
        diff = el2 - el1
        
        # Part 01
        # for i in ((el1 - diff), (el2 + diff)):
        #     if i in grid:
        #         antinodes.add(i.tup)
        # continue

        # Part 02
        i = el1
        while i in grid:
            antinodes.add(i.tup)
            i = i - diff
        j = el2
        while j in grid:
            antinodes.add(j.tup)
            j = j + diff

ans(len(antinodes))
