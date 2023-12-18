from lib import *

year, day = 2023, 18

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)
# """.splitlines()

coor = Coor(0,0)

nodes: list[Coor] = []

total_nodes = 0

for line in lines:
    if line:
        op, num, hex = line.split()

        # Part 01
        # val = int(num)
        # Part 02
        hex = hex.replace('#','').replace('(','').replace(')','')
        op = hex[5]
        val = int(hex[:-1], 16)

        match op:
            case 'U' | '3':
                diff = Coor(0,-1)
            case 'D' | '1':
                diff = Coor(0,1)
            case 'L' | '2':
                diff = Coor(-1,0)
            case 'R' | '0':
                diff = Coor(1,0)
            case _:
                raise NotImplementedError
        coor += diff * val
        nodes.append(coor)
        total_nodes += val

area = 0
for i in range(len(nodes)):
    area += nodes[i].x * (nodes[(i+1)%len(nodes)].y - nodes[(i-1)%len(nodes)].y)
area //= 2

print(len(nodes))

ans(total_nodes + (area - (total_nodes//2) + 1))
