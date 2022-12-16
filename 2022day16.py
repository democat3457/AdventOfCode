import dataclasses
import itertools
from typing import Tuple
from lib import *
import heapq

year, day = 2022, 16

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB, KK
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II
# Valve KK has flow rate=0; tunnels lead to valves CC, LL
# Valve LL has flow rate=0; tunnel leads to valve KK, MM
# Valve MM has flow rate=0; tunnel leads to valve LL, NN
# Valve NN has flow rate=0; tunnel leads to valve MM, OO
# Valve OO has flow rate=0; tunnel leads to valve NN
# """.splitlines()

@dataclass
class Valve:
    id: str
    flow: int
    tunnels: List[str]

valves: Dict[str, Valve] = dict()
good_valves: List[Valve] = []
good_valve_paths: Dict[Tuple[str, str], int] = dict()

total = 0
start_valve = None

for line in lines:
    if line:
        id, flow, tunnels = re.search("Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line).groups()
        valve = Valve(id, int(flow), tunnels.split(", "))
        valves[id] = valve
        if id == "AA":
            start_valve = valve
        if int(flow) != 0:
            good_valves.append(valve)

target_valves = ([start_valve] + good_valves.copy())
for valve in ([start_valve] + good_valves):
    target_valves.remove(valve)
    queue = list(map(tuple, zip(valve.tunnels.copy(), itertools.repeat(1))))
    visited = []
    atv = target_valves.copy()
    # s = ""
    while len(atv) and len(queue):
        q, d = queue.pop(0)
        visited.append(q)
        v = valves[q]
        if v in atv:
            atv.remove(v)
            good_valve_paths[(valve.id, v.id)] = d
            # s += f"\t{valve.id}({valve.flow}), {v.id}({v.flow}) -> {d}"
        for tunnel_id in v.tunnels:
            if tunnel_id not in visited:
                queue.append((tunnel_id, d+1))
    # print(s)

@dataclass
class Route:
    nodes: List[str]
    remaining_good_valves: List[str] = dataclasses.field(default_factory=lambda: list(map(lambda x: x.id, good_valves)))
    score: int = 0
    minutes_remaining: int = 26

    @property
    def last_node(self):
        return self.nodes[-1]
    
    @property
    def nodes_set(self):
        return set(self.nodes[1:])


current_valve = start_valve
queue = [Route([start_valve.id])]

final_routes: List[Route] = []

while len(queue):
    route = queue.pop(0)
    added = False
    for tunnel_id in route.remaining_good_valves:
        key = (route.last_node, tunnel_id) if ((route.last_node, tunnel_id) in good_valve_paths) else (tunnel_id, route.last_node)
        minutes = good_valve_paths[key] + 1
        mr = route.minutes_remaining - minutes
        if mr <= 0:
            continue

        added = True
        rgv = route.remaining_good_valves.copy()
        rgv.remove(tunnel_id)
        flow = valves[tunnel_id].flow
        queue.append(Route(route.nodes + [tunnel_id], rgv, route.score + (flow * mr), mr))
    if not added:
        # End of route
        final_routes.append(route)

final_routes.sort(key=lambda x: x.score, reverse=True)
# for fr in final_routes[:5]:
#     s = fr.nodes[0]
#     mr = 26
#     for a, b in itertools.pairwise(fr.nodes):
#         key = (a, b) if (a, b) in good_valve_paths else (b, a)
#         dist = good_valve_paths[key]
#         mr -= dist + 1
#         s += f" {dist} +1\t{b}"
#     print(f'{fr.score} rem{fr.minutes_remaining}\t{s}')

max_pair = None
max_score = 0

print(f"{len(final_routes)} routes")

for a, b in tqdm(itertools.combinations(final_routes, 2), total=(len((final_routes)*(len(final_routes)-1))//2)):
    if len(a.nodes_set.intersection(b.nodes_set)):
        continue

    if (s := (a.score + b.score)) > max_score:
        max_score = s
        max_pair = (a, b)

print(max_pair)
ans(max_score)
