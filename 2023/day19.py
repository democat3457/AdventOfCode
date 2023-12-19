from lib import *

year, day = 2023, 19

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}
# """.splitlines()
# lines = """
# in{s<2001:A,a>2000:A,R}
# """.splitlines()

# Part 01
# total = 0
# workflows: dict[str, list[tuple[Callable[[dict[str, int]], bool], str]]] = {}

# def process_workflow(workflow_name, part):
#     print(workflow_name)
#     if workflow_name == 'A':
#         return True
#     if workflow_name == 'R':
#         return False
#     conditions = workflows[workflow_name]
#     for c, v in conditions:
#         if eval(c):
#             return process_workflow(v, part)

# for line in lines:
#     if line:
#         if not line.startswith('{'):
#             name, conditions_str = re.match(r'^(.+){(.+)}', line).groups()
#             conditions = []
#             for cond in conditions_str.split(','):
#                 if ':' in cond:
#                     how, what = cond.split(':')
#                     val, comp, num = re.match(r'(\w)(.)(\d+)', how).groups()
#                     num = int(num)
#                     print(name, '-', val, comp, num, ':', what)
#                     conditions.append((f'part["{val}"]{comp}{num}', what))
#                     # conditions.append(((lambda p: p[val] < num) if comp == '<' else (lambda p: p[val] > num), what))
#                 else:
#                     print(name, '-', True, ':', cond)
#                     # conditions.append((lambda p: True, cond))
#                     conditions.append(('True', cond))
#             workflows[name] = conditions
#         else:
#             line = line.replace('{','').replace('}','')
#             part = {}
#             for s in line.split(','):
#                 n,e = s.split('=')
#                 e = int(e)
#                 part[n] = e
#             print(part)
#             if process_workflow('in', part):
#                 print('accepted')
#                 total += sum(part.values())
#             else:
#                 print('rejected')
# ans(total)
# quit()

# Part 02
workflows: dict[str, list[tuple[Callable[[dict[str, int]], bool], str]]] = {}

def process_workflow(workflow_name, ranges):
    # print(workflow_name)
    if workflow_name == 'A':
        return functools.reduce(operator.mul, map(lambda t: max(0, t[1]-t[0]-1),ranges), 1)
    if workflow_name == 'R':
        return 0
    conditions = workflows[workflow_name]
    subtotal = 0
    for (val,comp,num), v in conditions:
        new_ranges = copy.copy(ranges)
        if val is not True:
            if comp == '<':
                new_ranges[val] = new_ranges[val][0], min(num, new_ranges[val][1])
            else:
                new_ranges[val] = max(num, new_ranges[val][0]), new_ranges[val][1]
        res = process_workflow(v, new_ranges)
        subtotal += res
        # add "not in range" subrange for subsequent conditions
        if val is True:
            break
        if comp == '<':
            ranges[val] = max(num-1, ranges[val][0]), ranges[val][1]
        else:
            ranges[val] = ranges[val][0], min(num+1, ranges[val][1])
    return subtotal

for line in lines:
    if line:
        if not line.startswith('{'):
            name, conditions_str = re.match(r'^(.+){(.+)}', line).groups()
            conditions = []
            for cond in conditions_str.split(','):
                if ':' in cond:
                    how, what = cond.split(':')
                    val, comp, num = re.match(r'(\w)(.)(\d+)', how).groups()
                    num = int(num)
                    print(name, '-', val, comp, num, ':', what)
                    conditions.append((('xmas'.index(val), comp, num), what))
                else:
                    print(name, '-', (True), ':', cond)
                    conditions.append(((True,0,0), cond))
            workflows[name] = conditions

ans(process_workflow('in', [(0, 4001)] * 4))
