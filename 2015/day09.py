from lib import *

year, day = 2015, 9

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# """.splitlines()

edge_list: dict[set[str], int] = {}

for line in lines:
    if line:
        c1, c2, d = re.match(r'(.+) to (.+) = (\d+)', line).groups()
        d = int(d)
        edge_list[frozenset({c1, c2})] = d

cities_list: set[str] = functools.reduce(lambda x,y: x.union(y), edge_list.keys(), set())

min_route = math.inf
max_route = 0
for permutation in itertools.permutations(cities_list, len(cities_list)):
    total = 0
    for i, j in itertools.pairwise(permutation):
        total += edge_list[frozenset({i,j})]
    min_route = min(min_route, total)
    max_route = max(max_route, total)

# Part 01
# ans(min_route)
# Part 02
ans(max_route)
