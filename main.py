import globals

from helpers import calc_spring_k, calc_p_mass, calc_spring_length, create_initial_coordinates
from render import render_tent, multi_render_tent
from calculations import calc_fix_point_iteration

def init_setup(N: int) -> None:    
    create_initial_coordinates(N)
    globals.spring_k = calc_spring_k(N)
    globals.p_mass = calc_p_mass(N)
    globals.spring_length = calc_spring_length(N)

    calc_fix_point_iteration(N)

def start_cli() -> None:
    while True:
        N = int(input("Hur vill du köra programmet? 1. N = 25, 2. Flera olika val av N, 3. Avsluta"))

        if N == 1:
            init_setup(10)
            render_tent()
        elif N == 2:
            runs = [5, 10, 25, 30]            

            for run in runs:
                init_setup(run)

                # Sparar ner en kopia av koordinaterna som precis kördes och tömmer sedan ursprungslistan igen så vi kan köra från start igen 
                globals.archive_coordinates.append(globals.p_coordinates.copy())
                globals.p_coordinates.clear()

            multi_render_tent()
        else:
            break
        

start_cli()


