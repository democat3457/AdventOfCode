from dataclasses import dataclass
from typing import List
from lib import *
from pathlib import Path

year, day = 2022, 7

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()

@dataclass
class Folder:
    path: Path
    size: int

folders: List[Folder] = []

current_folder = Path("")

for line in lines:
    if line:
        if line.startswith("$ "):
            if line.startswith("$ cd"):
                destination = line.split("$ cd ")[1]
                if ".." == destination:
                    current_folder = current_folder.parent
                else:
                    current_folder /= destination
                    if current_folder not in folders:
                        folders.append(Folder(current_folder, 0))
            elif line.startswith("$ ls"):
                pass
        else:
            if line.startswith("dir "):
                pass
            else:
                size, name = line.split()
                for parent in (current_folder / name).parents:
                    for folder in folders:
                        if folder.path == parent:
                            folder.size += int(size)
                # files.append(File(current_folder / name), int(size))

# total = sum([folder.size for folder in folders if folder.size <= 100000])
total = min([folder for folder in folders if folder.size >= 1072511], key = lambda folder: folder.size)
ans(total)
# print([folder.size for folder in folders if folder.path == Path("/")])
