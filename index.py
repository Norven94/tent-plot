import math
from typing import TypedDict
import matplotlib.pyplot as plt

class Coordinates(TypedDict):
    y: float
    x: float

# Globala variabler
K = 1 # N/m
g = 9.82 # m/s^2
total_p_mass = 1 # kg
f_length_0 = 1 # m

# Randvillkoren 
ry = 0
rx0 = 0
rx1 = 1

# Tält fästen 
ymax = 1
xmax1 = 1/3
xmax2 = 2/3

# Start koordinater
p_coordinates: list[Coordinates] = [
    {"y": ry, "x": rx0},
    {"y": ymax, "x": xmax1},
    {"y": ymax, "x": xmax2},
    {"y": ry, "x": rx1}
]

# Hjälp funktioner 
def calc_p_mass(N: int) -> float:
    return total_p_mass / N

def calc_spring_length(N: int) -> float:
    return f_length_0 / (N - 1)

def calc_spring_k(N: int) -> float:
    return (N-1)*K 

def get_pos(index: int) -> Coordinates:
    return p_coordinates[index]

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
def calc_p_force(N: int, n: int) -> tuple[float, float, Coordinates]:
    # Flytta dessa senare, den behöver bara räknas en gång
    k = calc_spring_k(N)
    p_mass = calc_p_mass(N)
    spring_length = calc_spring_length(N)

    # Hämtar samtliga x, y koordinater samt räknar ut fjäderns kraft mellan nuvarande partikel och föregående/efterliggande partiklar
    p = get_pos(n)
    p_before = get_pos(n - 1)
    p_before_spring_force = calc_spring_force(p["x"], p["y"], p_before["x"], p_before["y"], k, spring_length)
    p_after = get_pos(n + 1)
    p_after_spring_force = calc_spring_force(p["x"], p["y"], p_after["x"], p_after["y"], k, spring_length)

    # Beräkna slutkraften för den enskilda partikeln. Det är fjäderns kraft mellan föregående och efterliggande partikel
    # som spelar roll här samt gravitationskraften för y-led. 
    fx_tot = p_before_spring_force[0] + p_after_spring_force[0]
    fy_tot = - p_mass * g + p_before_spring_force[1] + p_after_spring_force[1]

    return fx_tot, fy_tot, p

def calc_fix_point_iteration(N: int):
    alpha = 0.02
    TOL = 1e-6
    n = 0
    
    while True:
        N = len(p_coordinates)
        f_x, f_y, previous_coordinates = calc_p_force(N, n)
        new_x_pos = previous_coordinates["x"] + alpha * f_x
        new_y_pos = previous_coordinates["y"] + alpha * f_y
        p_coordinates.insert(n + 1, {
            "x": new_x_pos,
            "y": new_y_pos
        })
        n += 1

        if n > 20:
            # print(p_coordinates)
            break

def render_tent():
    calc_fix_point_iteration(3)
    x = [coordinate["x"] for coordinate in p_coordinates]
    y = [coordinate["y"] for coordinate in p_coordinates]

    fig, ax = plt.subplots() 
    ax.plot( 
        x, y, 
        marker=".", 
        linestyle="-", 
        label="Tent" ,
        color="blue",
    ) 
    ax.legend() 
    plt.show() 


render_tent()


