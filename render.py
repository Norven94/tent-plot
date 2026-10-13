# Filename: render.py
# Author:   Oskar Anderberg (941201)
# Created:  2026-10-13
# Description:  Hanterar all grafisk rendering för två olika körlägen.

import matplotlib.pyplot as plt
import globals

def render_tent() -> None:    
    tent_x = [coordinate["x"] for coordinate in globals.p_coordinates]
    tent_y = [coordinate["y"] for coordinate in globals.p_coordinates]

    force_y =  [force for force in globals.max_forces]
    force_x =  [i for i in range(len(globals.max_forces))]

    # Lägger till 3 olika grafer, en figur för tältet och två för maximala kraften som funktion av varje fixpunktsiteration
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(18, 6)) 
    ax[0].plot( 
        tent_x, tent_y, 
        marker=".", 
        linestyle="-", 
        label="Tent" ,
        color="blue",
    ) 
    ax[0].set_xlabel("x") 
    ax[0].set_ylabel("y")
    ax[0].set_title("Particle coordinates and connecting spring")
    ax[0].legend() 

    ax[1].plot( 
        force_x, force_y, 
        marker=".", 
        linestyle="-", 
        label=r'$\sqrt{dF_x^2 + dF_y^2}$',
        color="blue",
    ) 
    ax[1].set_yscale('linear')
    ax[1].set_xlabel("Iteration") 
    ax[1].set_ylabel("Force (N)")
    ax[1].set_title("Max force on particles (linear scale)")
    ax[1].legend()

    ax[2].plot( 
        force_x, force_y, 
        marker=".", 
        linestyle="-", 
        label=r'$\sqrt{dF_x^2 + dF_y^2}$',
        color="blue",
    ) 
    ax[2].set_yscale('log')
    ax[2].set_xlabel("Iteration") 
    ax[2].set_ylabel("Force logarithmic (N)")
    ax[2].set_title("Max force on particles (logarithmic scale)")
    ax[2].legend()

    plt.show() 

def multi_render_tent(runs: list[int]) -> None:
    fig, ax = plt.subplots() 
    colors = ["blue", "red", "orange", "green"]

    for i, render in enumerate(globals.archive_coordinates):
        x = [coordinate["x"] for coordinate in render]
        y = [coordinate["y"] for coordinate in render]
        
        ax.plot( 
                x, y, 
                marker=".", 
                linestyle="-", 
                label=f"N = {runs[i]}" ,
                color=colors[i],
            ) 
        ax.legend() 

    plt.show() 