from lib import *

year, day = 2025, 1

puzzle_input = load(year, day)
# puzzle_input = """
# L50
# L600
# """
lines = puzzle_input.strip().splitlines()
# [part_a], part_b = listsplit(lines, "")

total = 50
count = 0

# Part 01
# for line in lines:
#     if line:
#         total += int(line.replace("L", "-").replace("R", ""))
#         total %= 100
#         if total == 0:
#             count += 1

# Part 02
for line in lines:
    if line:
        diff = int(line.replace("L", "-").replace("R", ""))
        mag, dir = abs(diff), math.copysign(1, diff)
        for i in range(mag):
            total += dir
            total %= 100
            if total == 0:
                count += 1
        # math stuff does not work.. off by one errors everywhere
        # old_total = total
        # count += abs(total // 100)
        # if old_total > 0 and total == 0:
        #     count += 1
        # elif old_total == 0 and -100 < total < 0:
        #     count -= 1
        # total %= 100
        # print(total, count)

ans(count)
