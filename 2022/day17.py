from __future__ import annotations
from lib import *
from copy import deepcopy

year, day = 2022, 17

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
# lines = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
# """.splitlines()
jets = list(lines[0])
jet_index = 0

class Block:
    class Type:
        def __init__(self, grid: List[List[int]], left_check: List[List[int]], right_check: List[List[int]], down_check: List[List[int]]) -> None:
            self.grid = np.array(grid)
            self.left_check = np.array(left_check)
            self.right_check = np.array(right_check)
            self.down_check = np.array(down_check)

            self.origin = (self.grid.shape[0]-2, 1) # y,x

    types = [
        Type(
            [
                [0,1,1,1,1,0],
                [0,0,0,0,0,0],
            ],
            [
                [1,0,0,0,0,0],
                [0,0,0,0,0,0],
            ],
            [
                [0,0,0,0,0,1],
                [0,0,0,0,0,0],
            ],
            [
                [0,0,0,0,0,0],
                [0,1,1,1,1,0],
            ],
        ),
        Type(
            [
                [0,0,1,0,0],
                [0,1,1,1,0],
                [0,0,1,0,0],
                [0,0,0,0,0],
            ],
            [
                [0,1,0,0,0],
                [1,0,0,0,0],
                [0,1,0,0,0],
                [0,0,0,0,0],
            ],
            [
                [0,0,0,1,0],
                [0,0,0,0,1],
                [0,0,0,1,0],
                [0,0,0,0,0],
            ],
            [
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,1,0,1,0],
                [0,0,1,0,0],
            ],
        ),
        Type(
            [
                [0,0,0,1,0],
                [0,0,0,1,0],
                [0,1,1,1,0],
                [0,0,0,0,0],
            ],
            [
                [0,0,1,0,0],
                [0,0,1,0,0],
                [1,0,0,0,0],
                [0,0,0,0,0],
            ],
            [
                [0,0,0,0,1],
                [0,0,0,0,1],
                [0,0,0,0,1],
                [0,0,0,0,0],
            ],
            [
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,1,1,1,0],
            ],
        ),
        Type(
            [
                [0,1,0],
                [0,1,0],
                [0,1,0],
                [0,1,0],
                [0,0,0],
            ],
            [
                [1,0,0],
                [1,0,0],
                [1,0,0],
                [1,0,0],
                [0,0,0],
            ],
            [
                [0,0,1],
                [0,0,1],
                [0,0,1],
                [0,0,1],
                [0,0,0],
            ],
            [
                [0,0,0],
                [0,0,0],
                [0,0,0],
                [0,0,0],
                [0,1,0],
            ],
        ),
        Type(
            [
                [0,1,1,0],
                [0,1,1,0],
                [0,0,0,0],
            ],
            [
                [1,0,0,0],
                [1,0,0,0],
                [0,0,0,0],
            ],
            [
                [0,0,0,1],
                [0,0,0,1],
                [0,0,0,0],
            ],
            [
                [0,0,0,0],
                [0,0,0,0],
                [0,1,1,0],
            ],
        ),
    ]

    def __init__(self, type: Type, coord: Tuple[int, int], grid: np.ndarray) -> None:
        self.type = type
        self.coord = coord
        self.grid = grid
    
    @property
    def top_left_coord(self):
        return (self.coord[0]-self.type.grid.shape[0]+2, self.coord[1]-1)

    def move_left(self) -> bool:
        able = not (self.type.left_check & (self.grid[self.top_left_coord[0]:self.top_left_coord[0]+self.type.left_check.shape[0],self.top_left_coord[1]:self.top_left_coord[1]+self.type.left_check.shape[1]])).any()
        if not able:
            return False
        self.coord = (self.coord[0], self.coord[1]-1)
        return True

    def move_right(self) -> bool:
        able = not (self.type.right_check & (self.grid[self.top_left_coord[0]:self.top_left_coord[0]+self.type.right_check.shape[0],self.top_left_coord[1]:self.top_left_coord[1]+self.type.right_check.shape[1]])).any()
        if not able:
            return False
        self.coord = (self.coord[0], self.coord[1]+1)
        return True

    def move_down(self) -> bool:
        able = not (self.type.down_check & (self.grid[self.top_left_coord[0]:self.top_left_coord[0]+self.type.down_check.shape[0],self.top_left_coord[1]:self.top_left_coord[1]+self.type.down_check.shape[1]])).any()
        if not able:
            return False
        self.coord = (self.coord[0]+1, self.coord[1])
        return True
    
    def add_to_grid(self):
        self.grid[self.top_left_coord[0]:self.top_left_coord[0]+self.type.grid.shape[0],self.top_left_coord[1]:self.top_left_coord[1]+self.type.grid.shape[1]] |= self.type.grid

    index = 0

    @classmethod
    def next_type(cls) -> Type:
        t = cls.types[cls.index]
        cls.index += 1
        cls.index %= len(cls.types)
        return t

grid = np.array([0])

def reset_grid():
    global grid
    grid = np.array([
        [1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1],
    ])

reset_grid()

def get_highest_coord():
    for i in range(grid.shape[0]):
        if grid[i][1:8].any():
            return i
    return 0

def add_row():
    global grid
    grid = np.vstack(((1,0,0,0,0,0,0,0,1), grid))
    # if grid.shape[0] > 200:
    #     grid = grid[:200]

def get_height():
    return grid.shape[0]-get_highest_coord()-1

def make_key():
    return np.array2string(grid[:30], separator='')+f'_{Block.index}_{jet_index}'

key_to_match = None
matched_index_height = (0,0)
# mod = len(jets)*len(Block.types)

def drop_block():
    global jet_index, grid

    t = Block.next_type()
    bh = t.grid.shape[0]
    c = get_highest_coord()
    for _ in range(3-c+bh-1):
        add_row()
    
    block = Block(t, (get_highest_coord()-4, 3), grid)

    # moved = True
    while True:
        # moved = False
        d = jets[jet_index]
        jet_index += 1
        jet_index %= len(jets)
        match d:
            case '<':
                # moved = block.move_left() or moved
                block.move_left()
            case '>':
                block.move_right()
            case _:
                print(f'huh? weird jet character {_}')
        b = block.move_down()
        if not b:
            break
    
    block.add_to_grid()

for i in tqdm(range(200000)):
    if i % 5 == 0 and i >= 200:
        if key_to_match is None:
            key_to_match = make_key()
            matched_index_height = (i, get_height())
        else:
            key = make_key()
            if key == key_to_match:
                print(key)
                print(f'Matched {matched_index_height} with {(i, get_height())}')
                break
    drop_block()

cycle_iter = i-matched_index_height[0]
cycle_height = get_height()-matched_index_height[1]
print(f'Cycles every {cycle_iter} iterations with {cycle_height} height')

d, m = divmod(1000000000000, cycle_iter)

Block.index = 0
jet_index = 0
reset_grid()

for i in tqdm(range(cycle_iter+m)):
    drop_block()

ans((d-1)*cycle_height + get_height())
