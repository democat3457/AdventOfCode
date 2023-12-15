from lib import *

year, day = 2023, 15

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# """.splitlines()

total = 0

lines = truthy_list(lines)
line = lines[0]

lenses = [ [] for _ in range(256) ]
focal_lengths = [ [] for _ in range(256) ]

def hash(s):
    subtotal = 0
    for c in s:
        subtotal += ord(c)
        subtotal *= 17
        subtotal %= 256
    return subtotal

# Part 01
# for s in line.split(','):
#     total += hash(s)
# ans(total)
# quit()

for s in line.split(','):
    match = re.match(r'^(\w+)(-|=\d+)', s)
    if match is None:
        quit(1)
    label, op = match.groups()
    box = hash(label)
    if op.startswith('-'):
        if label in lenses[box]:
            l = lenses[box].index(label)
            lenses[box].pop(l)
            focal_lengths[box].pop(l)
    else:
        focal_length = int(op.removeprefix('='))
        if label in lenses[box]:
            l = lenses[box].index(label)
            focal_lengths[box][l] = focal_length
        else:
            lenses[box].append(label)
            focal_lengths[box].append(focal_length)

total = 0

for i, ls in enumerate(focal_lengths, start=1):
    for j, fl in enumerate(ls, start=1):
        total += i * j * fl

ans(total)
