from lib import *

year, day = 2024, 5

puzzle_input = load(year, day)
lines = puzzle_input.strip().splitlines()
# lines = """
# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# """.strip().splitlines()

total = 0

rules: dict[int, dict[int, str]] = defaultdict(dict)

rule_parsing = True
for line in lines:
    if line:
        if rule_parsing:
            a,b = map(int, line.split('|'))
            rules[a][b] = 'lt'
            rules[b][a] = 'gt'
        else:
            nums = list(map(int,line.split(",")))
            valid = True
            idx = 0
            for i, n in enumerate(nums):
                for j in range(i+1, len(nums)):
                    if rules[n][nums[j]] == 'gt':
                        valid = False
                        idx = i
                        break
                if not valid:
                    break

            # Part 01
            # if valid:
            #     total += nums[len(nums) // 2]
            # continue

            # Part 02
            if not valid:
                for n in nums:
                    cnts = list(map(itemgetter(1), filter(lambda t: t[0] in nums, rules[n].items())))
                    if cnts.count("gt") == cnts.count("lt"):
                        total += n
                        break
    else:
        rule_parsing = False

ans(total)
