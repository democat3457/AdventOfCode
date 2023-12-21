from __future__ import annotations

from typing import Generic, Iterable, TypeVar

from .coords import Coor

__all__ = [ "Grid" ]

T = TypeVar('T')

class Grid(Generic[T]):
    def __init__(self, lines: list[Iterable[T]]) -> None:
        self._lines = [list(a) for a in lines if a]
        if any(len(l) != self.width for l in self._lines):
            raise ValueError("Jagged array not supported in Grid")

    @property
    def lines(self):
        return self._lines

    @property
    def height(self):
        return len(self.lines)

    @property
    def width(self):
        return len(self.lines[0]) if self.height > 0 else 0

    def rotate_angle(self, angle: int) -> Grid[T]:
        """Rotate grid clockwise.

        Args:
            angle (int): angle to rotate the grid. angle must be a multiple of 90.

        Returns:
            Grid[T]: rotated grid
        """
        angle = angle % 360
        match angle:
            case 0:
                return Grid(self.lines)
            case 90:
                return Grid([ [ self.lines[i][j] for i in range(self.height -1, -1, -1) ] for j in range(self.width)])
            case 180:
                return Grid([ [ self.lines[i][j] for j in range(self.width -1, -1, -1) ] for i in range(self.height -1, -1, -1)])
            case 270:
                return Grid([ [ self.lines[i][j] for i in range(self.height) ] for j in range(self.width -1, -1, -1)])
            case what:
                raise ValueError(f'Invalid rotation angle {what}')

    def transpose(self) -> Grid[T]:
        """Switches columns and rows.

        Returns:
            Grid[T]: transposed grid
        """
        return Grid([ [ self.lines[i][j] for i in range(self.height) ] for j in range(self.width) ])

    def flip_h(self) -> Grid[T]:
        """Return horizontally flipped grid (over center vertical line).

        Returns:
            Grid[T]: horizontally flipped grid
        """
        return Grid([ [ self.lines[i][j] for j in range(self.width -1, -1, -1) ] for i in range(self.height) ])

    def flip_v(self) -> Grid[T]:
        """Return vertically flipped grid (over center horizontal line).

        Returns:
            Grid[T]: vertically flipped grid
        """
        return Grid([ [ self.lines[i][j] for j in range(self.width) ] for i in range(self.height -1, -1, -1) ])

    def in_range(self, idx):
        if isinstance(idx, slice):
            return True
        if isinstance(idx, int):
            return 0 <= idx < self.height
        if isinstance(idx, Coor):
            return 0 <= idx.x < self.height and 0 <= idx.y < self.width
        if isinstance(idx, tuple):
            if isinstance(idx[0], slice):
                return True
            if isinstance(idx[0], int):
                if not (0 <= idx[0] < self.height):
                    return False
                if isinstance(idx[1], slice):
                    return True
                if isinstance(idx[1], int):
                    return 0 <= idx[1] < self.width
        raise TypeError(f'Invalid grid index type for {idx}')

    def copy(self) -> Grid[T]:
        return Grid(self.lines)

    def __contains__(self, idx):
        return self.in_range(idx)

    def __iter__(self):
        for i in range(self.height):
            for j in range(self.width):
                yield Coor(i, j)

    def __getitem__(self, idx):
        if isinstance(idx, (int, slice)):
            return self.lines[idx]
        if isinstance(idx, Coor):
            return self.lines[idx.x][idx.y]
        if isinstance(idx, tuple):
            if isinstance(idx[0], int):
                return self.lines[idx[0]][idx[1]]
            elif isinstance(idx[0], slice):
                return [ l[idx[1]] for l in self.lines[idx[0]] ]
        raise TypeError(f'Invalid grid index type {idx}')
    
    def __setitem__(self, idx, value):
        if isinstance(idx, int):
            self.lines[idx] = value
        elif isinstance(idx, Coor):
            self.lines[idx.x][idx.y] = value
        elif isinstance(idx, tuple):
            self.lines[idx[0]][idx[1]] = value
        else:
            raise TypeError(f'Cannot set index type {type(value)} of Grid')

    def __eq__(self, __value: object) -> bool:
        return self.lines == __value.lines

    def __repr__(self) -> str:
        return repr(self.lines)

    def __str__(self) -> str:
        return '\n'.join(''.join(map(str, s)) for s in self.lines)
