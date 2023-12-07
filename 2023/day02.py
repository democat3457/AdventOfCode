from lib import *

year, day = 2023, 2

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# """.splitlines()

total = 0

# Part 01
# for line in lines:
#     if line:
#         g, s = line.split(': ')
#         n = int(g.split()[1])
#         valid = True
#         for group in s.split('; '):
#             for pair in group.split(', '):
#                 num,t = pair.split()
#                 num = int(num)
#                 if t == 'red':
#                     if num > 12:
#                         valid = False
#                 elif t == 'green':
#                     if num > 13:
#                         valid = False
#                 else:
#                     if num > 14:
#                         valid = False
#         if valid:
#             total += n

# Part 02
for line in lines:
    if line:
        g, s = line.split(': ')
        n = int(g.split()[1])
        mr,mg,mb = 0,0,0
        for group in s.split('; '):
            for pair in group.split(', '):
                num,t = pair.split()
                num = int(num)
                if t == 'red':
                    mr = max(num, mr)
                elif t == 'green':
                    mg = max(num, mg)
                else:
                    mb = max(num, mb)
            
        total += mr*mg*mb

ans(total)
