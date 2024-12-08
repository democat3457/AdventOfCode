from lib import *

year, day = 2024, 7

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """.splitlines()

total = 0

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

# Part 01
# for line in lines:
#     if line:
#         n, nums = line.split(": ")
#         n = int(n)
#         nums = intlist(nums.split())
#         for j in range(2 ** (len(nums) - 1)):
#             x = (
#                 bin(j)
#                 .replace("0b", "")
#                 .rjust(len(nums) - 1, "0")
#                 .replace("0", "+")
#                 .replace("1", "*")
#             )
#             num = nums[0]
#             for i in range(1, len(nums)):
#                 num = eval(f"{num}{x[i-1]}{nums[i]}")
#             if num == n:
#                 total += n
#                 break
# ans(total)
# quit()

# Part 02
for line in lines:
    if line:
        n,nums = line.split(": ")
        n = int(n)
        nums = intlist(nums.split())
        for j in range(3**(len(nums)-1)):
            x = (
                "".join(map(str, numberToBase(j, 3)))
                .rjust(len(nums) - 1, "0")
                .replace("0", "+")
                .replace("1", "*")
            )
            num = nums[0]
            for i in range(1, len(nums)):
                if x[i-1] == '2':
                    num = int(f'{num}{nums[i]}')
                else:
                    num = eval(f'{num}{x[i-1]}{nums[i]}')
            if num == n:
                total += n
                break

ans(total)
