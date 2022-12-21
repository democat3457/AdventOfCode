from __future__ import annotations
from lib import *

year, day = 2022, 21

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# """.splitlines()

@dataclass
class Operation:
    a: str|Operation
    b: str|Operation
    op: str
    humn: bool

    def __str__(self) -> str:
        return f'({str(self.a)}){self.op}({str(self.b)})'

monkeys: Dict[str, int|Operation] = dict()

for line in lines:
    if line:
        m = re.match(r"(\w{4}): (\d+)", line)
        if m is not None:
            monkeys[m.groups()[0]] = int(m.groups()[1])
        else:
            m = re.match(r"(\w{4}): (\w{4}) (.) (\w{4})", line)
            monkeys[m.groups()[0]] = Operation(m.groups()[1], m.groups()[3], m.groups()[2], False)

def find_value(t: str):
    if t == 'humn':
        return 'humn'
    monkey = monkeys[t]
    if isinstance(monkey, int):
        return monkey
    va = find_value(monkey.a)
    vb = find_value(monkey.b)
    if va == 'humn' or vb == 'humn':
        return Operation(va, vb, monkey.op, humn=True)
    if isinstance(va, Operation) or isinstance(vb, Operation):
        return Operation(va, vb, monkey.op, humn=True)

    match monkey.op:
        case '+':
            return va+vb
        case '-':
            return va-vb
        case '*':
            return va*vb
        case '/':
            return va//vb

print(find_value('root'))
# ans(find_value('root'))
