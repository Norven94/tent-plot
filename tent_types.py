# Filename: tent_types.py
# Author:   Oskar Anderberg (941201)
# Created:  2026-10-13
# Description:  Typer som används i hela applicationen för att lättare hantera datan och säkerställa
#               att alla funktioner tar emot och returnerar förutsägbar data.  

from typing import TypedDict

class Coordinates(TypedDict):
    y: float
    x: float
    fixed: bool

class Forces(TypedDict):
    f_y: float
    f_x: float