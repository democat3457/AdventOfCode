from lib import *
import random

year, day = 2023, 25

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# jqt: rhn xhk nvd
# rsh: frs pzl lsr
# xhk: hfx
# cmg: qnr nvd lhk bvb
# rhn: xhk bvb hfx
# bvb: xhk hfx
# pzl: lsr hfx nvd
# qnr: nvd
# ntq: jqt hfx bvb xhk
# nvd: lhk
# lsr: lhk
# rzs: qnr cmg lsr rsh
# frs: qnr lhk lsr
# """.splitlines()

components: set[str] = set()
connections: dict[str, list[str]] = defaultdict(list)
edges: list[frozenset[str]] = []

for line in lines:
    if line:
        name, connected = re.match(r'(\w+): (.+)', line).groups()
        connected = connected.split(' ')
        components.add(name)
        for c in connected:
            components.add(c)
            connections[name].append(c)
            connections[c].append(name)
            edges.append(frozenset((name,c)))

print(len(components))
# print(json.dumps(connections, indent=2))
print(len(edges))

class Graph:
    def __init__(self) -> None:
        self.connections: dict[str, list[str]] = defaultdict(list)
        self.edges: list[frozenset[str]] = []
        self.merged: dict[str, int] = defaultdict(lambda: 1)
    
    def copy(self):
        g = Graph()
        g.connections = { k: v.copy() for k, v in self.connections.items() }
        g.edges = self.edges.copy()
        g.merged = self.merged.copy()
        return g
    
    def __str__(self):
        return f'Conns: {self.connections} ({len(self.connections)})\nEdges: {self.edges}'


# Based on the Karger-Stein algorithm: https://en.wikipedia.org/wiki/Karger%27s_algorithm#Karger%E2%80%93Stein_algorithm
def contract(graph: Graph, t):
    graph = graph.copy()
    while len(graph.connections) > t:
        edge = random.choice(graph.edges)
        firstitem, seconditem = edge
        graph.merged[firstitem] += graph.merged[seconditem]
        while seconditem in graph.connections[firstitem]:
            graph.edges.remove(edge)
            graph.connections[firstitem].remove(seconditem)
        for c in graph.connections[seconditem]:
            if c != firstitem:
                for _ in range(graph.connections[c].count(seconditem)):
                    graph.connections[c].remove(seconditem)
                    graph.connections[c].append(firstitem)
                    graph.connections[firstitem].append(c)
                    graph.edges.remove(frozenset((seconditem, c)))
                    graph.edges.append(frozenset((firstitem, c)))
        del graph.connections[seconditem]
    return graph

def fastmincut(graph: Graph) -> Graph:
    if len(graph.connections) <= 6:
        return contract(graph, 2)
    else:
        t = math.ceil(1 + len(graph.connections) / math.sqrt(2))
        g1 = contract(graph, t)
        g2 = contract(graph, t)
        return min(fastmincut(g1), fastmincut(g2), key=lambda x: len(x.edges))

# test_conns: dict[str, list[str]] = defaultdict(list)
# test_edges_orig: list[tuple[str]] = [
# ('a','b'),
# ('b','c'),
# ('a','c'),
# ('c','d'),
# ('d','e'),
# ('a','f'),
# ('e','f'),
# ('e','g'),
# ('g','b'),
# ('h','a'),
# ('a','i'),
# ('h','i'),
# ('c','j'),
# ]
# test_edges: list[frozenset[str]] = list(map(frozenset, test_edges_orig))
# for e in test_edges:
#     i1, i2 = e
#     test_conns[i1].append(i2)
#     test_conns[i2].append(i1)

# test_graph = Graph()
# test_graph.connections = test_conns
# test_graph.edges = test_edges

# print(test_graph)
# test_graph = fastmincut(test_graph)
# print(test_graph)

# for (i1, i2) in test_graph.edges:
#     print(test_graph.merged[i1], test_graph.merged[i2])
#     break

graph = Graph()
graph.connections = connections
graph.edges = edges

graph = fastmincut(graph)

print(len(graph.connections))
print(len(graph.edges))

for (i1, i2) in graph.edges:
    print(graph.merged[i1], graph.merged[i2])
    ans(graph.merged[i1] * graph.merged[i2])
    break


