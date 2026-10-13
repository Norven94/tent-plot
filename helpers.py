# Filename: helpers.py
# Author:   Oskar Anderberg (941201)
# Created:  2026-10-13
# Description:  Diverse mindre hjälpfunktioner som används i applicationen. Exempelvis för att beräkna vissa värden eller
#               skapa upp de initiala koordinaterna för tältet.

import math
import globals

from tent_types import Coordinates, Forces

def calc_p_mass(N: int) -> float:
    return globals.total_p_mass / N

def calc_spring_length(N: int) -> float:
    return globals.total_spring_length / (N - 1)

def calc_spring_k(N: int) -> float:
    return (N-1)*globals.total_spring_k 

def get_fixed_ns() -> list[int]:
    fixed_ns = [n for n, coordinate in enumerate(globals.p_coordinates) if coordinate["fixed"]]

    return fixed_ns

# Skapar upp totalt N partiklar inkluderat de fasta punkterna som en startform för tältet med raka linjer
def create_initial_coordinates(N: int) -> None:
    for n in range(0, N):        
        x = n / (N - 1)

        # Säkerställer först att alla fixerade punkter och randvillkor följer med
        # samt ger dem en nyckel så vi inte förändrar deras koordinater senare
        if n == 0 or n == N - 1:
            y = globals.ry
            fixed = True
        elif n == round(globals.xmax1 * (N - 1)):
            x = globals.xmax1
            y = globals.ymax
            fixed = True
        elif n == round(globals.xmax2 * (N - 1)):
            x = globals.xmax2
            y = globals.ymax
            fixed = True
        else:
            # xmax1 = 1/3 => k = dy/dx = (1 - 0)/(1/3 - 0) = 3
            if x <= globals.xmax1:
                y = 3 * x
                fixed = False
            elif x <= globals.xmax2:
                # Horizontellt tills vi räknar med fjädrarna och gravitationen
                y = globals.ymax
                fixed = False
            else:
                # x = 2/3 => y = 3(1-2/3) = 1 OK
                # x = 1 => y = 3(1-1) = 0 OK
                y = 3 * (globals.rx1 - x)
                fixed = False

        globals.p_coordinates.append({ "x": x, "y": y, "fixed": fixed })
    
def get_pos(index: int) -> Coordinates:
    return globals.p_coordinates[index]