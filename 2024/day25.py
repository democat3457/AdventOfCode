from lib import *

year, day = 2024, 25

puzzle_input = load(year, day)
# puzzle_input = """
# """
lines = puzzle_input.strip().splitlines()
items = listsplit(lines, "")

total = 0

locks = []
keys = []

height = 0

for item in items:
    height = len(item)
    lock = all(k == '#' for k in item[0])
    grid = Grid(item[1:] if lock else item[:-1])
    (locks if lock else keys).append([ flatten(grid[:, i:i+1]).count('#') for i in range(grid.width) ])

height -= 2

for lock, key in itertools.product(locks, keys):
    for l,k in zip(lock, key):
        if l+k > height:
            break
    else:
        total += 1

ans(total)
