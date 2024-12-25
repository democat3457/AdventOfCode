from lib import *

year, day = 2024, 14

puzzle_input = load(year, day)
# puzzle_input = """
# """
lines = puzzle_input.strip().splitlines()
# [part_a], part_b = listsplit(lines, "")

GRID_WIDTH = 101
GRID_HEIGHT = 103

GRID_CENTER = Coor(GRID_WIDTH // 2, GRID_HEIGHT // 2)

@dataclass
class Robot:
    pos: Coor
    vel: Coor

robots: list[Robot] = []

for line in lines:
    if line:
        px, py, vx, vy = map(int, re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups())
        robots.append(Robot(Coor(px, py), Coor(vx, vy)))

# Part 01
# for _ in range(100):
#     for robot in robots:
#         robot.pos += robot.vel
#         robot.pos = Coor(robot.pos.x % GRID_WIDTH, robot.pos.y % GRID_HEIGHT)

# quadrants = [0, 0, 0, 0]

# for robot in robots:
#     diff = robot.pos - GRID_CENTER
#     if diff.x == 0 or diff.y == 0:
#         continue
#     pos = [int(diff.x > 0), int(diff.y > 0)]
#     idx = pos[0] * 2 + pos[1]
#     quadrants[idx] += 1

# print(quadrants)
# ans(functools.reduce(operator.mul, quadrants, 1))
# quit()

# Part 02
def check_for_tree():
    grid = Grid.filled(GRID_WIDTH, GRID_HEIGHT, '.')
    for robot in robots:
        grid[robot.pos.y, robot.pos.x] = '#'
    for row in range(grid.height):
        if any(key == '#' and len(list(grp)) >= 10 for key,grp in itertools.groupby(grid[row:row+1, :][0])):
            return grid
    return None

for i in tqdm(range(101*103)):
    vertical = [False] * GRID_HEIGHT
    for robot in robots:
        if robot.pos.x == GRID_CENTER.x:
            vertical[robot.pos.y] = True
        robot.pos += robot.vel
        robot.pos = Coor(robot.pos.x % GRID_WIDTH, robot.pos.y % GRID_HEIGHT)
    if (g:=check_for_tree()):
        ans(i+1)
        print(g)
        break
