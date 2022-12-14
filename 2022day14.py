from lib import *

year, day = 2022, 14

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
# """.splitlines()

depth = 0

rocks = set()

for line in lines:
    if line:
        pts = line.split(" -> ")
        for pt1, pt2 in zip(pts[:], pts[1:]):
            p1 = tuple(map(int, pt1.split(",")))
            p2 = tuple(map(int, pt2.split(",")))
            depth = max((depth, p1[1], p2[1]))
            if p1[0] == p2[0]:
                for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
                    rocks.add((p1[0], y))
            elif p1[1] == p2[1]:
                for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
                    rocks.add((x, p1[1]))

depth += 2
print(f"Depth: {depth}")

for x in range(500-depth-5, 500+depth+5):
    rocks.add((x, depth))

occupied = rocks.copy()

sand = 0
filled = False
while not filled:
    sand += 1
    pos = (500,0)
    at_rest = False
    while not at_rest:
        if (pos[0], pos[1]+1) not in occupied:
            pos = (pos[0], pos[1]+1)
        elif (pos[0]-1, pos[1]+1) not in occupied:
            pos = (pos[0]-1, pos[1]+1)
        elif (pos[0]+1, pos[1]+1) not in occupied:
            pos = (pos[0]+1, pos[1]+1)
        else:
            at_rest = True
    occupied.add(pos)
    if pos == (500,0):
        filled = True

ans(sand)
