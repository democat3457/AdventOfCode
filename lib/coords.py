from __future__ import annotations

from dataclasses import dataclass
from numbers import Number
from typing import Generic, TypeVar, get_args

__all__ = ["Vector2D", "Vec2D", "Coor", "interp_coords"]

T = TypeVar("T", bound=Number)

@dataclass
class Vector2D(Generic[T]):
    x: T
    y: T

    def __init_subclass__(cls) -> None:
        cls._type_T = get_args(cls.__orig_bases__[0])[0]

    @property
    def tup(self):
        return (self.x, self.y)
    
    @classmethod
    def from_(cls, other: Vector2D):
        return cls(cls._type_T(other.x), cls._type_T(other.y))

    def __add__(self, other):
        xval = None
        yval = None
        if isinstance(other, Vector2D):
            xval = other.x
            yval = other.y
        elif isinstance(other, tuple):
            if isinstance(other[0], Number):
                xval = other[0]
            if isinstance(other[1], Number):
                yval = other[1]
        elif isinstance(other, Number):
            xval = other
            yval = other

        if xval is None or yval is None:
            raise NotImplementedError

        return self.__class__(self._type_T(self.x + xval), self._type_T(self.y + yval))
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        xval = None
        yval = None
        if isinstance(other, Vector2D):
            xval = other.x
            yval = other.y
        elif isinstance(other, tuple):
            if isinstance(other[0], Number):
                xval = other[0]
            if isinstance(other[1], Number):
                yval = other[1]
        elif isinstance(other, Number):
            xval = other
            yval = other

        if xval is None or yval is None:
            raise NotImplementedError

        return self.__class__(self._type_T(self.x - xval), self._type_T(self.y - yval))

    def __mul__(self, other):
        xval = None
        yval = None
        if isinstance(other, Vector2D):
            xval = other.x
            yval = other.y
        elif isinstance(other, tuple):
            if isinstance(other[0], Number):
                xval = other[0]
            if isinstance(other[1], Number):
                yval = other[1]
        elif isinstance(other, Number):
            xval = other
            yval = other

        if xval is None or yval is None:
            raise NotImplementedError

        return self.__class__(self._type_T(self.x * xval), self._type_T(self.y * yval))
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        xval = None
        yval = None
        if isinstance(other, Vector2D):
            xval = other.x
            yval = other.y
        elif isinstance(other, tuple):
            if isinstance(other[0], Number):
                xval = other[0]
            if isinstance(other[1], Number):
                yval = other[1]
        elif isinstance(other, Number):
            xval = other
            yval = other

        if xval is None or yval is None:
            raise NotImplementedError

        return self.__class__(self._type_T(self.x / xval), self._type_T(self.y / yval))

    def __abs__(self):
        return self.__class__(self._type_T(abs(self.x)), self._type_T(abs(self.y)))

    def __neg__(self):
        return self.__class__(self._type_T(-self.x), self._type_T(-self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other: Vector2D):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash(self.tup)

@dataclass
class Vec2D(Vector2D[float]):
    pass
@dataclass
class Coor(Vector2D[int]):
    pass

def interp_coords(num, old_min, old_max, new_min, new_max):  # manual way supports interp between Vector2D
    return new_min + (new_max-new_min) * ((num-old_min) / (old_max-old_min))
