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
start = Coor(65,65)

"""
>>> x = 26501365-65
>>> x //= 131
>>> x
202300
>>> pairs = x // 2
>>> total = 0
>>> total += ((pairs * 2) ** 2) * not_start
>>> total += (((pairs * 2) - 1) ** 2) * start
>>> total += (x-1) * (big_pieces)
>>> total += middle_pieces
>>> total += x * (small_pieces)
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
