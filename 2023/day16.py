from lib import *
from itertools import chain, repeat

year, day = 2023, 16

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# .|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|....
# """.splitlines()

# print(lines)

lines = truthy_list(lines)

# print(list(map(len, lines)))

def get_coor(coor: Coor):
    return lines[coor.x][coor.y] if 0 <= coor.x < len(lines) and 0 <= coor.y < len(lines[0]) else None

def get_dir(dir):
    match dir:
        case 'r':
            return (0,1)
        case 'd':
            return (1,0)
        case 'l':
            return (0,-1)
        case 'u':
            return (-1,0)
        case _:
            raise NotImplementedError(dir)

mx = 0

# Part 01
# for start_x, start_y, direction in ((0,0,'r'),):
for start_x, start_y, direction in tqdm(chain(
    zip(range(len(lines)), repeat(0), repeat('r')),
    zip(repeat(0), range(len(lines[0])), repeat('d')),
    zip(range(len(lines)), repeat(len(lines[0])-1), repeat('l')),
    zip(repeat(len(lines)-1), range(len(lines[0])), repeat('u'))
), total=2*(len(lines) + len(lines[0]))):
    visited = []
    to_visit = [(Coor(start_x, start_y), direction)]
    while len(to_visit):
        c, d = to_visit.pop(0)
        if (c.tup,d) in visited:
            continue
        char = get_coor(c)
        if char is not None:
            visited.append((c.tup,d))
            match char:
                case '.':
                    to_visit.append((c + get_dir(d), d))
                case '|':
                    if d != 'd':
                        to_visit.append((c + get_dir('u'), 'u'))
                    if d != 'u':
                        to_visit.append((c + get_dir('d'), 'd'))
                case '-':
                    if d != 'l':
                        to_visit.append((c + get_dir('r'), 'r'))
                    if d != 'r':
                        to_visit.append((c + get_dir('l'), 'l'))
                case '/':
                    match d:
                        case 'u':
                            to_visit.append((c + get_dir('r'), 'r'))
                        case 'r':
                            to_visit.append((c + get_dir('u'), 'u'))
                        case 'd':
                            to_visit.append((c + get_dir('l'), 'l'))
                        case 'l':
                            to_visit.append((c + get_dir('d'), 'd'))
                case '\\':
                    match d:
                        case 'u':
                            to_visit.append((c + get_dir('l'), 'l'))
                        case 'r':
                            to_visit.append((c + get_dir('d'), 'd'))
                        case 'd':
                            to_visit.append((c + get_dir('r'), 'r'))
                        case 'l':
                            to_visit.append((c + get_dir('u'), 'u'))
            # print(to_visit)
    
    mx = max(mx, len(set(map(lambda x:x[0], visited))))

# print(visited)
ans(mx)
