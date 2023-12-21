from lib import *

year, day = 2023, 21

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# ...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ...........
# """.splitlines()

lines = truthy_list(lines)
grid = Grid(lines)

start = [c for c in grid if grid[c] == 'S'][0]

visited = {}
to_visit = deque([(start, 0)])
while True:
    coor, steps = to_visit.popleft()
    if coor.tup in visited:
        continue
    if steps == 65:
        break
    visited[coor.tup] = steps
    for add in ((-1,0),(1,0),(0,-1),(0,1)):
        new = coor+add
        if new in grid and grid[new] == '.':
            to_visit.append((new, steps+1))


ans(sum(1 for v in visited.values() if v % 2 == 0))
