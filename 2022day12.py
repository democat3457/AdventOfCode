from lib import *
import astar

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

grid = []
starting = (0,0)
ending = (0,0)

for line in lines:
    if line:
        if "S" in line:
            starting = (len(grid), line.index("S"))
            line = line.replace("S", "a")
        if "E" in line:
            ending = (len(grid), line.index("E"))
            line = line.replace("E", "z")
        grid.append(list(line))

print(starting, ending)

path = astar.astar(grid, starting, ending, False)
print(path)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) == starting:
            grid[i][j] = "S"
        elif (i,j) == ending:
            grid[i][j] = "E"
        elif (i,j) in path:
            grid[i][j] = "O"
print('\n'.join(map(lambda x: ''.join(x), grid)))
ans(len(path)-1)
