from lib import *

year, day = 2015, 10

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
line = truthy_list(lines)[0]

for _ in range(50): # 40 for Part 01
    groups = re.findall(r'((\d)\2*)', line)
    line = ''.join(map(lambda t: f'{len(t[0])}{t[1]}', groups))

ans(len(line))
