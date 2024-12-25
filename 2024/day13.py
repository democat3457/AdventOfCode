from lib import *

from scipy.linalg import lu

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
# puzzle_input = """
# Button A: X+18, Y+5
# Button B: X+3, Y+3
# Prize: X=21, Y=7
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
    coor_goal = Coor(int(prize.group(1)), int(prize.group(2))) + Coor(
        10000000000000, 10000000000000 # Part 02
        # 0,0 # Part 01
        # 10000, 10000 # testing
    )

    # Part 01
    # for i in reversed(range(101)):
    #     b_total = coor_b * i
    #     if b_total.x > coor_goal.x or b_total.y > coor_goal.y:
    #         continue
    #     if b_total == coor_goal:
    #         total += i
    #         break
    #     left = coor_goal - b_total
    #     if left.x % coor_a.x == 0 and left.y % coor_a.y == 0 and left.x // coor_a.x == left.y // coor_a.y:
    #         total += i + 3 * (left.x // coor_a.x)
    # continue

    # Part 02
    def use_lu():
        arr = np.array([
            [coor_a.x, coor_b.x, coor_goal.x],
            [coor_a.y, coor_b.y, coor_goal.y]
        ])
        _, u = lu(arr, permute_l=True)
        if u[0][0] == u[0][1] == 0 and u[0][2] != 0:
            return (0,0),0
        if u[1][0] == u[1][1] == 0 and u[1][2] != 0:
            return (0,0),0
        if np.all(np.abs(u[1]) < 0.001):
            if (coor_goal.x / coor_b.x) < (coor_goal.x / coor_a.x * 3):
                remaining = coor_goal.x % coor_b.x
                return (remaining // coor_a.x, coor_goal.x // coor_b.x),1
            else:
                remaining = coor_goal.x % coor_a.x
                return (coor_goal.x // coor_a.x, remaining // coor_b.x),2
        if abs(abs(u[1][2] / u[1][1]) - round(u[1][2] / u[1][1])) > 0.001:
            return (0,0),0
        m = (u[0][2] - round(u[1][2] / u[1][1] * u[0][1]))
        if m % u[0][0] != 0:
            return (0,0),0
        return (round(m / u[0][0]), round(u[1][2] / u[1][1])),(m,u)

    # for evaluating the lu algorithm
    def use_iter():
        def find_best_token_total(cgoal: Coor):
            for i in reversed(range(max(cgoal.x // coor_b.x, cgoal.y // coor_b.y))):
            # for i in range(101):
                b_total = coor_b * i
                if b_total.x > cgoal.x or b_total.y > cgoal.y:
                    continue
                if b_total == cgoal:
                    return (0,i)
                left = cgoal - b_total
                if left.x % coor_a.x == 0 and left.y % coor_a.y == 0 and left.x // coor_a.x == left.y // coor_a.y:
                    return (left.x // coor_a.x, i)
            return (0,0)

        combo = find_best_token_total(coor_goal)
        return combo

    lu_val,lu_case = use_lu()
    total += lu_val[0] * 3 + lu_val[1]
    # print(f'a: {lu_val[0]}\tb: {lu_val[1]}')

    # testing lu vs iteration
    # iter_val = use_iter()
    # if lu_val != iter_val:
    #     print('incorrect:','lu:',lu_val,'iter:',iter_val)
    #     print('lu_case:',lu_case)
    #     print('a:',coor_a,'b:',coor_b,'goal:',coor_goal)

ans(int(total))
