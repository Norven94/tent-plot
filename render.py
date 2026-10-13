# Filename: render.py
# Author:   Oskar Anderberg (941201)
# Created:  2026-10-13
# Description:  Hanterar all grafisk rendering för två olika körlägen.

import matplotlib.pyplot as plt
import globals

def render_tent() -> None:    
    x = [coordinate["x"] for coordinate in globals.p_coordinates]
    y = [coordinate["y"] for coordinate in globals.p_coordinates]

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