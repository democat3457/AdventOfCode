from lib import *

import graphviz

year, day = 2024, 24

puzzle_input = load(year, day)
# puzzle_input = """
# """
lines = puzzle_input.strip().splitlines()
part_a, part_b = listsplit(lines, "")

# for Part 02
toswap = {
    "input classified": "wire to swap with",
    "wire to swap with": "input classified",
}
problem_wires: tuple[int] = (-1,) # problem wires to look at... highlighted red in graph
# teehee

wires: dict[str, str | tuple[str, str, str]] = dict()
solved = dict()
xs = []
ys = []

for line in part_a:
    if line:
        a,b = line.split(': ')
        wires[a] = b
        solved[a] = b
        if a.startswith("x"):
            idx = int(a.replace("x", ""))
            xs.append((idx, b))
        elif a.startswith("y"):
            idx = int(a.replace("y", ""))
            ys.append((idx, b))

x_val = int("".join(map(itemgetter(1), sorted(xs, reverse=True))), 2)
y_val = int("".join(map(itemgetter(1), sorted(ys, reverse=True))), 2)
actual = x_val + y_val
actual_str = bin(actual).removeprefix("0b")
print(actual_str)

# Visualization for manual Part 02
graph = graphviz.Digraph("2024day24")

for line in part_b:
    if line:
        a,op,b,c = re.match(r"(...) (.+) (...) -> (...)", line).groups()

        # code for part 02
        if c in toswap:
            c = toswap[c]
        if c.startswith('z'):
            idx = int(c.replace('z',''))
            if idx in problem_wires:
                graph.node(c, c, style='filled', fillcolor='red')

        if op == "XOR":
            op = '^'
        elif op == "OR":
            op = '|'
        elif op == 'AND':
            op = '&'
        wires[c] = (a, b, op)

@functools.lru_cache()
def solve(wire: str):
    if wire in solved:
        return solved[wire]
    if isinstance(wires[wire], tuple):
        a,b,op = wires[wire]
        val_a = solve(a)
        val_b = solve(b)
        res = eval(val_a + op + val_b)
        graph.edge(a, wire, f'{op} {res}')
        graph.edge(b, wire, f'{op} {res}')

        return str(res)
    raise ValueError

zs = []

for w in wires.keys():
    if w.startswith('z'):
        z_val = solve(w)
        idx = int(w.replace('z',''))
        zs.append((idx, z_val))

graph.render(directory=Path("inputs/graphviz"))

string = "".join(map(itemgetter(1), sorted(zs, reverse=True)))
print(string)

result = int(string, 2)

ans(result)
