from globals import total_p_mass, f_length_0, K, p_coordinates
from tent_types import Coordinates

def calc_p_mass(N: int) -> float:
    return total_p_mass / N

def calc_spring_length(N: int) -> float:
    return f_length_0 / (N - 1)

def calc_spring_k(N: int) -> float:
    return (N-1)*K 
    
def get_pos(index: int) -> Coordinates:
    return p_coordinates[index]