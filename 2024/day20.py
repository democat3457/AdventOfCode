from lib import *

year, day = 2024, 20

puzzle_input = load(year, day)
# puzzle_input = """
# ###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############
# """
lines = puzzle_input.strip().splitlines()
# [part_a], part_b = listsplit(lines, "")

grid = Grid(lines)
[start], [end] = grid.find_all(('S', 'E'))

coors = dict()

q = [(0, start)]
visited = set()
while len(q):
    dst, c = q.pop()
    if c in visited:
        continue
    visited.add(c)
    coors[c] = dst
    if c == end:
        break
    for d in Grid.adjacent():
        if c+d in grid and grid[c+d] != '#':
            q.append((dst+1, c+d))

total = 0

# Part 01
# for c, dst in coors.items():
#     for d in Grid.adjacent():
#         nc = c + d * 2
#         if nc in coors and abs(coors[nc] - dst) >= 102:
#             total += 1
# ans(total // 2)
# quit()

# Part 02
diag = Grid.adjacent_diagonal()
for ii in Grid.adjacent():
    diag.remove(ii)

print(diag)

for c, dst in tqdm(coors.items()):
    for x in range(21):
        for y in range(21-x):
            if x == 0 and y == 0:
                continue
            cc = Coor(x,y)
            for d in set(map(lambda a: a*cc, diag)):
                nc = c+d
                traveled = abs(d.x)+abs(d.y)
                if nc in coors and abs(coors[nc] - dst) - traveled >= 100:
                    total += 1

ans(total // 2)
