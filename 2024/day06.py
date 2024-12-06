from lib import *

year, day = 2024, 6

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """.splitlines()

grid = Grid(lines)

total = 0

visited = set()
for c in grid:
    if grid[c] == '^':
        guard_pos = c
        break
rot = Coor(-1, 0)
while guard_pos in grid:
    # print(guard_pos)
    visited.add(guard_pos.tup)
    while (guard_pos + rot) in grid and grid[guard_pos + rot] == '#':
        rot = Coor(rot.y, -rot.x)
    guard_pos = guard_pos + rot

ans(len(visited))
