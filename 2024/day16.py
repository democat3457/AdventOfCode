from lib import *
import heapq

year, day = 2024, 16

puzzle_input = load(year, day)
# puzzle_input = """
# ###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############
# """
lines = puzzle_input.strip().splitlines()

grid = Grid(lines)

for c in grid:
    if grid[c] == 'S':
        start = c
    elif grid[c] == 'E':
        end = c

# Part 01
# q = [(0, start, Coor(0, 1))]
# visited = set()
# heapq.heapify(q)

# while len(q):
#     score, c, prev_dir = heapq.heappop(q)
#     if c in map(operator.itemgetter(0), visited):
#         continue
#     visited.add((c, score))
#     if c == end:
#         ans(score)
#         break
#     for d in Grid.adjacent():
#         if c + d not in grid:
#             continue
#         if grid[c + d] == "#":
#             continue
#         if prev_dir is None or d == prev_dir:
#             heapq.heappush(q, (score + 1, c + d, d))
#         else:
#             heapq.heappush(q, (score + 1001, c + d, d))
# quit()

# Part 02
q = [(0, start, Coor(0, 1), set())]
heapq.heapify(q)

min_score = None
total_visited = set()
global_visited = dict()

while len(q):
    score, c, prev_dir, visited = heapq.heappop(q)
    if c in visited:
        continue
    if (c, prev_dir) in global_visited:
        if global_visited[(c, prev_dir)] < score:
            continue
    visited.add(c)
    global_visited[(c, prev_dir)] = score
    if c == end:
        if min_score is None or score == min_score:
            min_score = score
            total_visited = total_visited.union(visited)
        else:
            break
    for d in Grid.adjacent():
        if c+d not in grid:
            continue
        if grid[c+d] == '#':
            continue
        if prev_dir is None or d == prev_dir:
            new_coor = (score + 1, c + d, d, visited.copy())
        elif prev_dir != -d:
            new_coor = (score + 1001, c + d, d, visited.copy())
        if not len(q):
            heapq.heappush(q, new_coor)
            continue
        head = q[0]
        if new_coor[0] == head[0] and new_coor[1] == head[1] and new_coor[2] == head[2]:
            for v in new_coor[3]:
                head[3].add(v)
        else:
            heapq.heappush(q, new_coor)

for v in total_visited:
    grid[v] = 'O'

print(grid)

ans(len(total_visited))
