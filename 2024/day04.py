from lib import *

year, day = 2024, 4

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# """.splitlines()

grid = Grid(lines)
dirs = [ Coor(a,b) for a in range(-1,2) for b in range(-1,2) ]
dirs.remove(Coor(0,0))

diag = [
    (-1,-1),
    (-1,1),
    (1,1),
    (1,-1),
]

total = 0

# Part 01
# for c in grid:
#     if grid[c] == "X":
#         for dir in dirs:
#             if (
#                 (c + dir * 3) in grid
#                 and grid[c + dir] == "M"
#                 and grid[c + dir * 2] == "A"
#                 and grid[c + dir * 3] == "S"
#             ):
#                 total += 1
# ans(total)
# quit()

# Part 02
for c in grid:
    if grid[c] == 'A':
        if not all(grid.in_range(c+d) for d in diag):
            continue
        diag_vals = [ grid[c+d] for d in diag ]
        if ''.join(diag_vals) in ('MMSS', 'MSSM', 'SSMM', 'SMMS'):
            total += 1

ans(total)
