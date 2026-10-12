import math
import matplotlib.pyplot as plt

from helpers import calc_spring_k, calc_p_mass, calc_spring_length, get_pos, calc_fixed_ns, create_initial_coordinates, calc_max_force
from tent_types import Forces
from globals import p_coordinates, g

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
def calc_p_force(N: int, n: int) -> tuple[float, float]:
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

    return fx_tot, fy_tot

def calc_fix_point_iteration(N: int):
    alpha = 0.02
    TOL = 1e-6
    n = 0
    fixed_ns = calc_fixed_ns(N)
    create_initial_coordinates(N, fixed_ns)
    
    while True:
        p_forces: list[Forces] = []

        for n in range(N - 1):
            if n in fixed_ns:
                p_forces.append({"f_x": 0, "f_y": 0})
            else:
                f_x, f_y = calc_p_force(N, n)
                p_forces.append({"f_x": f_x, "f_y": f_y})

        if calc_max_force(p_forces, fixed_ns) < TOL:
            break
        else:     
            for n, force in enumerate(p_forces):
                if n in fixed_ns:
                    continue      

                p_coordinates[n]["x"] += alpha * force["f_x"]
                p_coordinates[n]["y"] += alpha * force["f_y"]


def render_tent():
    calc_fix_point_iteration(25)
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


