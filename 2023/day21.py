from lib import *

year, day = 2023, 21

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# ...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ...........
# """.splitlines()

# Part 01 Example
# STEPS = 6
# Part 01
# STEPS = 64

# STEPS = 26501365
STEPS = 65
PARITY = 0

# start_parity == corner dot
# not_start    == corner O

lines = truthy_list(lines)
grid = Grid(lines)

# Part 01
# start = [c for c in grid if grid[c] == 'S'][0]
start = Coor(130,130)

# x start = 7282 (. on corner)
# x not start = 7331
# tl small = 950
# tl big = 6386
# bl small = 923
# bl big = 6390
# tr small = 941
# tr big = 6388
# br small = 925
# br big = 6408
# bm = 5516
# rm = 5514
# lm = 5494
# tm = 5492

"""
>>> x = 26501365-65
>>> x //= 131
>>> x
202300
>>> pairs = x // 2
>>> total = 0
>>> total += ((pairs * 2) ** 2) * 7331
>>> total += (((pairs * 2) - 1) ** 2) * 7282
>>> total += (x-1) * (6386+6390+6388+6408)
>>> total += 5516 + 5514 + 5494 + 5492
>>> total += x * (950+923+941+925)
>>> total
<ans>
"""

visited = {}
to_visit = deque([(start, 0)])
while len(to_visit) > 0:
    coor, steps = to_visit.popleft()
    if coor.tup in visited:
        continue
    if steps == (STEPS+1):
        break
    visited[coor.tup] = steps
    for add in ((-1,0),(1,0),(0,-1),(0,1)):
        new = coor+add
        if new in grid and grid[new] in '.S':
            to_visit.append((new, steps+1))

new_grid = grid.copy()
for k, v in visited.items():
    if v % 2 == PARITY:
        new_grid[k[0]][k[1]] = 'O'

print(str(new_grid))

ans(sum(1 for v in visited.values() if v % 2 == PARITY))
