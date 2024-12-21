from lib import *

year, day = 2024, 21

puzzle_input = load(year, day)
# puzzle_input = """
# 029A
# 980A
# 179A
# 456A
# 379A
# """
lines = puzzle_input.strip().splitlines()

numeric = {
    '7': Coor(0,0),
    '8': Coor(0,1),
    '9': Coor(0,2),
    '4': Coor(1,0),
    '5': Coor(1,1),
    '6': Coor(1,2),
    '1': Coor(2,0),
    '2': Coor(2,1),
    '3': Coor(2,2),
    ' ': Coor(3,0),
    '0': Coor(3,1),
    'A': Coor(3,2),
}

directional = {
    ' ': Coor(0,0),
    '^': Coor(0,1),
    'A': Coor(0,2),
    '<': Coor(1,0),
    'v': Coor(1,1),
    '>': Coor(1,2),
}


def process_shortest(key_to_coor: dict[str, Coor]) -> dict[tuple[str, str], list[str]]:
    shortest = defaultdict(list)
    for a,b in itertools.product(key_to_coor.items(), repeat=2):
        if a[0] == ' ' or b[0] == ' ':
            continue
        if a[0] == b[0]:
            shortest[(a[0], b[0])].append('A')
            continue
        row = ('v' if (b[1].x - a[1].x) > 0 else '^') * abs(b[1].x - a[1].x)
        col = ('>' if (b[1].y - a[1].y) > 0 else '<') * abs(b[1].y - a[1].y)
        # first change r, then c
        if row and col:
            if not (a[1].y == key_to_coor[' '].y and b[1].x == key_to_coor[' '].x):
                shortest[(a[0], b[0])].append(row+col+'A')
            if not (a[1].x == key_to_coor[' '].x and b[1].y == key_to_coor[' '].y):
                shortest[(a[0], b[0])].append(col+row+'A')
        else:
            shortest[(a[0], b[0])].append(row+col+'A')
    return shortest

shortest_numeric = process_shortest(numeric)
shortest_directional = process_shortest(directional)

@functools.lru_cache()
def find_min_pair_length(a: str, b: str, level: int):
    return min([ find_min_dir(path, level) for path in shortest_directional[(a,b)] ])

@functools.lru_cache()
def find_min_dir(dirstr: str, level: int) -> int:
    if level == 0:
        return len(dirstr)
    total_len = 0
    for a,b in itertools.pairwise('A'+dirstr):
        min_pair_length = find_min_pair_length(a, b, level-1)
        # print(level, dirstr, a, b, min_pair_length)
        total_len += min_pair_length
    return total_len

@functools.lru_cache()
def find_min_num(numstr: str):
    total_len = 0
    for a,b in itertools.pairwise('A'+numstr):
        # robot_directionals = 2    # Part 01
        robot_directionals = 25     # Part 02

        min_pair_length = min([ find_min_dir(path, robot_directionals) for path in shortest_numeric[(a,b)] ])
        total_len += min_pair_length
    return total_len

total = 0

for line in lines:
    if line:
        num = find_min_num(line)
        # print(line, len(num), num)
        total += num * int(line.replace('A',''))

ans(total)
