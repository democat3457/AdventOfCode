from lib import *
from dataclasses import field

year, day = 2022, 19

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
# Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
# """.splitlines()

@dataclass
class Blueprint:
    id: int
    ore_cost: int
    clay_cost: int
    obsidian_cost: Tuple[int, int]
    geode_cost: Tuple[int, int]
    line: str

@dataclass
class OCOG:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def add_with(self, other):
        self.ore += other.ore
        self.clay += other.clay
        self.obsidian += other.obsidian
        self.geode += other.geode
    
    def copy(self):
        return OCOG(self.ore, self.clay, self.obsidian, self.geode)

bps: List[Blueprint] = []
total = 0

for line in lines:
    if line:
        groups = tuple(map(int, re.findall('(\d+)', line)))
        bps.append(Blueprint(groups[0], groups[1], groups[2], (groups[3], groups[4]), (groups[5], groups[6]), line))

# for bp in bps:
#     robots = OCOG(1)
#     raw = OCOG()
#     next_target = ''
#     print(bp.line)
#     for minute in range(1, 25):
#         print(f"=== Minute {minute} ===")
#         bought = False
#         match next_target:
#             case 'ore':
#                 if raw.ore >= bp.ore_cost:
#                     raw.ore -= bp.ore_cost
#                     bought = True
#                     print('Bought an ore robot')
#             case 'clay':
#                 if raw.ore >= bp.clay_cost:
#                     raw.ore -= bp.clay_cost
#                     bought = True
#                     print('Bought a clay robot')
#             case 'obsidian':
#                 if raw.ore >= bp.obsidian_cost[0] and raw.clay >= bp.obsidian_cost[1]:
#                     raw.ore -= bp.obsidian_cost[0]
#                     raw.clay -= bp.obsidian_cost[1]
#                     bought = True
#                     print('Bought an obsidian robot')
#             case 'geode':
#                 if raw.ore >= bp.geode_cost[0] and raw.obsidian >= bp.geode_cost[1]:
#                     raw.ore -= bp.geode_cost[0]
#                     raw.obsidian -= bp.geode_cost[1]
#                     bought = True
#                     print('Bought a geode robot')
#             case _:
#                 pass

#         raw.add_with(robots)

#         if bought:
#             match next_target:
#                 case 'ore':
#                     robots.ore += 1
#                 case 'clay':
#                     robots.clay += 1
#                 case 'obsidian':
#                     robots.obsidian += 1
#                 case 'geode':
#                     robots.geode += 1
#                 case _:
#                     pass
#             next_target = ''
        
#         print(f'{robots} robots and {raw} resources')

#         # valuable overrides
#         if raw.ore >= bp.geode_cost[0] and raw.obsidian >= bp.geode_cost[1]:
#             next_target = 'geode'
#             print('Overriden next target to geode')
#         # elif raw.ore+1 >= bp.obsidian_cost[0] and raw.clay+1 >= bp.obsidian_cost[1]:
#         #     next_target = 'obsidian'
#         #     print('Overriden next target to obsidian')
        
#         # Find next target robot
#         if not next_target:
#             time_till = OCOG()
#             time_till.ore = math.ceil(max(0, bp.ore_cost - raw.ore) / robots.ore)
#             time_till.clay = math.ceil(max(0, bp.clay_cost - raw.ore) / robots.ore)
#             if robots.clay > 0:
#                 time_till.obsidian = max(math.ceil(max(0, bp.obsidian_cost[0] - raw.ore) / robots.ore), math.ceil(max(0, bp.obsidian_cost[1] - raw.clay) / robots.clay))
#             else:
#                 time_till.obsidian = 10000
#             if robots.obsidian > 0:
#                 time_till.geode = max(math.ceil(max(0, bp.geode_cost[0] - raw.ore) / robots.ore), math.ceil(max(0, bp.geode_cost[1] - raw.obsidian) / robots.obsidian))
#             else:
#                 time_till.geode = 10000
            
#             # print(time_till)
            
#             def find_next_target():
#                 if time_till.ore <= time_till.clay:
#                     if robots.ore < max((bp.clay_cost, bp.obsidian_cost[0], bp.geode_cost[0])):
#                         return 'ore'
#                 if time_till.clay <= time_till.ore:
#                     time_till_ob_modified = max(math.ceil(max(0,bp.obsidian_cost[0]-(raw.ore - bp.clay_cost))/robots.ore), math.ceil(max(0,bp.obsidian_cost[1]-raw.clay)/(robots.clay+1)))
#                     if time_till_ob_modified <= time_till.obsidian:
#                         if robots.obsidian == 0:
#                             return 'clay'
#                     if robots.obsidian > 0:
#                         time_till_ge_modified = max(math.ceil(max(0,bp.geode_cost[0]-(raw.ore - bp.clay_cost))/robots.ore), math.ceil(max(0,bp.geode_cost[1]-raw.obsidian)/(robots.obsidian)))
#                         if time_till_ge_modified < time_till.geode:
#                             return 'clay'
#                 if time_till.obsidian < 10000:
#                     time_till_ge_modified = max(math.ceil(max(0,bp.geode_cost[0]-(raw.ore - bp.obsidian_cost[0]))/robots.ore), math.ceil(max(0,bp.geode_cost[1]-raw.obsidian)/(robots.obsidian+1)))
#                     if time_till_ge_modified <= time_till.geode:
#                         return 'obsidian'
#                 if time_till.geode < 10000:
#                     # if time_till.geode < time_till.obsidian:
#                         return 'geode'
#                     # return 'obsidian'
#                 return 'clay'
#                 # if time_till.geode <= time_till.obsidian and time_till.geode <= time_till.ore and time_till.geode <= time_till.clay:
#                 #     next_target = 'geode'
#                 # elif time_till.obsidian <= time_till.ore and time_till.obsidian <= time_till.clay:
#                 #     next_target = 'obsidian'
#                 # elif time_till.clay <= time_till.ore:
#                 #     next_target = 'clay'
#                 # else:
#                 #     next_target = 'ore'
            
#             next_target = find_next_target()
            
#             print("Time_till:", time_till, "Next target:", next_target)

#     total += bp.id * raw.geode
#     print(bp.id, raw.geode)

@dataclass
class Route:
    robots: OCOG = field(default_factory=lambda: OCOG(1))
    raw: OCOG = field(default_factory=OCOG)
    next_target: str = ''
    minute: int = 1

for bp in bps:
    queue: List[Route] = [Route()]
    max_geodes = 0

    # tq = tqdm([])
    it = 0
    try:
        while len(queue):
            it += 1
            route = queue[0]
            bought = False
            match route.next_target:
                case 'ore':
                    if route.raw.ore >= bp.ore_cost:
                        route.raw.ore -= bp.ore_cost
                        bought = True
                case 'clay':
                    if route.raw.ore >= bp.clay_cost:
                        route.raw.ore -= bp.clay_cost
                        bought = True
                case 'obsidian':
                    if route.raw.ore >= bp.obsidian_cost[0] and route.raw.clay >= bp.obsidian_cost[1]:
                        route.raw.ore -= bp.obsidian_cost[0]
                        route.raw.clay -= bp.obsidian_cost[1]
                        bought = True
                case 'geode':
                    if route.raw.ore >= bp.geode_cost[0] and route.raw.obsidian >= bp.geode_cost[1]:
                        route.raw.ore -= bp.geode_cost[0]
                        route.raw.obsidian -= bp.geode_cost[1]
                        bought = True
                case _:
                    pass

            route.raw.add_with(route.robots)

            if bought:
                match route.next_target:
                    case 'ore':
                        route.robots.ore += 1
                    case 'clay':
                        route.robots.clay += 1
                    case 'obsidian':
                        route.robots.obsidian += 1
                    case 'geode':
                        route.robots.geode += 1
                    case _:
                        pass
                route.next_target = ''
            
            route.minute += 1
            # tq.write(str(route.raw.geode)+' '+str(route.minute))

            if it % 500000 == 0:
                print(f'Iteration {it} | Max: {max_geodes} | Queue len: {len(queue)}')
            # tq.update()
            # tq.set_description(str(max_geodes)+'_'+str(len(queue)))

            if route.minute > 24:
                if route.raw.geode > max_geodes:
                    max_geodes = route.raw.geode
                queue.pop(0)
                continue
            
            # Find next target robot
            if route.minute < 24 and not route.next_target:
                queue.pop(0)
                if route.minute < 22:
                    queue.insert(0, Route(route.robots.copy(), route.raw.copy(), 'ore', route.minute))
                    queue.insert(0, Route(route.robots.copy(), route.raw.copy(), 'clay', route.minute))
                if route.minute < 23 and route.robots.clay > 0:
                    queue.insert(0, Route(route.robots.copy(), route.raw.copy(), 'obsidian', route.minute))
                if route.robots.obsidian > 0:
                    queue.insert(0, Route(route.robots.copy(), route.raw.copy(), 'geode', route.minute))
    except KeyboardInterrupt:
        print(len(queue))
        print(route)


    total += bp.id * max_geodes
    print(bp.id, max_geodes)

ans(total)
