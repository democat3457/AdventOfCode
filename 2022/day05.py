from lib import *
import re

year, day = 2022, 5

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()

loading = True
width = 9
boxes = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
}

for line in lines:
    if not line:
        loading = False
        continue
    
    if loading:
        for match in re.finditer("\[(.)\]", line):
            boxes[(match.start() // 4) + 1].append(match.group(1))
    else:
        nums: re.Match[str] = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        src = int(nums.group(2))
        dst = int(nums.group(3))
        for i in reversed(range(int(nums.group(1)))):
            boxes[dst].insert(0, boxes[src].pop(i))

s = ""

for l in boxes.values():
    s += l[0]

ans(s)
