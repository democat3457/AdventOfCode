from lib import *

year, day = 2024, 3

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# mul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()mul(8,6))don't()don't()mul(6,6)do()mul(1,1)mul(2,0)do()
# """.splitlines()

total = 0

# Part 01
# for line in lines:
#     if line:
#         ls = re.findall(r"mul\((\d+),(\d+)\)", line)
#         for l in ls:
#             total += int(l[0]) * int(l[1])

# Part 02
enabled = True
for line in lines:
    if line:
        while line:
            if line.startswith('do()'):
                enabled = True
                line = line.replace('do()', '', 1)
            elif line.startswith("don't()"):
                enabled = False
                line = line.replace("don't()",'',1)
            elif enabled and (m:=re.match(r'^mul\((\d+),(\d+)\)', line)):
                total += int(m.group(1)) * int(m.group(2))
                print(m.group(0))
                line = line.replace(m.group(0), '',1)
            else:
                line = line[1:]

ans(total)
