from lib import *

year, day = 2022, 22

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
lines = \
"""        ...#    
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5R2
""".splitlines()

grid: List[List[str]] = []
directions: List[str|int] = []

grid_width = 0
loading_grid = True
position = (0, 0)
facings = ('r', 'd', 'l', 'u')
facing_map = {
    'u': (-1, 0),
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1),
}
facing = 'r'
for line in lines:
    if line and loading_grid:
        if grid_width == 0:
            grid_width = len(line)
            position = (0, len(line)-len(line.lstrip()))
        grid.append(list(line)+[' ']*(grid_width-len(line)))
    elif line and not loading_grid:
        dirs = re.findall(r'\d+|\w', line)
        for d in dirs:
            try:
                di = int(d)
            except:
                di = d
            finally:
                directions.append(di)
    else:
        loading_grid = False

grid = np.array(grid)

example_lookup = dict()
for y in range(0, 4):
    example_lookup[(y, 7, 'l')] = (4, y+4), 'd'
    example_lookup[(y, 12, 'r')] = (11-y, 15), 'l'
for y in range(4, 8):
    example_lookup[(y, -1, 'l')] = (11, 15-(y-4)), 'u'
    example_lookup[(y, 12, 'r')] = (8, 15-(y-4)), 'd'
for y in range(8, 12):
    example_lookup[(y, 7, 'l')] = (7, (4+(11-y))), 'u'
    example_lookup[(y, 16, 'r')] = (11-y, 11), 'l'
for x in range(0, 4):
    example_lookup[(3, x, 'u')] = (0, 11-x), 'd'
    example_lookup[(8, x, 'd')] = (11, 11-x), 'u'
for x in range(4, 8):
    example_lookup[(3, x, 'u')] = (x-4, 8), 'r'
    example_lookup[(8, x, 'd')] = (11-(x-4), 8), 'r'
for x in range(8, 12):
    example_lookup[(-1, x, 'u')] = (4, 11-x), 'd'
    example_lookup[(12, x, 'd')] = (7, 11-x), 'u'
for x in range(12, 16):
    example_lookup[(7, x, 'u')] = ((15-x)+4, 11), 'l'
    example_lookup[(12, x, 'd')] = ((15-x)+4, 0), 'r'

actual_lookup = dict()
for y in range(0, 50):
    actual_lookup[(y, 49, 'l')] = (149-y, 0), 'r'
    actual_lookup[(y, 150, 'r')] = (149-y, 99), 'l'
for y in range(50, 100):
    actual_lookup[(y, 49, 'l')] = (100, y-50), 'd'
    actual_lookup[(y, 100, 'r')] = (49, y+50), 'u'
for y in range(100, 150):
    actual_lookup[(y, -1, 'l')] = (149-y, 50), 'r'
    actual_lookup[(y, 100, 'r')] = (149-y, 149), 'l'
for y in range(150, 200):
    actual_lookup[(y, -1, 'l')] = (0, y-100), 'd'
    actual_lookup[(y, 50, 'r')] = (149, y-100), 'u'
for x in range(0, 50):
    actual_lookup[(99, x, 'u')] = (x+50, 50), 'r'
    actual_lookup[(200, x, 'd')] = (0, x+100), 'd'
for x in range(50, 100):
    actual_lookup[(-1, x, 'u')] = (x+100, 0), 'r'
    actual_lookup[(150, x, 'd')] = (x+100, 49), 'l'
for x in range(100, 150):
    actual_lookup[(-1, x, 'u')] = (199, x-100), 'u'
    actual_lookup[(50, x, 'd')] = (x-50, 99), 'l'

grid_height = len(grid)
# print('\n'.join([''.join(g) for g in grid]))
print(f'Starting position: {position}')

for dir in tqdm(directions):
    if isinstance(dir, str):
        if dir == 'R':
            facing = facings[(facings.index(facing)+1) % len(facings)]
        elif dir == 'L':
            facing = facings[(facings.index(facing)-1) % len(facings)]
        with open('log.txt', 'a') as f:
            f.write(f'Facing is now {facing}\n')
        continue

    new_facing = facing
    for _ in range(dir):
        facing = new_facing
        query = tuple(map(operator.add, position, facing_map[facing]))
        with open('log.txt', 'a') as f:
            f.write(f'q{query} nf:{new_facing}\n')
        found = False
        while not found:
            if 0 <= query[0] < grid_height and 0 <= query[1] < grid_width:
                g = grid[query[0]][query[1]]
                if g != ' ':
                    found = True
                    break
            query, new_facing = example_lookup[tuple(query)+(facing,)]
            # query, new_facing = actual_lookup[tuple(query)+(facing,)]
        if g == '#':
            break
        
        # g is .
        position = tuple(query)
        # print(position)

print(f'Final position and facing: {position} {facing}')

ans((position[0]+1)*1000 + (position[1]+1)*4 + facings.index(facing))
