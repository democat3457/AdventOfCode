from lib import *

year, day = 2022, 12

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# """.splitlines()

grid = Grid(lines)
[starting], [ending] = grid.find_all(("S", "E"))
grid[starting] = "a"
grid[ending] = "z"

print(starting, ending)

def adjacent(curr: Coor, next: Coor):
    current_value = ord(grid[curr])
    if ord(grid[next]) > (current_value + 1):
        # print(f'unwalkable {ord(grid[next])} > {current_value + 1}')
        return False

    # Redirect to faster upper path
    if next == Coor(17, 68) or next == Coor(16, 87):
        return False

    return True

path = astar.astar(grid, starting, ending, adjacency_check=adjacent)
print(path)

for c in grid:
    if c == starting:
        grid[c] = "S"
    elif c == ending:
        grid[c] = "E"
    elif c in path:
        grid[c] = "O"
print(grid)
ans(len(path)-1)
