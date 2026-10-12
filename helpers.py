import math

from globals import total_p_mass, f_length_0, K, p_coordinates, xmax1, xmax2, ymax, rx1
from tent_types import Coordinates, Forces

def calc_p_mass(N: int) -> float:
    return total_p_mass / N

def calc_spring_length(N: int) -> float:
    return f_length_0 / (N - 1)

def calc_spring_k(N: int) -> float:
    return (N-1)*K 

def calc_fixed_ns(N:int) -> list[int]:
    x_coordinates = [coordinate["x"] for coordinate in p_coordinates]
    fixed_ns: list[int] = []

    for x_coord in x_coordinates:
        fixed_ns.append(round(N * x_coord))

    return fixed_ns

# Skapar upp totalt N partiklar inkluderat de fasta punkterna 
def create_initial_coordinates(N: int, fixed_ns: list[int]) -> None:
    p_coordinates.clear()
    for n in range(N):
        x = n / (N - 1)

        if x == xmax1:
            y = 1
        elif x < xmax1:
            y = 3 * x
        elif x == xmax2:
            y = 1
        elif x < xmax2:
            y = ymax
        else:
            y = 3 * (rx1 - x)

        p_coordinates.append({ "x": x, "y": y })


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