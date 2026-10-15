# Filename: main.py
# Author:   Oskar Anderberg (941201)
# Created:  2026-10-13
# Description:  Applicationens huvud, här startar vi applicationen och säger till den vilket läge vi 
#               vill köra.
 
import globals

from helpers import calc_spring_k, calc_p_mass, calc_spring_length, create_initial_coordinates
from render import render_tent, multi_render_tent
from calculations import run_fix_point_iteration

def reset() -> None: 
    globals.max_forces.clear()
    globals.p_coordinates.clear()

def init_setup(N: int) -> None:    
    create_initial_coordinates(N)
    globals.spring_k = calc_spring_k(N)
    globals.p_mass = calc_p_mass(N)
    globals.spring_length = calc_spring_length(N)

    run_fix_point_iteration(N)

def start_cli() -> None:
    while True:
        N = int(input("Hur vill du köra programmet? 1. N = 25, 2. Flera olika val av N, 3. Avsluta"))

        if N == 1:
            init_setup(25)
            render_tent()
            reset()
        elif N == 2:
            # Max 4 värden annars måste fler färger läggas till i render.py
            runs = [5, 10, 25, 100]            

            for run in runs:
                init_setup(run)

                # Sparar ner en kopia av koordinaterna som precis kördes och tömmer sedan ursprungslistan igen så vi kan köra från start igen 
                globals.archive_coordinates.append(globals.p_coordinates.copy())
                reset()

            multi_render_tent(runs)
        else:
            break
        

start_cli()


