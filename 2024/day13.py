from lib import *

year, day = 2024, 13

puzzle_input = load(year, day)
# puzzle_input = """
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
# """
cases = puzzle_input.strip().split('\n\n')

total = 0

for case in cases:
    button_a, button_b, goal = case.splitlines()
    a = re.match(r"Button A: X\+(\d+), Y\+(\d+)", button_a)
    coor_a = Coor(int(a.group(1)), int(a.group(2)))
    b = re.match(r"Button B: X\+(\d+), Y\+(\d+)", button_b)
    coor_b = Coor(int(b.group(1)), int(b.group(2)))
    prize = re.match(r"Prize: X=(\d+), Y=(\d+)", goal)
    coor_goal = Coor(int(prize.group(1)), int(prize.group(2)))
    for i in reversed(range(101)):
        b_total = coor_b * i
        if b_total.x > coor_goal.x or b_total.y > coor_goal.y:
            continue
        if b_total == coor_goal:
            total += i
            break
        left = coor_goal - b_total
        if left.x % coor_a.x == 0 and left.y % coor_a.y == 0 and left.x // coor_a.x == left.y // coor_a.y:
            total += i + 3 * (left.x // coor_a.x) 

ans(total)
