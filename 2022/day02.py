from lib import *

year, day = 2022, 2

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()

total = 0

for line in lines:
    if line:
        a, b = line.split()
        if b == "X":
            total += 0
            if a == "A":
                total += 3
            elif a == "B":
                total += 1
            elif a == "C":
                total += 2
        elif b == "Y":
            total += 3
            if a == "A":
                total += 1
            elif a == "B":
                total += 2
            elif a == "C":
                total += 3
        elif b == "Z":
            total += 6
            if a == "A":
                total += 2
            elif a == "B":
                total += 3
            elif a == "C":
                total += 1

ans(total)
