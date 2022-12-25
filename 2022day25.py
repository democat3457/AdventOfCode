from lib import *

year, day = 2022, 25

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 1=-0-2
# 12111
# 2=0=
# 21
# 2=01
# 111
# 20012
# 112
# 1=-1=
# 1-12
# 12
# 1=
# 122
# """.splitlines()

total: int = 0

for line in lines:
    if line:
        for i, char in enumerate(reversed(line)):
            if char == "=":
                val = -2
            elif char == "-":
                val = -1
            else:
                val = int(char)
            total += val * 5**i

valmap = ['=', '-', '0', '1', '2']

s = ""

while total > 0:
    nv = (total+2) % 5
    s = f"{valmap[nv]}{s}"

    total = round(total / 5)

# print(s)
ans(s)
