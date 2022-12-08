from lib import *
import numpy as np

year, day = 2022, 8

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = [
# '30373',
# '25512',
# '65332',
# '33549',
# '35390'
# ]

grid = []

for line in lines:
    if line:
        grid.append(list(map(lambda c: int(c), line)))

h = len(grid)
w = len(grid[0])

results = np.full((h, w), 0)

# part 2
for i in range(h):
    for j in range(w):
        height = grid[i][j]
        print(f'height {height} of {(i, j)}')

        score = 1
        print("up")
        count = 0
        for k in reversed(range(i)):
            count += 1
            print(k, j)
            if grid[k][j] < height:
                continue
            print(f'mult {score} by {count}')
            score *= count
            break
        else:
            print(f'mult {score} by {count}')
            score *= count

        print("down")
        count = 0
        for k in range(i+1, h):
            count += 1
            print(k, j)
            if grid[k][j] < height:
                continue
            print(f'mult {score} by {count}')
            score *= count
            break
        else:
            print(f'mult {score} by {count}')
            score *= count
        print("left")
        count = 0
        for k in reversed(range(j)):
            count += 1
            print(i, k)
            if grid[i][k] < height:
                continue
            print(f'mult {score} by {count}')
            score *= count
            break
        else:
            print(f'mult {score} by {count}')
            score *= count
        print("right")
        count = 0
        for k in range(j+1, w):
            count += 1
            print(i, k)
            if grid[i][k] < height:
                continue
            print(f'mult {score} by {count}')
            score *= count
            break
        else:
            print(f'mult {score} by {count}')
            score *= count

        results[i][j] = score

# part 1
# for i in range(h):
#     max_found = -1
#     for j in range(w):
#         if grid[i][j] > max_found:
#             max_found = grid[i][j]
#             results[i][j] = True
#         # elif grid[i][j] == max_found:
#         #     pass
#         # else:
#         #     break
#     max_found = -1
#     for j in reversed(range(w)):
#         if grid[i][j] > max_found:
#             max_found = grid[i][j]
#             results[i][j] = True
#         # elif grid[i][j] == max_found:
#         #     pass
#         # else:
#         #     break

# for j in range(w):
#     max_found = -1
#     for i in range(h):
#         if grid[i][j] > max_found:
#             max_found = grid[i][j]
#             results[i][j] = True
#         # elif grid[i][j] == max_found:
#         #     pass
#         # else:
#         #     break
#     max_found = -1
#     for i in reversed(range(h)):
#         if grid[i][j] > max_found:
#             max_found = grid[i][j]
#             results[i][j] = True
#         # elif grid[i][j] == max_found:
#         #     pass
#         # else:
#         #     break

# print(results)
ans(np.max(results))
