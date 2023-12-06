from lib import *

year, day = 2023, 6

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# """.splitlines()

total = 1

times = []
distances = []

for line in lines:
    if line:
        if line.startswith('Time'):
            # Part 01
            # times = list(map(int, line.replace('Time:','').split()))
            times = list(map(int, line.replace('Time:','').replace(' ','').split()))
        elif line.startswith('Distance'):
            # Part 01
            # distances = list(map(int, line.replace('Distance:','').split()))
            distances = list(map(int, line.replace('Distance:','').replace(' ','').split()))

for t, d in zip(times, distances):
    ways = 0
    for i in range(1, t):
        val = i * (t-i)
        if val > d:
            ways += 1

    total *= ways

ans(total)
