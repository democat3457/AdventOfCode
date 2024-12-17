from lib import *

year, day = 2024, 17

puzzle_input = load(year, day)
# puzzle_input = """
# Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0
# """
# puzzle_input = """
# Register A: 2024
# Register B: 29
# Register C: 9

# Program: 1,7
# """
lines = puzzle_input.strip()

total = 0

reg_a = int(re.search(r"Register A: (\d+)", lines).group(1))
reg_b = int(re.search(r"Register B: (\d+)", lines).group(1))
reg_c = int(re.search(r"Register C: (\d+)", lines).group(1))
prog = intlist(re.search(r"Program: (.+)$", lines).group(1).split(','))

# Part 02 test values
# reg_a = 164250032175541
# reg_a = 1223756

# Part 01
# out = []
# pointer = 0

# while pointer < len(prog):
#     opcode, operand = prog[pointer:pointer+2]
#     lit = operand

#     def get_combo():
#         if operand <= 3:
#             combo = operand
#         elif operand == 4:
#             combo = reg_a
#         elif operand == 5:
#             combo = reg_b
#         elif operand == 6:
#             combo = reg_c
#         else:
#             print("Error")
#         return combo

#     if opcode == 0:
#         reg_a = reg_a >> get_combo()
#     elif opcode == 1:
#         reg_b ^= lit
#     elif opcode == 2:
#         reg_b = get_combo() % 8
#     elif opcode == 3:
#         if reg_a != 0:
#             pointer = lit
#             continue
#     elif opcode == 4:
#         reg_b ^= reg_c
#     elif opcode == 5:
#         out.append(get_combo() % 8)
#     elif opcode == 6:
#         reg_b = reg_a >> get_combo()
#     elif opcode == 7:
#         reg_c = reg_a >> get_combo()
#     pointer += 2

# print(reg_a, reg_b, reg_c)

# ans(','.join(map(str, out)))
# quit()

# Part 02
def inv(c: str):
    return '0' if c == '1' else '1'
def invstr(invkey: str, s: str):
    return ''.join( inv(c) if ik == '~' else c for ik, c in zip(invkey, s) )

# cases crafted to input
cases: tuple[str, str, Callable[[tuple[str, ...]], str]] = [
    ("000", r"(.)$", lambda gs: inv(gs[0]) + '00'),
    ("001", r"$", lambda gs: '100'),
    ("010", r"(.)(.)(.)$", lambda gs: invstr('~~+', gs)),
    ("011", r"(.)(.)$", lambda gs: invstr('~~', gs) + '1'),
    ("100", r"(.)(.)(.)..$", lambda gs: invstr('+++', gs)),
    ("101", r"(.)(.)(.).$", lambda gs: invstr('++~', gs)),
    ("110", r"(.)(.)(.)....$", lambda gs: invstr('+~+', gs)),
    ("111", r"(.)(.)(.)...$", lambda gs: invstr('+~~', gs)),
]


max_val = '1'*200
# DFA-ish
def find_min_sol(s: str, prog: list[int]):
    if not len(prog):
        return s
    valid = []
    next_out = bin(prog[-1]).removeprefix('0b').rjust(3, '0')
    for pot_case, pattern, out_func in cases:
        new_s = s.rjust(pattern.count("."), "0")
        m = re.search(pattern, new_s)
        if m:
            out = out_func(m.groups())
            if next_out == out:
                sol = find_min_sol(new_s + pot_case, prog[:-1])
                valid.append(sol)
                continue
        valid.append(max_val)
    return min(valid, key=lambda x: int(x, 2))

s = find_min_sol("", prog)
print(prog)
print(s)
ans(int(s, 2))
