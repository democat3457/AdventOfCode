from lib import *
import ast
import functools

year, day = 2022, 13

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """
# """.splitlines()

total = 0
index = 1

@functools.total_ordering
class FancyList:
    def __init__(self, ls: List) -> None:
        self.ls = ls
    
    def __len__(self):
        return len(self.ls)
    
    def __getitem__(self, k):
        return self.ls[k]
    
    def __setitem__(self, k, x):
        self.ls[k] = x
    
    def __lt__(self, other):
        return self.compare(other, 1) == 1
    
    def __eq__(self, other):
        return self.compare(other, 1) == -1
    
    def __gt__(self, other):
        return self.compare(other, 1) == 0

    def compare(self, other, index):
        total = 0
        for i in range(max(len(self), len(other))):
            if i >= len(self):
                total += index
                return total
            elif i >= len(other):
                return total

            if isinstance(self[i], int) and isinstance(other[i], int):
                if self[i] < other[i]:
                    total += index
                    return total
                elif self[i] > other[i]:
                    return total
            
            if isinstance(self[i], list):
                self[i] = FancyList(self[i])
            if isinstance(other[i], list):
                other[i] = FancyList(other[i])
            
            if isinstance(self[i], int) and isinstance(other[i], FancyList):
                self[i] = FancyList([self[i]])
            if isinstance(self[i], FancyList) and isinstance(other[i], int):
                other[i] = FancyList([other[i]])
            
            if isinstance(self[i], FancyList) and isinstance(other[i], FancyList):
                val = self[i].compare(other[i], index)
                if val != -1:
                    return val
        return -1

# l1: List = None
# l2: List = None
# for line in lines:
#     if line:
#         if l1 is None:
#             l1 = FancyList(ast.literal_eval(line))
#         else:
#             l2 = FancyList(ast.literal_eval(line))
#     else:
#         total += l1.compare(l2, index)
#         index += 1
#         l1 = None
#         l2 = None

f1 = FancyList([[2]])
f2 = FancyList([[6]])
lists = [f1, f2]
for line in lines:
    if line:
        lists.append(FancyList(ast.literal_eval(line)))

lists.sort()

ans((lists.index(f1)+1) * (lists.index(f2)+1))
