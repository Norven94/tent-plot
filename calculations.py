# Filename: calculations.py
# Author:   Oskar Anderberg (941201)
# Created:  2026-10-13
# Description:  Beräknar olika fjäderkrafter samt gravitationskraft på en partikel. Samt kör en fixpunktsalgoritm 
#               för att uppdatera respektive partikels koordinater utefter de uträknade krafterna som påverkar dem. 

import math
import globals

from helpers import get_pos, get_fixed_ns
from tent_types import Forces

# Returnerar kraften för den partikel med högst kraft
def calc_max_force(p_forces: list[Forces], fixed_ns: list[int]) -> float:
    max_force = 0

    for n, force in enumerate(p_forces):
            if n in fixed_ns:
                continue

            # Den sammanställda partikelns kraft 
            total_p_force = math.sqrt(force["f_x"]**2 + force["f_y"]**2)

            if total_p_force > max_force:
                max_force = total_p_force

    # Behåller max_force efter varje fixpunktsiteration så den kan plotas ut senare
    globals.max_forces.append(max_force)

    return max_force

def calc_spring_force(xn: float, yn: float, xj: float, yj: float, k: float, spring_length: float) -> tuple[float, float]:
    dx = xj - xn
    dy = yj - yn

    new_spring_length = math.sqrt(dx**2 + dy**2)
    # d_length > 0 (fjädern drar) / d_length < 0 (fjädern trycker)
    d_length = new_spring_length - spring_length

    fx = k * d_length * ((xj-xn) / new_spring_length)
    fy = k * d_length * ((yj-yn) / new_spring_length)

    return fx, fy

# Beräknar krafterna i x och y-led för partikel n. 
def calc_p_force(n: int) -> tuple[float, float]:
    # Hämtar samtliga x, y koordinater samt räknar ut fjäderns kraft mellan nuvarande partikel och föregående/efterliggande partiklar
    p = get_pos(n)
    p_before = get_pos(n - 1)
    p_before_spring_force = calc_spring_force(p["x"], p["y"], p_before["x"], p_before["y"], globals.spring_k, globals.spring_length)
    p_after = get_pos(n + 1)
    p_after_spring_force = calc_spring_force(p["x"], p["y"], p_after["x"], p_after["y"], globals.spring_k, globals.spring_length)

    # Beräkna slutkraften för den enskilda partikeln. Det är fjäderns kraft mellan föregående och efterliggande partikel
    # som spelar roll här samt gravitationskraften för y-led. 
    fx_tot = p_before_spring_force[0] + p_after_spring_force[0]
    fy_tot = - globals.p_mass * globals.g + p_before_spring_force[1] + p_after_spring_force[1]

    return fx_tot, fy_tot

# Kör fixpunktsiterationen och uppdaterar respektive partikels position baserat på krafterna som påverkar den.
def calc_fix_point_iteration(N: int) -> None:
    alpha = 0.001
    TOL = 1e-6
    n = 0
    fixed_ns = get_fixed_ns()
    
    while True:
        p_forces: list[Forces] = []

        for n in range(N - 1):
            if n in fixed_ns:
                p_forces.append({"f_x": 0, "f_y": 0})
            else:
                f_x, f_y = calc_p_force(n)
                p_forces.append({"f_x": f_x, "f_y": f_y})

        # Vi avslutar iterationen när den partikel med högst kraft har en kraft som är lägre än 10^-6N
        if calc_max_force(p_forces, fixed_ns) < TOL:
            break
        else:     
            for n, force in enumerate(p_forces):
                if n in fixed_ns:
                    continue      

                globals.p_coordinates[n]["x"] += alpha * force["f_x"]
                globals.p_coordinates[n]["y"] += alpha * force["f_y"]