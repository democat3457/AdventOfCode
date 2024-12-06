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

def right_rotate(c):
    return Coor(c.y, -c.x)

for c in grid:
    if grid[c] == '^':
        start_guard_pos = c
        break

# Part 01
# total = 0
# visited = set()
# guard_pos = start_guard_pos
# rot = Coor(-1, 0)
# while guard_pos in grid:
#     # print(guard_pos)
#     visited.add(guard_pos.tup)
#     while (guard_pos + rot) in grid and grid[guard_pos + rot] == "#":
#         rot = right_rotate(rot)
#     guard_pos = guard_pos + rot
# ans(len(visited))
# quit()

# Part 02 Smart? no worky
# possible = set()
# visited = set()
# visited_rots = defaultdict(set)
# guard_pos = start_guard_pos
# rot = Coor(-1, 0)
# while guard_pos in grid:
#     # print(guard_pos)
#     if guard_pos.tup in visited_rots:
#         # print(f"intersect at {guard_pos}; cur rot {rot}; visited {visited[guard_pos.tup]}")
#         if right_rotate(rot).tup in visited_rots[guard_pos.tup]:
#             if (guard_pos + rot).tup not in visited:
#                 possible.add((guard_pos + rot).tup)
#     visited.add(guard_pos.tup)
#     visited_rots[guard_pos.tup].add(rot.tup)
#     temp_pos = guard_pos
#     while (temp_pos - rot) in grid and grid[temp_pos - rot] != '#':
#         temp_pos = temp_pos - rot
#         if rot.tup in visited_rots[temp_pos.tup]:
#             break
#         visited_rots[temp_pos.tup].add(rot.tup)
#     turned = False
#     while (guard_pos + rot) in grid and grid[guard_pos + rot] == '#':
#         rot = right_rotate(rot)
#         if turned: print("hi") # never runs, so there is no corner case
#         turned = True
#     guard_pos = guard_pos + rot
# ans(len(possible))
# quit()

# Part 02 Bruteforce
total = 0
for c in tqdm(grid, total=grid.width * grid.height):
    if grid[c] == '.':
        guard_pos = start_guard_pos
        funny_grid = grid.copy()
        funny_grid[c] = '#'
        visited = set()
        rot = Coor(-1, 0)
        while guard_pos in funny_grid:
            # print(guard_pos)
            if (guard_pos.tup, rot.tup) in visited:
                total += 1
                break
            visited.add((guard_pos.tup, rot.tup))
            while (guard_pos + rot) in funny_grid and funny_grid[guard_pos + rot] == "#":
                rot = right_rotate(rot)
            guard_pos = guard_pos + rot
ans(total)
