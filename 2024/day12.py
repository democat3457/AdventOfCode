from lib import *

year, day = 2024, 12

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
# """.splitlines()

grid = Grid(lines)

adj = [Coor(0,1), Coor(0,-1), Coor(1,0), Coor(-1,0)]
corners = [
    (Coor(0,1),Coor(1,1),Coor(1,0)),
    (Coor(0,-1),Coor(1,-1),Coor(1,0)),
    (Coor(0,1),Coor(-1,1),Coor(-1,0)),
    (Coor(0,-1),Coor(-1,-1),Coor(-1,0)),
]

unvisited = list(grid)

total = 0

while len(unvisited):
    c = unvisited[0]
    val = grid[c]
    q = [c]
    region = []
    while len(q):
        cc = q.pop(0)
        if cc in region or cc not in unvisited:
            continue
        region.append(cc)
        unvisited.remove(cc)
        for d in Grid.adjacent:
            if cc+d in grid and grid[cc+d] == val:
                q.append(cc+d)

    area = len(region)
    perimeter = 0
    for cc in region:
        cnt = 0

        # Part 01
        # for d in adj:
        #     if cc+d in region:
        #         cnt += 1
        # perimeter += 4 - cnt
        # continue
        
        # Part 02
        for corner_set in corners:
            if (
                cc + corner_set[0] not in region
                # and cc + corner_set[1] in region
                and cc + corner_set[2] not in region
            ) or (
                cc + corner_set[0] in region
                and cc + corner_set[1] not in region
                and cc + corner_set[2] in region
            ):
                cnt += 1
        perimeter += cnt

    total += area * perimeter

ans(total)
