from lib import *

year, day = 2023, 24

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 19, 13, 30 @ -2,  1, -2
# 18, 19, 22 @ -1, -1, -2
# 20, 25, 34 @ -2, -2, -4
# 12, 31, 28 @ -1, -2, -1
# 20, 19, 15 @  1, -5, -3
# """.splitlines()

'''
s = si + t*vs
m = mi + t1*vm
n = ni + t2*vn
p = pi + t3*vp
'''

MIN_XY = 7
MAX_XY = 27

MIN_XY = 200000000000000
MAX_XY = 400000000000000

DIST_SIDE = MAX_XY-MIN_XY

hail: list[tuple[int,int]] = []

for line in lines:
    if line:
        px,py,pz,vx,vy,vz = map(int, re.findall(r'(-?\d+)', line))

        # if vx+vy+vz == 0:
        #     print('hi!', vx,vy,vz)
        # continue

        # y-y1=(dy/dx)(x-x1)
        # y = (dy/dx)(x-x1) + y1
        # x = (dx/dy)(y-y1) + x1
        # dx(y-y1)=dy(x-x1)
        x1 = (vx/vy)*(MIN_XY-py) + px
        x2 = (vx/vy)*(MAX_XY-py) + px
        y1 = (vy/vx)*(MIN_XY-px) + py
        y2 = (vy/vx)*(MAX_XY-px) + py

        if MIN_XY < px < MAX_XY:
            if vx > 0:
                y1 = 0
            elif vx < 0:
                y2 = 0
        if MIN_XY < py < MAX_XY:
            if vy > 0:
                x1 = 0
            elif vy < 0:
                x2 = 0

        valid_points = [ Coor(c[0],c[1]) for c in ((x1,MIN_XY),(x2,MAX_XY),(MIN_XY,y1),(MAX_XY,y2)) if MIN_XY <= c[0] <= MAX_XY and MIN_XY <= c[1] <= MAX_XY ]
        # valid_points = [ c[2] for c in ((x1,MIN_XY,x1-MIN_XY),(x2,MAX_XY,(MAX_XY-x2)+2*DIST_SIDE),(MIN_XY,y1,(MAX_XY-y1)+3*DIST_SIDE),(MAX_XY,y2,(y2-MIN_XY)+DIST_SIDE)) if MIN_XY <= c[0] <= MAX_XY and MIN_XY <= c[1] <= MAX_XY ]
        if len(valid_points) > 2:
            raise RuntimeError # possibly goes from corner to corner
        if len(valid_points) == 2:
            # hail.append(tuple(sorted(valid_points)))
            hail.append(tuple(valid_points))
        elif len(valid_points) == 1:
            # print('wow it grazes the corner')
            # hail.append((valid_points[0], valid_points[0]))
            hail.append((Coor(px,py), valid_points[0]))

def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

total = 0

for (t1,i),(t2,j) in itertools.combinations(enumerate(hail), 2):
    # if j[0] < i[0] <= i[1] <j[1] or i[0] < j[0] <= j[1] < i[1]:
    #     continue
    if not intersect(i[0],i[1],j[0],j[1]):
        continue
    total += 1
    # print(t1,t2)

ans(total)
