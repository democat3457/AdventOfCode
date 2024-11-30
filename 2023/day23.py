from __future__ import annotations
from typing import Generic

from lib import *
import heapq

T = TypeVar('T')

class Node(Generic[T]):
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent: Node[T]|None=None, position: T=None):
        if parent is None:
            self.parents: list[Node[T]] = []
        else:
            self.parents = parent.parents + [parent]
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    @property
    def parent(self):
        return self.parents[-1] if len(self.parents) else None

    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f

year, day = 2023, 23

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# #.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#
# """.splitlines()

grid = Grid(truthy_list(lines))

# what squares do we search
adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)

start = Coor(0, [j for j in range(grid.width) if grid[0,j] == '.'][0])
end = Coor(grid.height-1, [j for j in range(grid.width) if grid[grid.height-1,j] == '.'][0])

intersection_adjs: dict[tuple[int,int], list[Coor]] = {}

for c in grid:
    if grid[c] != '#' and c != start and c != end:
        adj = [c+a for a in adjacent_squares if grid[c+a] != '#']
        if len(adj) > 2:
            intersection_adjs[c.tup] = adj

def find_edge(intersection: Coor, adj: Coor) -> tuple[int, tuple[Coor,Coor]|tuple[None,None]]:
    node = adj, intersection-adj
    found = [intersection]
    while True:
        if node[0].tup in intersection_adjs:
            return len(found) - 1, node
        if node[0] == start:
            return len(found) - 1, node
        if node[0] == end:
            return len(found) - 1, node
        found.append(node[0])
        new_adj = [(node[0]+a) for a in adjacent_squares if (node[0]+a) not in found and grid[node[0]+a] != '#']
        if len(new_adj) == 1:
            node = new_adj[0], node[0] - new_adj[0]
        elif len(new_adj) == 0:
            return -1, (None, None)
        else:
            raise RuntimeError

edges: dict[tuple[int,int], list[tuple[tuple[int,int], int]]] = defaultdict(list)

found_adjs: dict[tuple[int,int], list[Coor]] = defaultdict(list)

for i, adjs in intersection_adjs.items():
    for adj in adjs:
        if adj in found_adjs[i]:
            continue
        length, (j, from_dir) = find_edge(Coor(i[0],i[1]), adj)
        found_adjs[i].append(adj)
        if j is None or from_dir is None:
            continue
        j = j.tup
        found_adjs[j].append(from_dir)
        edges[i].append((j, length))
        edges[j].append((i, length))

start_node = Node(None, start)
start_node.g = start_node.h = start_node.f = 0
end_node = Node(None, end)
end_node.g = end_node.h = end_node.f = 0

# Initialize both open and closed list
open_list: deque[Node[Coor]] = deque([ start_node ])

# Heapify the open_list and Add the start node
# heapq.heapify(open_list) 
# heapq.heappush(open_list, start_node)

max_length = 0

# print(intersection_adjs)
print(len(edges))

t = tqdm()

# Loop until you find the end
while len(open_list) > 0:

    t.update()
    t.set_description(f'{len(open_list)} {max_length}', refresh=False)
    
    # Get the current node
    current_node = open_list.popleft()
    # closed_list.append(current_node)

    # Found the goal
    if current_node == end_node:
        max_length = max(max_length, current_node.g)
        continue

    # Generate children
    children: list[Node] = []
    
    for adj_inter, weight in edges[current_node.position.tup]: # Adjacent squares

        # if new_position == (0,1) and grid[node_position] == '<':
        #     continue
        # if new_position == (0,-1) and grid[node_position] == '>':
        #     continue
        # if new_position == (1,0) and grid[node_position] == '^':
        #     continue
        # if new_position == (-1,0) and grid[node_position] == 'v':
        #     continue

        # Create new node
        child = Node(current_node, Coor(adj_inter[0], adj_inter[1]))

        if child in current_node.parents:
            continue

        # Create the f, g, and h values
        child.g = current_node.g + weight + 1
        # dist_to_start = child.position - start_node.position
        # child.h = ((dist_to_start.x ** 2) + (dist_to_start.y ** 2))
        # child.h = 0
        child.f = child.g

        # Add the child to the open list
        open_list.append(child)

ans(max_length)
