from lib import *
import heapq

year, day = 2023, 22

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 1,0,1~1,2,1
# 0,0,2~2,0,2
# 0,2,3~2,2,3
# 0,0,4~0,2,4
# 2,0,5~2,2,5
# 0,1,6~2,1,6
# 1,1,8~1,1,9
# """.splitlines()

bricks = []
occupied = defaultdict(list)

for line in lines:
    if line:
        id = len(bricks) # -1 == ground
        parts = line.split('~')
        xyz1 = tuple(map(int, parts[0].split(',')))
        xyz2 = tuple(map(int, parts[1].split(',')))
        bricks.append((xyz1, xyz2))
        for x in range(xyz1[0], xyz2[0]+1):
            for y in range(xyz1[1], xyz2[1]+1):
                for z in range(xyz1[2], xyz2[2]+1):
                    occupied[(x,y)].append((z, id))

bricks_below = defaultdict(list)
bricks_above = defaultdict(set)
actual_bricks_below = defaultdict(set)

bricks_on_ground: list[int] = []

for i, (xyz1, xyz2) in enumerate(bricks):
    for x in range(xyz1[0], xyz2[0]+1):
        for y in range(xyz1[1], xyz2[1]+1):
            min_z = min(xyz1[2], xyz2[2])
            occ = list(map(itemgetter(0), occupied[(x,y)]))
            for z in range(min_z -1, 0, -1):
                if z in occ:
                    bricks_below[i].append(occupied[(x,y)][occ.index(z)][1])
                    break
    if len(bricks_below[i]) == 0:
        bricks_on_ground.append(i)
        bricks_below[i].append(-1)

print(len(bricks), len(bricks_below), len(bricks_on_ground))

fallen_brick_zs = { -1: 0 } # -1 == ground

to_process = list(map(lambda i: (1+abs(bricks[i][0][2]-bricks[i][1][2]), i), bricks_on_ground))
heapq.heapify(to_process)

while len(to_process) > 0:
    max_z, brick = heapq.heappop(to_process)
    for subbrick in bricks_below[brick]:
        if (fallen_brick_zs[subbrick] + 1) == (max_z - abs(bricks[brick][0][2]-bricks[brick][1][2])):
            # brick is supported by subbrick
            bricks_above[subbrick].add(brick)
            actual_bricks_below[brick].add(subbrick)

    fallen_brick_zs[brick] = max_z

    # filter for incomplete brick matching
    bricks_above_this = [ (max_z+1+abs(bricks[k][0][2]-bricks[k][1][2]), k) for k,v in bricks_below.items() if brick in v and all(b in fallen_brick_zs for b in v) ]
    for it in bricks_above_this:
        heapq.heappush(to_process, it)
    bricks_above[brick] # generate the empty set

print('# supported by ground:', len(bricks_above[-1]))

# Part 01
removable = 0

for b, a in bricks_above.items():
    if b == -1:
        continue
    for ba in a:
        if len(actual_bricks_below[ba]) == 1:
            break
    else:
        removable += 1

ans(removable)

# Part 02
def disintegrate(brick: int, disintegrated: set[int]) -> int:
    total = 0
    for ba in bricks_above[brick]:
        if len([b for b in actual_bricks_below[ba] if b not in disintegrated]) == 1:
            total += 1 + disintegrate(ba, disintegrated)
            disintegrated.add(ba)
    return total

ans(sum(disintegrate(brick, set()) for brick in range(len(bricks))))
