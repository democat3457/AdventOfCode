from lib import *
from itertools import repeat

year, day = 2023, 20

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a
# """.splitlines()
# lines = """
# broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output
# """.splitlines()

class Module:
    def __init__(self, name: str, outputs: list[str]) -> None:
        self.name = name
        self.outputs = outputs
    def register_input(self, input_name: str):
        pass
    def process_pulse(self, input_name: str, pulse: str) -> list[tuple[str, str]]:
        raise NotImplementedError
    def make_out_list(self, out_pulse: str):
        return list(zip(repeat(self.name), repeat(out_pulse), self.outputs))

class FlipFlop(Module):
    def __init__(self, name: str, outputs: list[str]) -> None:
        super().__init__(name, outputs)
        self.enabled = False
    def process_pulse(self, input_name: str, pulse: str) -> list[tuple[str, str]]:
        if pulse == 'high':
            return []
        self.enabled = not self.enabled
        out = 'high' if self.enabled else 'low'
        return self.make_out_list(out)

class Conjunction(Module):
    def __init__(self, name: str, outputs: list[str]) -> None:
        super().__init__(name, outputs)
        self.inputs: dict[str, str] = {}
    def register_input(self, input_name: str):
        self.inputs[input_name] = 'low'
    def process_pulse(self, input_name: str, pulse: str) -> list[tuple[str, str]]:
        self.inputs[input_name] = pulse
        if all(v == 'high' for v in self.inputs.values()):
            out = 'low'
        else:
            out = 'high'
        return self.make_out_list(out)

class Broadcaster(Module):
    def process_pulse(self, input_name: str, pulse: str) -> list[tuple[str, str]]:
        return self.make_out_list(pulse)

class Output(Module):
    def process_pulse(self, input_name: str, pulse: str) -> list[tuple[str, str]]:
        return []

class RX(Output):
    def __init__(self, name: str, outputs: list[str]) -> None:
        super().__init__(name, outputs)
        self.input = ""

    def register_input(self, input_name: str):
        self.input = input_name

modules: dict[str, Module] = {}

modules['output'] = Output('output', [])
modules['rx'] = RX('rx', [])

for line in lines:
    if line:
        nametype, outputs = re.match(r'(.+) -> (.+)', line).groups()
        outputs = outputs.split(', ')
        if nametype.startswith('%'):
            name = nametype.removeprefix('%')
            module = FlipFlop(name, outputs)
        elif nametype.startswith('&'):
            name = nametype.removeprefix('&')
            module = Conjunction(name, outputs)
        elif nametype.startswith('broadcaster'):
            name = 'broadcaster'
            module = Broadcaster(name, outputs)
        else:
            raise NotImplementedError
        modules[name] = module

for n, m in modules.items():
    for o in m.outputs:
        modules[o].register_input(n)

# Part 01
# def process_button():
#     low, high = 0,0
#     pulses: deque[tuple[str, str]] = deque([ ('button', 'low', 'broadcaster') ])
#     while len(pulses) > 0:
#         input_name, pulse, output_name = pulses.popleft()
#         if pulse == 'high':
#             high += 1
#         else:
#             low += 1
#         # print(input_name, f'-{pulse}->', output_name)
#         results = modules[output_name].process_pulse(input_name, pulse)
#         pulses.extend(results)
#     return low, high

# low, high = 0,0
# for _ in range(1000):
#     tl, th = process_button()
#     low += tl
#     high += th
# ans(low*high)

# Part 02
rx_conj: Conjunction = modules[modules['rx'].input]
rx_inputs = list(rx_conj.inputs.keys())
rx_input_highs = { name: [] for name in rx_inputs }
for i in tqdm(range(100000)):
    pulses: deque[tuple[str, str]] = deque([ ('button', 'low', 'broadcaster') ])
    while len(pulses) > 0:
        input_name, pulse, output_name = pulses.popleft()
        # print(input_name, f'-{pulse}->', output_name)
        if output_name == rx_conj.name:
            if pulse == 'high':
                rx_input_highs[input_name].append(i)
        results = modules[output_name].process_pulse(input_name, pulse)
        pulses.extend(results)

rx_input_cycles = {}
for i, l in rx_input_highs.items():
    rx_input_cycles[i] = l[1] - l[0]

ans(math.lcm(*rx_input_cycles.values()))
