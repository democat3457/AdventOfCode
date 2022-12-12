import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, List

import numpy as np
import pyperclip
import requests


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

def ans(answer):
    print(answer)
    pyperclip.copy(str(answer))
