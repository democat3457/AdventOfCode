from math import copysign
from lib import *

year, day = 2022, 9

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
# """.splitlines()

tail_visited = set()
rope_length = 2
rope = [(0,0)] * rope_length

for line in lines:
    if line:
        tail_visited.add(rope[rope_length - 1])
        dir, dst = line.split()
        dst = int(dst)
        
        for _ in range(dst):
            if dir == 'U':
                rope[0] = (rope[0][0], rope[0][1]-1)
            elif dir == 'D':
                rope[0] = (rope[0][0], rope[0][1]+1)
            elif dir == 'L':
                rope[0] = (rope[0][0]-1, rope[0][1])
            elif dir == 'R':
                rope[0] = (rope[0][0]+1, rope[0][1])
            for i in range(rope_length - 1):
                if abs(rope[i+1][0] - rope[i][0]) > 1 or abs(rope[i+1][1] - rope[i][1]) > 1:
                    x = rope[i+1][0] + (0 if (rope[i][0]-rope[i+1][0]) == 0 else int(copysign(1, rope[i][0]-rope[i+1][0])))
                    y = rope[i+1][1] + (0 if (rope[i][1]-rope[i+1][1]) == 0 else int(copysign(1, rope[i][1]-rope[i+1][1])))
                    rope[i+1] = (x,y)
            tail_visited.add(rope[rope_length - 1])


tail_visited.add(rope[rope_length - 1])
ans(len(tail_visited))
