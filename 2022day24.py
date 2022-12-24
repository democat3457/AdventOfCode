from lib import *

year, day = 2022, 24

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# #.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#
# """.splitlines()

ls = [l for l in lines if l][1:-1]

grid_height = len(ls)
grid_width = 0

movements = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}

blizzards = []

for i in range(len(ls)):
    line = ls[i]
    if line:
        ln = line[1:-1]
        if grid_width == 0:
            grid_width = len(ln)
        for j in range(len(ln)):
            if ln[j] != '.':
                blizzards.append(((i, j), ln[j]))

starting_position = (-1, 0)
ending_position = (grid_height, grid_width-1)

search = tuple(movements.values()) + ((0,0),)

blizzard_positions = [set([b[0] for b in blizzards])]
for minute in range(1, math.lcm(grid_width, grid_height)):
    for i in range(len(blizzards)):
        blz = blizzards[i]
        newpos = tuple(map(operator.add, blz[0], movements[blz[1]]))
        newpos = newpos[0] % grid_height, newpos[1] % grid_width
        blizzards[i] = (newpos, blz[1])
    blizzard_positions.append(set([b[0] for b in blizzards]))

print('Done seeding blizzards')

minute = 0
def br():
    global blizzard_positions
    global search
    global starting_position
    global ending_position
    global grid_height
    global grid_width
    global minute
    current_pos_queue = [starting_position]
    next_pos_queue = set()
    visited_states = set()
    tq = tqdm([])
    while len(current_pos_queue):
        minute += 1
        # blizzards move
        blz_pos = blizzard_positions[minute % len(blizzard_positions)]
        for position in current_pos_queue:
            visited_states.add((position, minute % len(blizzard_positions)))
            for m in search:
                newpos = vec_add(position, m)
                if newpos == ending_position:
                    return
                if (newpos, (minute + 1) % len(blizzard_positions)) in visited_states:
                    continue
                if newpos != starting_position:
                    if newpos[0] < 0 or newpos[0] >= grid_height:
                        continue
                    if newpos[1] < 0 or newpos[1] >= grid_width:
                        continue
                if newpos in blz_pos:
                    continue
                next_pos_queue.add(newpos)
        
        del current_pos_queue
        current_pos_queue = list(next_pos_queue)
        next_pos_queue.clear()

        # print(minute)
        # if minute % 10000 == 0:
        # print(f'Minute {minute} | Queue: {len(current_pos_queue)}')

        tq.update()
        tq.set_description(f'Minute {minute} | Queue: {len(current_pos_queue)}')
br()
starting_position, ending_position = ending_position, starting_position
br()
starting_position, ending_position = ending_position, starting_position
br()

ans(minute)
