from lib import *

year, day = 2024, 15

puzzle_input = load(year, day)
# puzzle_input = """
# ########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<
# """
# puzzle_input = """
# ##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
# """
# puzzle_input = """
# #######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^
# """
lines = puzzle_input.strip()

g, s = lines.split('\n\n')
grid = Grid(g.splitlines())
s = s.replace('\n','')

def print_grid():
    new_grid = Grid(["." * grid.width * 2 for _ in range(grid.height)])
    for o in obstacles:
        new_grid[o] = "#"
    for b in boxes:
        new_grid[b] = "O"
    new_grid[robot] = "@"
    print(str(new_grid))

offset = Coor(0,1)

dirs = {
    '^': Coor(-1,0),
    'v': Coor(1,0),
    '<': Coor(0,-1),
    '>': Coor(0,1),
}

obstacles = set()
boxes = []

# Part 01
# for c in grid:
#     if grid[c] == '@':
#         robot = c
#     elif grid[c] == '#':
#         obstacles.add(c)
#     elif grid[c] == 'O':
#         boxes.append(c)

# for ch in s:
#     d = dirs[ch]
#     i = 1
#     first_box = None
#     while robot+d*i in grid:
#         if robot+d*i in obstacles:
#             break
#         if robot+d*i in boxes:
#             if first_box is None:
#                 first_box = boxes.index(robot+d*i)
#         else:
#             if first_box is not None:
#                 boxes[first_box] = robot+d*i
#             robot = robot + d
#             break
#         i += 1


# new_grid = Grid([ '.'*grid.width for _ in range(grid.height) ])
# for o in obstacles:
#     new_grid[o] = '#'
# for b in boxes:
#     new_grid[b] = 'O'
# new_grid[robot] = '@'
# print(str(new_grid))

# ans(sum(map(lambda c: c.x*100 + c.y, boxes)))
# quit()

# Part 02
for c in grid:
    new_c = c * Coor(1,2)
    if grid[c] == '@':
        robot = new_c
    elif grid[c] == '#':
        obstacles.add(new_c)
        obstacles.add(new_c+offset)
    elif grid[c] == 'O':
        boxes.append(new_c)
        boxes.append(new_c+offset)

for i, ch in enumerate(s):
    d = dirs[ch]
    collision_boxes = set()
    q = [robot+d]
    while len(q):
        c = q.pop(0)
        if c in obstacles:
            break
        if c in boxes:
            idx = boxes.index(c)
            collision_boxes.add(idx)
            if idx % 2 == 0:
                collision_boxes.add(idx+1)
                other_c = boxes[idx+1]
            else:
                collision_boxes.add(idx-1)
                other_c = boxes[idx-1]
            if d.y != 0: # left-right
                q.append(c + d*2)
            else: # up-down
                for oc in (c, other_c):
                    q.append(oc + d)
    else:
        for idx in collision_boxes:
            boxes[idx] = boxes[idx] + d
        robot = robot + d

    # if i < 50:
    #     print(ch)
    #     print_grid()

ans(sum(map(lambda c: c.x*100 + c.y, boxes[::2])))
