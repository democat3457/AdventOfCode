from lib import *

year, day = 2023, 10

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# """.splitlines()

lines = truthy_list(lines)

total = 0

s_pos = (0,0)

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == 'S':
            s_pos = (i,j)
            break
    else:
        continue
    break

chars = {
    '.': [],
    '|': [(1,0), (-1,0)],
    '-': [(0,1), (0,-1)],
    'L': [(0,1), (-1,0)],
    'J': [(0,-1), (-1,0)],
    '7': [(0,-1), (1,0)],
    'F': [(0,1), (1,0)],
    'S': [(0,1),(1,0),(0,-1),(-1,0)],
}

def proc(f: tuple[int,int] | None, t: tuple[int,int]):
    x,y = t
    for i,j in chars[lines[x][y]]:
        if f is not None and (x+i,y+j) == f:
            continue
        if (-i,-j) in chars[lines[x+i][y+j]]:
            return (x+i,y+j)

in_loop = [[False for _ in range(len(__))] for __ in lines]

prev_pos = s_pos
pos = proc(None, s_pos)
in_loop[s_pos[0]][s_pos[1]] = True
total_len = 1
start_edges = [(pos[0]-s_pos[0],pos[1]-s_pos[1])]

while pos != s_pos:
    old_pos = pos
    pos = proc(prev_pos, pos)
    prev_pos = old_pos
    in_loop[prev_pos[0]][prev_pos[1]] = True
    total_len += 1

start_edges.append((prev_pos[0]-s_pos[0],prev_pos[1]-s_pos[1]))
start_char = [k for k, v in chars.items() if set(v) == set(start_edges)][0]
# print(start_char)

# replace S with computed start char
start_line = lines[s_pos[0]]
lines[s_pos[0]] = start_line[:s_pos[1]] + start_char + start_line[s_pos[1]+1:]

# Part 01
# ans(total_len//2)
# quit()

# for il in in_loop:
#     print(il)

total = 0
for i, line in enumerate(lines):
    inside = False
    f = ''
    for j, c in enumerate(line):
        if not in_loop[i][j]:
            if inside:
                total += 1
        else:
            match c:
                case '|':
                    inside = not inside
                case '-':
                    pass
                case 'L' | 'F':
                    f = c
                case '7' | 'J':
                    if f+c in ('L7', 'FJ'):
                        inside = not inside
                    f = ''
                case _:
                    pass

# visualization
out_lines = copy.deepcopy(lines)
for i, line in enumerate(out_lines):
    for j, c in enumerate(line):
        if in_loop[i][j]:
            oj = out_lines[i]
            out_lines[i] = oj[:j] + 'O' + oj[j+1:]
Path('out.txt').write_text('\n'.join(out_lines))

ans(total)
