from lib import *

year, day = 2023, 12

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
# """.splitlines()

# Original Part 01
# total = 0
# m = 0

# def set_str(s, questions, value: str):
#     x = list(s)
#     value = value.rjust(len(questions), '0').replace('0', '.').replace('1', '#')
#     for q, v in zip(questions, value):
#         x[q] = v
#     return ''.join(x)

# def get_groups(s: str):
#     groups = re.findall(r'(#+)', s)
#     return tuple(map(len, groups))

# for line in tqdm(lines):
#     if line:
#         tmptotal = 0
#         s, groups = line.split()
#         groups = tuple(map(int, groups.split(',')))
#         questions = [i for i, c in enumerate(s) if c == '?']
#         for it in range(2**len(questions)):
#             x = set_str(s, questions, bin(it).replace('0b',''))
#             if get_groups(x) == groups:
#                 tmptotal += 1
#         # print(tmptotal)
#         total += tmptotal

# ans(total)
# quit()

find_cache: dict[tuple[int, str, str], int] = {}

def matches_template(template: str, string: str):
    for t, s in zip(template, string):
        if t != '?' and t != s:
            return False
    return True

def get_key(length, template, groups):
    return str(length) + template + ' ' + ' '.join(groups)

def group_find(length: int, template: str, groups: tuple[str,...]):
    if get_key(length, template, groups) in find_cache:
        return find_cache[get_key(length, template, groups)]
    if len(groups) == 0:
        ret = '.' * length
        retval = 1 if matches_template(template, ret) else 0
        find_cache[get_key(length, template, groups)] = retval
        return retval
    group = groups[0]
    new_groups = groups[1:]
    retval = 0
    for i in range(length-sum(map(len, new_groups))-len(group)+1):
        hashtag = '.'*i + group
        if matches_template(template, hashtag):
            retval += group_find(length-len(hashtag), template[len(hashtag):], new_groups)
    find_cache[get_key(length, template, groups)] = retval
    return retval

total = 0

for line in tqdm(lines):
    if line:
        _s, _groups = line.split()
        _groups = tuple(map(int, _groups.split(',')))
        # New Part 01
        # s, groups = _s, _groups
        s = '?'.join([_s] * 5)
        groups = _groups * 5
        hashtags = [('#'*g + '.') for g in groups]
        hashtags[-1] = hashtags[-1][:-1] # remove . at end of last group

        tmptotal = group_find(len(s), s, tuple(hashtags))
        total += tmptotal

ans(total)
