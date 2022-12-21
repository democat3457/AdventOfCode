from lib import *

year, day = 2022, 21

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# """.splitlines()

@dataclass
class Operation:
    a: str
    b: str
    op: str

monkeys: Dict[str, int|Operation] = dict()

for line in lines:
    if line:
        m = re.match(r"(\w{4}): (\d+)", line)
        if m is not None:
            monkeys[m.groups()[0]] = int(m.groups()[1])
        else:
            m = re.match(r"(\w{4}): (\w{4}) (.) (\w{4})", line)
            monkeys[m.groups()[0]] = Operation(m.groups()[1], m.groups()[3], m.groups()[2])

def find_value(t: str):
    monkey = monkeys[t]
    if isinstance(monkey, int):
        return monkey
    va = find_value(monkey.a)
    vb = find_value(monkey.b)
    match monkey.op:
        case '+':
            return va+vb
        case '-':
            return va-vb
        case '*':
            return va*vb
        case '/':
            return va//vb

ans(find_value('root'))
