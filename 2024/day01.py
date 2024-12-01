from lib import *

year, day = 2024, 1

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# """.splitlines()

total = 0

# Part 01
# a = []
# b = []

# for line in lines:
#     if line:
#         c,d = map(int, line.split())
#         a.append(c)
#         b.append(d)

# a.sort()
# b.sort()

# for i in range(len(a)):
#     total += abs(a[i] - b[i])

# ans(total)
# quit()


# Part 02
a = []
b = defaultdict(lambda:0)

for line in lines:
    if line:
        c,d = map(int, line.split())
        a.append(c)
        b[d] += 1


for i in range(len(a)):
    total += a[i] * b[a[i]]

ans(total)
