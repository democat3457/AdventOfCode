from lib import *

year, day = 2024, 19

puzzle_input = load(year, day)
# puzzle_input = """
# r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb
# """
patts, designs = puzzle_input.strip().split('\n\n')

patts = patts.strip().split(', ')

@functools.lru_cache()
def proc(design: str):
    if not len(design):
        return 1
    valid = 0
    for p in patts:
        if design.startswith(p):
            valid += proc(design.removeprefix(p))
    return valid

total = 0

for line in tqdm(designs.splitlines()):
    if line:
        # Part 01
        # if proc(line):
        #     total += 1
        # continue

        # Part 02
        total += proc(line)

ans(total)
