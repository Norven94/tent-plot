from typing import TypedDict

class Coordinates(TypedDict):
    y: float
    x: float
    fixed: bool

class Forces(TypedDict):
    f_y: float
    f_x: float