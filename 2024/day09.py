from lib import *

year, day = 2024, 9

puzzle_input = load(year, day)
# puzzle_input = "2333133121414131402"
line = intlist(puzzle_input.strip())

# Part 01
# files = line[::2]
# holes = line[1::2]

# total = 0

# ids = list(enumerate(files)) # id, amnt
# i = 0
# hole = False
# s = ""
# while i < sum(files):
#     if not hole:
#         id, amt = ids.pop(0)
#         # print(i, "not hole", total, id, amt)
#         total += id * (i * amt + (amt * (amt - 1)) // 2)
#         # s += str(id) * amt
#         hole = True
#         i += amt
#     else:
#         next_hole_size = holes.pop(0)
#         while next_hole_size > 0:
#             # print(i, "    hole", total, next_hole_size, len(holes))
#             if ids[-1][1] > next_hole_size:
#                 ids[-1] = (ids[-1][0], ids[-1][1] - next_hole_size)
#                 total += ids[-1][0] * (i * next_hole_size + (next_hole_size * (next_hole_size - 1)) // 2)
#                 # s += str(ids[-1][0]) * next_hole_size
#                 i += next_hole_size
#                 next_hole_size = 0
#             else:
#                 id, amt = ids.pop()
#                 total += id * (i * amt + (amt * (amt - 1)) // 2)
#                 # s += str(id) * amt
#                 i += amt
#                 next_hole_size -= amt
#         hole = False

# # print(s)
# ans(total)
# quit()

# Part 02
blocks = []
spaces = []

id = 0
pos = 0
for i, val in enumerate(line):
    if i % 2 == 0:
        blocks.append((id, pos, val))  # id, pos, amt
        id += 1
    else:
        spaces.append((pos, val))  # pos, amt
    pos += val

for i in range(len(blocks) - 1, -1, -1):
    id, pos, amt = blocks[i]
    for j in range(i):
        if spaces[j][1] >= amt:
            blocks[i] = (id, spaces[j][0], amt)
            spaces[j] = (spaces[j][0] + amt, spaces[j][1] - amt)
            break

total = 0

for id, pos, amt in blocks:
    total += id * (pos * amt + (amt * (amt - 1)) // 2)

ans(total)
