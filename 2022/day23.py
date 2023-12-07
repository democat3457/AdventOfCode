from lib import *

year, day = 2022, 23

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# ....#..
# ..###.#
# #...#.#
# .#...##
# #.###..
# ##.#.##
# .#..#..
# """.splitlines()

elves = []

y_counter = 0
for line in lines:
    if line:
        for x in range(len(line)):
            if line[x] == '#':
                elves.append((x, y_counter))
        y_counter += 1

check_order = [
    ('N', (0, -1)), 
    ('S', (0, 1)), 
    ('W', (-1, 0)), 
    ('E', (1, 0)),
]

def present_around(elf):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (elf[0]+i, elf[1]+j) in elves:
                return True
    return False

def present_direction(elf, dir):
    match dir:
        case 'N':
            return (elf[0]-1, elf[1]-1) in elves or (elf[0], elf[1]-1) in elves or (elf[0]+1, elf[1]-1) in elves
        case 'S':
            return (elf[0]-1, elf[1]+1) in elves or (elf[0], elf[1]+1) in elves or (elf[0]+1, elf[1]+1) in elves
        case 'W':
            return (elf[0]-1, elf[1]-1) in elves or (elf[0]-1, elf[1]) in elves or (elf[0]-1, elf[1]+1) in elves
        case 'E':
            return (elf[0]+1, elf[1]-1) in elves or (elf[0]+1, elf[1]) in elves or (elf[0]+1, elf[1]+1) in elves
        case _:
            return False

tq = tqdm([])
tq.update()

round = 0
# print(elves)
while True:
    round += 1
    proposals = dict()
    invalid_locations = set()
    for elf in elves:
        if not present_around(elf):
            continue

        for dir, move in check_order:
            if not present_direction(elf, dir):
                proposed = tuple(map(operator.add, elf, move))
                # print(f'Proposing {proposed} for {elf} ({dir})')
                if proposed in proposals.values():
                    invalid_locations.add(proposed)
                proposals[elf] = proposed
                break

    if not len(proposals):
        break

    tq.set_description(str(len(proposals)))
    
    # print(f'Invalid: {invalid_locations}')
    
    valid_proposals = {
        k: v for k, v in proposals.items()
        if v not in invalid_locations
    }

    for elf, loc in valid_proposals.items():
        elves.remove(elf)
        elves.append(loc)
    
    check_order.append(check_order.pop(0))

    tq.update()

    # print(elves)

# width  = max(map(operator.itemgetter(0), elves))-min(map(operator.itemgetter(0), elves))+1
# height = max(map(operator.itemgetter(1), elves))-min(map(operator.itemgetter(1), elves))+1
# print(f'{width}x{height} rect')
# ans(width*height-len(elves))
ans(round)
