from lib import *
from lib.astar import Node
import heapq

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

start = Coor(0, [j for j in range(grid.width) if grid[0,j] == '.'][0])
end = Coor(grid.height-1, [j for j in range(grid.width) if grid[grid.height-1,j] == '.'][0])

start_node = Node(None, start)
start_node.g = start_node.h = start_node.f = 0
end_node = Node(None, end)
end_node.g = end_node.h = end_node.f = 0

# Initialize both open and closed list
open_list: list[Node] = []

# Heapify the open_list and Add the start node
heapq.heapify(open_list) 
heapq.heappush(open_list, start_node)

# what squares do we search
adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)

max_length = 0

# Loop until you find the end
while len(open_list) > 0:     
    
    # Get the current node
    current_node = heapq.heappop(open_list)
    # closed_list.append(current_node)

    # Found the goal
    if current_node == end_node:
        max_length = max(max_length, current_node.g)
        continue

    # Generate children
    children: list[Node] = []
    
    for new_position in adjacent_squares: # Adjacent squares

        # Get node position
        node_position = current_node.position + new_position

        # Make sure within range
        if node_position not in grid:
            # print('out range')
            continue

        if grid[node_position] == '#':
            continue

        if new_position == (0,1) and grid[node_position] == '<':
            continue
        if new_position == (0,-1) and grid[node_position] == '>':
            continue
        if new_position == (1,0) and grid[node_position] == '^':
            continue
        if new_position == (-1,0) and grid[node_position] == 'v':
            continue

        if current_node.parent is not None and node_position == current_node.parent.position:
            continue

        # Make sure walkable terrain
        # if ord(maze[node_position[0]][node_position[1]]) > (current_value + 1):
        #     # print(f'unwalkable {ord(maze[node_position[0]][node_position[1]])} > {current_value + 1}')
        #     continue

        # if node_position == (17, 68) or node_position == (16, 87):
        #     continue

        # Create new node
        new_node = Node(current_node, node_position)

        # Append
        children.append(new_node)

    # Loop through children
    for child in children:

        # Create the f, g, and h values
        child.g = current_node.g + 1
        dist_to_start = child.position - start_node.position
        child.h = ((dist_to_start.x ** 2) + (dist_to_start.y ** 2))
        # child.h = 0
        child.f = child.g + child.h

        # Add the child to the open list
        heapq.heappush(open_list, child)

ans(max_length)
