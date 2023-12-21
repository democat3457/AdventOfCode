from lib import *

year, day = 2015, 12

puzzle_input = load(year, day)

total = 0

obj = json.loads(puzzle_input)

def sum_obj(obj):
    if isinstance(obj, int):
        return obj
    if isinstance(obj, str):
        return 0
    if isinstance(obj, list):
        return sum(map(sum_obj, obj))
    if isinstance(obj, dict):
        # Part 01
        # return sum(map(sum_obj, obj.values()))
        # Part 02
        return sum(map(sum_obj, obj.values())) if "red" not in obj.values() else 0

ans(sum_obj(obj))
