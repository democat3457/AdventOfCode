from lib import *

year, day = 2024, 2

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """.splitlines()

# Part 01
# total = 0

# for line in lines:
#     if line:
#         nums = map(int, line.split())
#         dir = 100
#         valid = True
#         for n1, n2 in itertools.pairwise(nums):
#             if dir == 100:
#                 dir = math.copysign(1, n2 - n1)
#             diff = n2 - n1
#             if math.copysign(1, diff) != dir:
#                 valid = False
#                 break
#             if 1 <= abs(diff) <= 3:
#                 continue
#             valid = False
#             break
#         if valid:
#             total += 1

# ans(total)
# quit()

# Part 02
total = 0

for line in lines:
    if line:
        nums = list(map(int, line.split()))
        valid = True
        for i in range(-1, len(nums)): # brute force since there arent many numbers anyway
            nnums = nums.copy()
            if i != -1:
                nnums.pop(i)
            dir = 100
            valid = True
            for n1, n2 in itertools.pairwise(nnums):
                if dir == 100:
                    dir = math.copysign(1, n2 - n1)
                diff = n2 - n1
                if math.copysign(1, diff) != dir:
                    valid = False
                    break
                if 1 <= abs(diff) <= 3:
                    continue
                valid = False
                break
            if valid:
                break
        if valid: total += 1

ans(total)
