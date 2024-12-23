from lib import *

year, day = 2024, 23

puzzle_input = load(year, day)
# puzzle_input = """
# kh-tc
# qp-kh
# de-cg
# ka-co
# yn-aq
# qp-ub
# cg-tb
# vc-aq
# tb-ka
# wh-tc
# yn-cg
# kh-ub
# ta-co
# de-co
# tc-td
# tb-wq
# wh-td
# ta-ka
# td-qp
# aq-cg
# wq-ub
# ub-vc
# de-ta
# wq-aq
# wq-vc
# wh-yn
# ka-de
# kh-ta
# co-tc
# wh-qp
# tb-vc
# td-yn
# """
lines = puzzle_input.strip().splitlines()
# [part_a], part_b = listsplit(lines, "")

adjacency: dict[str, set[str]] = defaultdict(set)

for line in lines:
    if line:
        a,b = line.split('-')
        adjacency[a].add(b)
        adjacency[b].add(a)

# Part 01
# sets = set()

# for k, v in adjacency.items():
#     if k.startswith("t"):
#         for j in v:
#             for m in adjacency[j]:
#                 if m != k and m in v:
#                     sets.add(frozenset((k, j, m)))

# print(sets)
# ans(len(sets))
# quit()

# Part 02
largest_set = set()

for k in tqdm(adjacency.keys()):
    for s in more_itertools.powerset_of_sets(adjacency[k]):
        if all(s.difference((j,)).issubset(adjacency[j]) for j in s):
            s = s.union((k,))
            if len(s) > len(largest_set):
                largest_set = s

print(largest_set)
ans(','.join(sorted(largest_set)))
