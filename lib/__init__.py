import copy
import json
import math
import re
from collections import defaultdict, deque
from dataclasses import dataclass, field
from numbers import Number
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Tuple, TypeVar

import functools
import itertools
import numpy as np
import operator
import pyperclip
import requests
from tqdm import tqdm
from operator import itemgetter

from . import astar
from .coords import *
from .grid import *


def load(year, day):
    input_path = Path(f"./inputs/{year}_{day:02}.txt").resolve()
    if input_path.exists():
        p_in = input_path.read_text()
    else:
        req = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies={"session": Path(".session").read_text()},
            headers={"User-Agent": "cwongmath@gmail.com"}
        )
        if req.status_code != 200:
            print(f"Error {req.status_code}: getting request")
            quit(1)
        p_in = req.text + "\n"
        input_path.write_text(p_in)

    return p_in

def get_element_in_arrays(array: Any, indices: Iterable[int], default: Any):
    for idx in indices:
        if 0 <= idx < len(array):
            array = array[idx]
        else:
            return default
    return array

T = TypeVar('T')

def truthy_list(array: Iterable[T]) -> list[T]:
    return [a for a in array if a]

def vec_add(t0: tuple, t1: tuple):
    return (t0[0]+t1[0], t0[1]+t1[1])

def shoelace(nodes: list[Coor]):
    area = 0
    for i in range(len(nodes)):
        area += nodes[i].x * (nodes[(i+1)%len(nodes)].y - nodes[(i-1)%len(nodes)].y)
    area /= 2
    return area

def picks_internal(area: Number, num_of_nodes: Number):
    return (area - (num_of_nodes/2) + 1)

def flatten(ls: Iterable[Iterable[T]]) -> list[T]:
    return [ item for item_list in ls for item in item_list ]

def ans(answer):
    print(answer)
    pyperclip.copy(str(answer))
