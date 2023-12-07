from lib import *

year, day = 2023, 3

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """.splitlines()

grid = truthy_list(lines)

gears = defaultdict(list)

def get_at(i: int, j: int):
    return get_element_in_arrays(grid, (i,j), ' ')

def any_symbols_adjacent(i: int, j: int):
    l = [get_at(i+m,j+n) not in ' .1234567890' for m in (-1,0,1) for n in (-1,0,1)]
    # print(i,j,l)
    return any(l)

def gear_adjacent(i: int, j: int):
    l = [(get_at(i+m,j+n) == '*', (i+m, j+n)) for m in (-1,0,1) for n in (-1,0,1)]
    # print(i,j,l)
    return list(map(operator.itemgetter(1), filter(lambda x: x[0], l)))

total = 0

for i, line in enumerate(grid):
    j = 0
    while j < len(line):
        match = re.match('(\d+)', line[j:])
        if match:
            s = match.group(1)
            n = int(s)
            gears_adj = set()
            for k in range(len(s)):
                # Part 01
                # if any_symbols_adjacent(i, j+k):
                #     total += n
                #     # print(n, k)
                #     break

                for ga in gear_adjacent(i, j+k):
                    gears_adj.add(ga)
            for ga in gears_adj:
                gears[ga].append(n)
            j += len(s)
        else:
            j += 1

# Part 01
# ans(total)

# Part 02
# print(gears)
for gal in gears.values():
    if len(gal) == 2:
        total += gal[0] * gal[1]

ans(total)
