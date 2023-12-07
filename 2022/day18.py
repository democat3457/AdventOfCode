from lib import *
from operator import add, mul

year, day = 2022, 18

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# 2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5
# """.splitlines()

faces = [
    (0,0,1),
    (0,0,-1),
    (0,1,0),
    (0,-1,0),
    (1,0,0),
    (-1,0,0),
]

total = 0
cubes = []

for line in lines:
    if line:
        cube = tuple(map(int, line.split(',')))
        cubes.append(cube)

sa = 0
valid_faces = []

for cube in cubes:
    for face in faces:
        if tuple(map(add, cube, face)) not in cubes:
            sa += 1
            valid_faces.append((cube, face))

outside_cubes = set()
outside_faces = []

for _ in tqdm(range(5), total=5):
    tqdm.write(str(len(outside_faces)))
    for vf in valid_faces:
        if vf in outside_faces:
            continue
        visited = set()
        for i in range(1,22):
            cube = tuple(map(add, vf[0], map(mul, vf[1], (i,i,i))))
            visited.add(cube)

            if cube in cubes:
                break

            if cube in outside_cubes or any(map(lambda x: x < 0 or x > 21, cube)):
                outside_cubes = outside_cubes.union(visited)
                outside_faces.append(vf)
                break



ans(len(outside_faces))
