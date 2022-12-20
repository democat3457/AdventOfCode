from lib import *
import math

year, day = 2022, 20

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 1
# 2
# -3
# 3
# -2
# 0
# 4
# """.splitlines()

total = 0

orders = []

for i in range(len(lines)):
    line = lines[i]
    if line:
        orders.append((len(orders), int(line)*811589153))

print(orders)
total_length = len(orders)
for _ in range(10):
    for i in range(total_length):
        for j in range(total_length):
            if orders[j][0] == i:
                item = orders.pop(j)
                index = (j+item[1])
                orders.insert(index%(total_length-1),item)
                # print(orders)
                break
    # print(orders)
# print(orders)

zero = [i for i, order in enumerate(orders) if order[1] == 0][0]
ans(orders[(zero+1000)%total_length][1]+orders[(zero+2000)%total_length][1]+orders[(zero+3000)%total_length][1])
