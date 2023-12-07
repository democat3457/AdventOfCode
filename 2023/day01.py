from lib import *

year, day = 2023, 1

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# """.splitlines()

total = 0

words = [0, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nums = list(range(10))

for line in lines:
    if line:
        first = -1, 10**9
        last = -1, -1
        # for c in line:
        #     try:
        #         i = int(c)
        #         if first == -1:
        #             first = i
        #         last = i
        #     except:
        #         pass
        for i, j in itertools.chain(enumerate(words), enumerate(nums)):
            w = str(j)
            try:
                if line.index(w) < first[1]:
                    first = i, line.index(w)
                if line.rindex(w) > last[1]:
                    last = i, line.rindex(w)
            except:
                pass
        num = int(f'{first[0]}{last[0]}')

        # concise one-liners!
        # first = min([ (i, line.find(str(j))) for i, j in itertools.chain(enumerate(words), enumerate(nums)) if line.find(str(j)) != -1 ], key=lambda x: x[1])[0]
        # last = max([ (i, line.rfind(str(j))) for i, j in itertools.chain(enumerate(words), enumerate(nums)) if line.find(str(j)) != -1 ], key=lambda x: x[1])[0]
        # num = int(f'{first}{last}')

        total += num

ans(total)

