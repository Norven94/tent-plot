import math

from globals import total_p_mass, f_length_0, K, p_coordinates, xmax1, xmax2, ymax, rx1, ry
from tent_types import Coordinates, Forces

def calc_p_mass(N: int) -> float:
    return total_p_mass / N

def calc_spring_length(N: int) -> float:
    return f_length_0 / (N - 1)

def calc_spring_k(N: int) -> float:
    return (N-1)*K 

def get_fixed_ns() -> list[int]:
    fixed_ns = [n for n, coordinate in enumerate(p_coordinates) if coordinate["fixed"]]
    print(coordinate for n, coordinate in enumerate(p_coordinates) if coordinate["fixed"])
    return fixed_ns

# Skapar upp totalt N partiklar inkluderat de fasta punkterna som en startform för tältet med raka linjer
def create_initial_coordinates(N: int) -> None:
    for n in range(0, N):        
        x = n / (N - 1)

        # Säkerställer först att alla fixerade punkter och randvillkor följer med
        # samt ger dem en nyckel så vi inte förändrar deras koordinater senare
        if n == 0 or n == N - 1:
            y = ry
            fixed = True
        elif x == xmax1:
            x = xmax1
            y = ymax
            fixed = True
        elif x == xmax2:
            x = xmax2
            y = ymax
            fixed = True
        else:
            # xmax1 = 1/3 => k = dy/dx = (1 - 0)/(1/3 - 0) = 3
            if x <= xmax1:
                y = 3 * x
                fixed = False
            elif x <= xmax2:
                # Horizontellt tills vi räknar med fjädrarna och gravitationen
                y = ymax
                fixed = False
            else:
                # x = 2/3 => y = 3(1-2/3) = 1 OK
                # x = 1 => y = 3(1-1) = 0 OK
                y = 3 * (rx1 - x)
                fixed = False

        p_coordinates.append({ "x": x, "y": y, "fixed": fixed })

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

    return max_force
    
def get_pos(index: int) -> Coordinates:
    return p_coordinates[index]