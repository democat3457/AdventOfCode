from lib import *

year, day = 2023, 13

puzzle_input = load(year, day)
inp = puzzle_input
# inp = """
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
# """

def proc_lines(lines: list[str], avoid: int = -1):
    enumerated_lines = list(enumerate(lines))

    columns = [ ''.join(n[i] for n in lines) for i in range(len(lines[0])) ]
    enumerated_columns = list(enumerate(columns))

    total = -1

    for (i1, l1), (i2, l2) in zip(enumerated_lines, enumerated_lines[1:]):
        if l1 == l2:
            # print('e', i1, i2)
            # print(lines[i1-1:-1:-1])
            for j1, j2 in zip(reversed(lines[:i1]), lines[i2+1:]):
                # print('comp', j1, j2)
                if j1 != j2:
                    break
            else:
                subtotal = 100 * (i1+1) # == i2
                if subtotal != avoid:
                    total = subtotal
                    break
    else:
        # check columns
        for (i1, l1), (i2, l2) in zip(enumerated_columns, enumerated_columns[1:]):
            if l1 == l2:
                # print('c', i1, i2)
                for j1, j2 in zip(reversed(columns[:i1]), columns[i2+1:]):
                    # print('cccomp', j1, j2)
                    if j1 != j2:
                        break
                else:
                    subtotal = i1+1 # == i2
                    if subtotal != avoid:
                        total = subtotal
                        break
    
    return total

def proc_case(lines: list[str]):
    old_grid_total = proc_lines(lines)

    # Part 01
    # return old_grid_total

    new_lines = [ list(s) for s in lines ]
    for i in range(len(lines)):
        old_row = [ n for n in new_lines[i] ]
        for j in range(len(old_row)):
            old_char = old_row[j]
            new_lines[i][j] = '#' if old_char == '.' else '.'
            new_grid_total = proc_lines(new_lines, avoid=old_grid_total)
            if new_grid_total >= 0:
                return new_grid_total
            new_lines[i][j] = old_char
    
    return 0
    

total = 0

for lines in inp.split('\n\n'):
    lines = lines.splitlines()
    lines = truthy_list(lines)
    if not len(lines):
        continue

    grid_total = proc_case(lines)

    total += grid_total

ans(total)
