import globals

from helpers import calc_spring_k, calc_p_mass, calc_spring_length, create_initial_coordinates
from render import render_tent
from calculations import calc_fix_point_iteration

def init_setup() -> None:
    N = int(input("Välj N"))

    create_initial_coordinates(N)
    globals.spring_k = calc_spring_k(N)
    globals.p_mass = calc_p_mass(N)
    globals.spring_length = calc_spring_length(N)

    calc_fix_point_iteration(N)

def start() -> None:
    init_setup()
    render_tent()

start()


