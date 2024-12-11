from lib import *

year, day = 2024, 11

puzzle_input = load(year, day)
# puzzle_input = ""
line = puzzle_input.strip()

total = 0

nums = intlist(line.split())

num_dict = defaultdict(int)

for n in nums:
    num_dict[n] += 1

t = tqdm(range(75)) # Part 01 = 25 ; Part 02 = 75

for _ in t:
    t.set_description(str(len(num_dict)))
    new_nums = defaultdict(int)
    for i, cnt in num_dict.items():
        if i == 0:
            new_nums[1] += cnt
        elif len(str(i)) % 2 == 0:
            new_nums[int(str(i)[:len(str(i))//2])] += cnt
            new_nums[int(str(i)[(len(str(i)) // 2) :])] += cnt
        else:
            new_nums[i*2024] += cnt
    num_dict = new_nums

ans(sum(num_dict.values()))
