from lib import *
from tqdm import tqdm

year, day = 2022, 15

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3
# """.splitlines()

occupied_ranges: Dict[int, List] = dict()
ln = 0

for line in lines:
    if line:
        ln += 1
        print(ln, line)
        print(len(occupied_ranges))
        sx, sy, bx, by = tuple(map(int, re.search("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()))
        dist = abs(sx - bx) + abs(sy - by)
        for y in tqdm(range(sy-dist, sy+dist+1)):
            cd = abs(sy - y)
            if y in occupied_ranges:
                l: List = occupied_ranges[y]
                start = sx-(dist-cd)
                end = sx+(dist-cd)
                merged = False
                finish = False
                while not finish:
                    for i in range(len(l)):
                        if l[i][0] <= start <= l[i][1] and l[i][0] <= end <= l[i][1]:
                            merged = True
                            finish = True
                            break
                        if start < l[i][0] < end and start < l[i][1] < end:
                            if (start, end) not in l:
                                l[i] = (start, end)
                            else:
                                l.pop(i)
                            merged = True
                            break
                        # if ln == 6 and y > (sy-dist+660000):
                        #     tqdm.write(f"{l[i]} {(start, end)}")
                        if l[i][0] < start < l[i][1] or l[i][0] < end < l[i][1]:
                            l[i] = (min(l[i][0], start), max(end, l[i][1]))
                            merged = True
                            break
                    else:
                        break
                if not merged:
                    l.append((start, end))
            else:
                occupied_ranges[y] = [(sx-(dist-cd),sx+(dist-cd))]

for r, k in tqdm(occupied_ranges.items()):
    merged = False
    if len(k) > 1:
        finish = False
        k.sort(key=lambda x: x[0])
        while not finish:
            for i in range(len(k)-1):
                if k[i+1][0] <= k[i][0] <= k[i+1][1] and k[i+1][0] <= k[i][1] <= k[i+1][1]:
                    k.pop(i)
                    merged = True
                    break
                if k[i][0] <= k[i+1][0] <= k[i][1] and k[i][0] <= k[i+1][1] <= k[i][1]:
                    k.pop(i+1)
                    merged = True
                    break
                if k[i][0] < k[i+1][0] <= k[i][1] or k[i][0] <= k[i+1][1] < k[i][1]:
                    k[i] = (min(k[i][0], k[i+1][0]), max(k[i+1][1], k[i][1]))
                    k.pop(i+1)
                    merged = True
                    break
            else:
                break
            k.sort(key=lambda x: x[0])
    if len(k) > 1 and 0 <= r <= 4000000:
        print(r, k)


# print([(r, k) for (r, k) in occupied_ranges.items() if len(k) > 1])
# ans(len([o for o in occupied if (o[1] == 2000000 and o not in beacons)]))
# ans(len(occupied))
