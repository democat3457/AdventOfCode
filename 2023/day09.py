from lib import *

year, day = 2023, 9

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45
# """.splitlines()

def extrapolate(seq: list[int]):
    if not any(seq):
        return 0
    nl = [j-i for i, j in zip(seq, seq[1:])]
    # Part 01
    # return seq[-1] + extrapolate(nl)
    return seq[0] - extrapolate(nl)


total = 0

for line in lines:
    if line:
        ints = list(map(int, line.split()))
        total += extrapolate(ints)

ans(total)
