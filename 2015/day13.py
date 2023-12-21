from lib import *

year, day = 2015, 13

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# """.splitlines()

happiness = defaultdict(dict)

for line in lines:
    if line:
        curr, loss, amnt, target = re.match(r'(.+) would (lose|gain) (\d+) happiness units? by sitting next to (.+)\.', line).groups()
        amnt = int(amnt)
        if loss == 'lose':
            amnt *= -1
        happiness[curr][target] = amnt


# Part 02
for person in list(happiness.keys()):
    happiness['me'][person] = 0
    happiness[person]['me'] = 0


max_happiness = 0
for people in itertools.permutations(happiness.keys(), len(happiness)):
    total = 0
    for p1, p2 in zip(people, people[1:] + (people[0],)):
        total += happiness[p1][p2]
        total += happiness[p2][p1]
    max_happiness = max(max_happiness, total)

ans(max_happiness)
