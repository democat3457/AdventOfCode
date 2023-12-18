from lib import *
from lib.astar import Node
import heapq

year, day = 2023, 17

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533
# """.splitlines()
# lines = """
# 112999
# 911111
# """.splitlines()
# lines = """
# 111111111111
# 999999999991
# 999999999991
# 999999999991
# 999999999991
# """.splitlines()

h_mult = 0.05

# Part 01
# straight_min, straight_max = 0, 3
straight_min, straight_max = 4, 10

maze = truthy_list(lines)

start = Coor(0,0)
end = Coor(len(maze)-1, len(maze[0])-1)

# Create start and end node
start_node = Node(None, start)
start_node.g = start_node.h = start_node.f = 0
end_node = Node(None, end)
end_node.g = end_node.h = end_node.f = 0

# Initialize both open and closed list
open_list: list[Node[Coor]] = []
closed_list: set[tuple[tuple[int, int], tuple[int,int], float]] = set()

# Heapify the open_list and Add the start node
heapq.heapify(open_list) 
heapq.heappush(open_list, start_node)

# Adding a stop condition
print(len(maze) * len(maze[0]))

# what squares do we search
adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)

t = tqdm([])

try:
    # Loop until you find the end
    while len(open_list) > 0:
        t.update()

        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_key = (current_node.position.tup, (current_node.position - current_node.parent.position).tup if current_node.parent is not None else None, current_node.h)
        if closed_key in closed_list:
            continue
        closed_list.add(closed_key)

        # Found the goal
        if current_node == end_node and current_node.h >= h_mult * straight_min:
            break

        # Generate children
        children: list[Node] = []

        for new_position in adjacent_squares: # Adjacent squares

            # Get node position
            node_position: Coor = current_node.position + new_position

            if current_node.parent is not None and node_position == current_node.parent.position:
                continue
            previous_direction: tuple[int,int] | None = (current_node.position - current_node.parent.position).tup if current_node.parent is not None else None
            temp_node = current_node
            for straight_amnt in range(straight_max + 1):
                if temp_node.parent is None:
                    break
                if (temp_node.position - temp_node.parent.position).tup != previous_direction:
                    break
                temp_node = temp_node.parent

            if previous_direction is not None and straight_amnt < straight_min and new_position != previous_direction: # haven't gone required straight distance yet
                continue
            if previous_direction is not None and straight_amnt >= straight_max and previous_direction == new_position: # have gone maximum straight distance
                continue
            if previous_direction is not None and new_position != previous_direction: # turning, reset straight amnt
                straight_amnt = 0

            # Make sure within range
            if not (0 <= node_position.x < len(maze) and 0 <= node_position.y < len(maze[0])):
                # print('out range')
                continue

            new_h = h_mult * (straight_amnt + 1)

            if (node_position.tup, new_position, new_h) in closed_list:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            new_node.h = new_h

            # Append
            children.append(new_node)

        t.set_description(f'{current_node.f} {len(open_list)} {len(closed_list)}', refresh=False)

        # Loop through children
        for child in children:

            # Create the f, g, and h values
            child.g = current_node.g + int(maze[child.position.x][child.position.y])
            child.f = child.g + child.h

            # Add the child to the open list
            heapq.heappush(open_list, child)
except KeyboardInterrupt:
    pass

path = []
current = current_node
while current is not None:
    path.append(current.position)
    current = current.parent
print(' '.join(map(str, path[::-1])))  # Return reversed path
print('\n'.join(''.join('#' if Coor(i,j) in path else '-' for j, l in enumerate(line)) for i, line in enumerate(maze)))

new_arr = [ ['.' for j in range(len(maze[0])) ] for i in range(len(maze)) ]
# closed_list_pos = list(map(lambda x: x.position.tup, closed_list))
for c, d, h in closed_list:
    new_arr[c[0]][c[1]] = 'O'
print('\n'.join(''.join(new_arr[i][j] for j, l in enumerate(line)) for i, line in enumerate(maze)))

# print(len(closed_list_pos), len(set(closed_list_pos)))

ans(current_node.g)
