from lib import *

year, day = 2023, 8

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
# """.splitlines()

total = 0

lines = truthy_list(lines)

insts = lines[0]
lines = lines[1:]

nodes: dict[str, tuple[str, str]] = {}

for line in lines:
    if line:
        n, t = line.split(' = ')
        t1, t2 = re.findall(r'([\w\d]{3})', t)
        nodes[n] = (t1, t2)

a = [n for n in nodes.keys() if n.endswith('A')]

node = 'AAA'
it = 0
i = 0
t = tqdm()
ew = [(not n.endswith('Z')) for n in a]
cycle_count = [[] for _ in range(len(a))]
mod_cycle_count = [[] for _ in range(len(a))]
actual_cycle_count = [-1] * len(a)
start = [-1] * len(a)
while any(c == -1 for c in actual_cycle_count):
    ind = 0 if insts[i] == 'L' else 1
    a = [nodes[b][ind] for b in a]
    i = (i+1) % len(insts)
    it += 1
    ew = [(not n.endswith('Z')) for n in a]
    for j in range(len(a)):
        if actual_cycle_count[j] != -1:
            continue
        if not ew[j]:
            if i in mod_cycle_count[j]:
                cc = cycle_count[j][mod_cycle_count[j].index(i)]
                actual_cycle_count[j] = it - cc
                start[j] = it
            else:
                cycle_count[j].append(it)
                mod_cycle_count[j].append(i)
        # cycle_count[j] = k+1 if k >= 0 else 0 if not ew[j] else -1
    t.set_description(str([len(x) for x in cycle_count]) + " " + str(actual_cycle_count), refresh=False)#not all(ew))
    t.update()

print(actual_cycle_count)
print(start)

lcm = math.lcm(*actual_cycle_count)

ans(lcm)
