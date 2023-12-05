from lib import *

year, day = 2023, 5

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
MAX = 4300000000
# lines = """
# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4
# """.splitlines()
# MAX = 110

total = 0

seeds: list[int] = []
ssmap: list[tuple[int, int, int]] = []
sfmap: list[tuple[int, int, int]] = []
fwmap: list[tuple[int, int, int]] = []
wlmap: list[tuple[int, int, int]] = []
ltmap: list[tuple[int, int, int]] = []
thmap: list[tuple[int, int, int]] = []
hlmap: list[tuple[int, int, int]] = []
maps = [ssmap,sfmap,fwmap,wlmap,ltmap,thmap,hlmap]

state = 0

for line in lines:
    if line:
        if line.startswith("seeds: "):
            seeds = list(map(int, line.replace('seeds: ','').split()))
        elif line.startswith("seed-to-soil"):
            state = 0
        elif line.startswith("soil-to"):
            state = 1
        elif line.startswith("ferti"):
            state = 2
        elif line.startswith("water"):
            state = 3
        elif line.startswith("light"):
            state = 4
        elif line.startswith("temp"):
            state = 5
        elif line.startswith("humid"):
            state = 6
        else:
            i, j, k = map(int, line.split())
            maps[state].append((i,j,k))

# Part 01
# new_seeds = {}
# for s in seeds:
#     os = s
#     for i,m in enumerate(maps):
#         for x,y,z in m:
#             if y <= s < y+z:
#                 s = (s-y)+x
#                 break
#     # print(s)
#     new_seeds[os] = s
# ans(min(new_seeds.items(), key=operator.itemgetter(1))[1])

# Part 02
seed_ranges = list(zip(seeds[::2], seeds[1::2]))

for t in tqdm(range(MAX),total=MAX):
    os = t
    for i,m in enumerate(reversed(maps)):
        for x,y,z in m:
            if x <= t < x+z:
                t = (t-x)+y
                break
    for s,r in seed_ranges:
        if s <= t < s+r:
            ans(os)
            quit()
