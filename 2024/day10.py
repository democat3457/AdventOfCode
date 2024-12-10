from lib import *
import heapq

year, day = 2024, 10

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# """.splitlines()

adj = [Coor(0, 1),Coor(0,-1), Coor(1,0), Coor(-1,0)]

total = 0

grid = Grid(lines)

# Part 01
# for c in grid:
#     if grid[c] == "0":
#         q = deque([c])
#         visited = set()
#         while len(q):
#             coor = q.popleft()
#             if coor in visited:
#                 continue
#             visited.add(coor)
#             # print(coor)
#             i = int(grid[coor])
#             if i == 9:
#                 total += 1
#                 continue
#             for d in adj:
#                 if (coor + d) in grid:
#                     # print(grid[coor+d])
#                     if grid[coor + d] == str(i + 1):
#                         q.append(coor + d)

# ans(total)
# quit()

# Part 02
for c in grid:
    if grid[c] == '0':
        q = [(0, c.tup)]
        heapq.heapify(q)
        
        visited = defaultdict(int)
        visited[c.tup] = 1
        while len(q):
            _, coor = heapq.heappop(q)
            i = int(grid[coor])
            
            # print(coor)
            if i == 9:
                total += visited[coor]
                # print(visited[coor])
                continue
            for d in adj:
                if (coor+d) in grid:
                    # print(grid[coor+d])
                    if grid[coor+d] == str(i+1):
                        if (i+1, (coor+d).tup) not in q:
                            q.append((i+1, (coor+d).tup))
                        visited[(coor+d).tup] += visited[coor]

ans(total)
