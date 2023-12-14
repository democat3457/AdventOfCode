from lib import *

year, day = 2023, 14

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
# """.splitlines()

lines = truthy_list(lines)

# Part 01
# columns = [ [ line[i] for line in lines ] for i in range(len(lines[0])) ]

# total = 0

# for column in columns:
#     to_add = len(lines)
#     for i, c in enumerate(column):
#         if c == 'O':
#             total += to_add
#             to_add -= 1
#         elif c == '#':
#             to_add = len(lines) - i - 1

# ans(total)
# quit()

VALUE = 1000000000

lines = [ list(row) for row in lines ]

def make_state():
    return '\n'.join("".join(l) for l in lines)

height = len(lines)
width = len(lines[0])

states = [ make_state() ]

first_it = next_it = 0

for it in tqdm(range(1, VALUE+1)):
    for j in range(width):
        to_add = 0
        for i in range(height):
            if lines[i][j] == 'O':
                lines[i][j] = '.'
                lines[to_add][j] = 'O'
                to_add += 1
            elif lines[i][j] == '#':
                to_add = i+1
    for i in range(height):
        to_add = 0
        for j in range(width):
            if lines[i][j] == 'O':
                lines[i][j] = '.'
                lines[i][to_add] = 'O'
                to_add += 1
            elif lines[i][j] == '#':
                to_add = j+1
    for j in range(width):
        to_add = height-1
        for i in range(height-1, -1, -1):
            if lines[i][j] == 'O':
                lines[i][j] = '.'
                lines[to_add][j] = 'O'
                to_add -= 1
            elif lines[i][j] == '#':
                to_add = i-1
    for i in range(height):
        to_add = width-1
        for j in range(width-1, -1, -1):
            if lines[i][j] == 'O':
                lines[i][j] = '.'
                lines[i][to_add] = 'O'
                to_add -= 1
            elif lines[i][j] == '#':
                to_add = j-1

    new_state = make_state()
    if new_state in states:
        first_it, next_it = states.index(new_state), it
        break
    states.append(new_state)

# print(make_state())

left = (VALUE - first_it) % (next_it - first_it)

for it in tqdm(range(left)):
    for j in range(width):
        to_add = 0
        for i in range(height):
            if lines[i][j] == 'O':
                lines[i][j] = '.'
                lines[to_add][j] = 'O'
                to_add += 1
            elif lines[i][j] == '#':
                to_add = i+1
    for i in range(height):
        to_add = 0
        for j in range(width):
            if lines[i][j] == 'O':
                lines[i][j] = '.'
                lines[i][to_add] = 'O'
                to_add += 1
            elif lines[i][j] == '#':
                to_add = j+1
    for j in range(width):
        to_add = height-1
        for i in range(height-1, -1, -1):
            if lines[i][j] == 'O':
                lines[i][j] = '.'
                lines[to_add][j] = 'O'
                to_add -= 1
            elif lines[i][j] == '#':
                to_add = i-1
    for i in range(height):
        to_add = width-1
        for j in range(width-1, -1, -1):
            if lines[i][j] == 'O':
                lines[i][j] = '.'
                lines[i][to_add] = 'O'
                to_add -= 1
            elif lines[i][j] == '#':
                to_add = j-1

total = 0

for i, line in enumerate(lines):
    to_add = height-i
    total += to_add * line.count('O')

ans(total)
