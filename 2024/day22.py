from lib import *

year, day = 2024, 22

puzzle_input = load(year, day)
# puzzle_input = """
# """
lines = puzzle_input.strip().splitlines()

def mix_and_prune(num1: int, num2: int):
    mixed = num1 ^ num2
    pruned = mixed % 16777216
    return pruned

@functools.lru_cache()
def next_secret_num(num: int):
    num = mix_and_prune(num, num * 64)
    num = mix_and_prune(num, num // 32)
    num = mix_and_prune(num, num * 2048)
    return num

# Part 01
# total = 0

# for line in lines:
#     if line:
#         i = int(line)
#         for _ in range(2000):
#             i = next_secret_num(i)
#         total += i

# ans(total)
# quit()

# Part 02
buyer_prices: list[list[int]] = []

for line in lines:
    if line:
        i = int(line)
        prices = [i%10]
        for _ in range(2000):
            i = next_secret_num(i)
            prices.append(i%10)
        buyer_prices.append(prices)

buyer_changes: dict[tuple[int, int, int, int], int] = defaultdict(int)

for lst in buyer_prices:
    changes = list(map(lambda t: t[1]-t[0], itertools.pairwise(lst)))
    visited = set()
    for i, w in enumerate(more_itertools.sliding_window(changes, 4)):
        real_index = i+4
        if w in visited:
            continue
        visited.add(w)
        buyer_changes[w] += lst[real_index]

maximum = max(buyer_changes.items(), key=itemgetter(1))
print(maximum)
ans(maximum[1])
