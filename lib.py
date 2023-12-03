import math
import re
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Tuple

import itertools
import numpy as np
import operator
import pyperclip
import requests
from tqdm import tqdm

from coords import Vec2D, Coor, interp_coords


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

def vec_add(t0: Tuple, t1: Tuple):
    return (t0[0]+t1[0], t0[1]+t1[1])

def ans(answer):
    print(answer)
    pyperclip.copy(str(answer))
