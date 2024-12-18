from __future__ import annotations
from lib import *
import heapq

year, day = 2024, 18

puzzle_input = load(year, day)
# puzzle_input = """
# 5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0
# """
lines = puzzle_input.strip().splitlines()

# SIZE = 6
SIZE = 70

grid = Grid([ '.'*(SIZE+1) for _ in range(SIZE+1) ])

# Part 01
# obstacles = []
# for i in range(1024):
#     a,b = map(int, lines[i].split(','))
#     obstacles.append(Coor(b,a))
#     grid[b,a] = '#'

# start = Coor(0,0)
# end = Coor(SIZE, SIZE)

# q = [(0, start)]
# visited = set()
# heapq.heapify(q)
# while len(q):
#     i, c = heapq.heappop(q)
#     if c in visited:
#         continue
#     visited.add(c)
#     if c == end:
#         ans(i)
#         break
#     for d in Grid.adjacent():
#         if c+d in grid:
#             if grid[c+d] == '#':
#                 continue
#             heapq.heappush(q, (i+1, c+d))
# quit()

# Part 02
obstacles = []
nodes: dict[Coor, Node] = dict()

class Node:
    def __init__(self, c: Coor, root: Node | None, tr: bool = False, bl: bool = False):
        self.coor = c
        self.root = root
        self.touching_topright = tr
        self.touching_botleft = bl
        self.followers = set()
    
    def __str__(self):
        return f'{self.coor}: root {self.root.coor if self.root else True}: tr/bl {self.touching_topright}/{self.touching_botleft}'

def get_root(node: Node):
    if node is None:
        return node
    while node.root is not None:
        node = node.root
    return node

def touching_topright(c: Coor):
    return c.x == 0 or c.y == SIZE
def touching_botleft(c: Coor):
    return c.x == SIZE or c.y == 0

for i in range(len(lines)):
    a,b = map(int, lines[i].split(','))
    c = Coor(b,a)
    obstacles.append(Coor(b,a))
    roots: set[Coor] = set()
    for d in Grid.adjacent_diagonal():
        if c+d in obstacles:
            roots.add(get_root(nodes[c+d]).coor)
    if not len(roots):
        nodes[c] = Node(c, None, touching_topright(c), touching_botleft(c))
        continue
    elif len(roots) == 1:
        root = nodes[next(iter(roots))]
    else:
        root = nodes[next(iter(roots))]
        for other_root in roots:
            if other_root == root.coor:
                continue
            ort = nodes[other_root]
            ort.root = root
            root.followers = root.followers.union(ort.followers)
            root.touching_botleft |= ort.touching_botleft
            root.touching_topright |= ort.touching_topright
    nodes[c] = Node(c, root)
    root.followers.add(c)
    root.touching_topright |= touching_topright(c)
    root.touching_botleft |= touching_botleft(c)
    if root.touching_botleft and root.touching_topright:
        ans(f"{a},{b}")
        break

# print(list(map(str, nodes.values())))
