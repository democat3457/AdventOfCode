from dataclasses import dataclass, field
from typing import Callable, List
from lib import *
import re

year, day = 2022, 11

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1

# """.splitlines()

@dataclass
class Monkey:
    id: int = -1
    items: List[int] = field(default_factory = list)
    operation: Callable = None
    test: int = -1
    on_true: int = -1
    on_false: int = -1
    inspected: int = 0

def oper(t, val):
    return (lambda x: x * val) if t else (lambda x: x + val)

mod = 1

monkeys: List[Monkey] = []
m = None
for line in lines:
    if line:
        if line.startswith("Monkey"):
            m = Monkey()
        if line.startswith("  Starting"):
            m.items = list(map(int, line.split("  Starting items: ")[1].split(", ")))
        if line.startswith("  Operation"):
            if re.search(r"new = old \* old", line) is not None:
                m.operation = lambda x: x * x
            else:
                op, val = re.search(r"new = old (.) (\d+)", line).groups()
                val = int(val)
                if op == "*":
                    m.operation = oper(True, val)
                elif op == "+":
                    m.operation = oper(False, val)
        if line.startswith("  Test"):
            m.test = int(re.search(r"divisible by (\d+)", line).group(1))
            mod *= m.test
        if line.startswith("    If true"):
            m.on_true = int(re.search(r"monkey (\d+)", line).group(1))
        if line.startswith("    If false"):
            m.on_false = int(re.search(r"monkey (\d+)", line).group(1))
    else:
        m.id = len(monkeys)
        monkeys.append(m)

for i in range(10000):
    for m in monkeys:
        for _ in range(len(m.items)):
            item = m.items.pop(0)
            # print(f"Item in: {item}")
            item = m.operation(item)
            item = item % mod
            # print(f"Operation(2) = {m.operation(2)}")
            # item = item // 3
            # print(f"Item out: {item}")
            if item % m.test == 0:
                # print(f"Throw to {m.on_true}")
                monkeys[m.on_true].items.append(item)
            else:
                # print(f"Throw to {m.on_false}")
                monkeys[m.on_false].items.append(item)
            m.inspected += 1
    print(f"Round {i+1}")

a = sorted(monkeys, key=lambda mo: mo.inspected, reverse=True)
ans(a[0].inspected * a[1].inspected)
