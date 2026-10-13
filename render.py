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

def multi_render_tent() -> None:
    fig, ax = plt.subplots() 
    colors = ["blue", "red", "orange", "green"]

    for i, render in enumerate(globals.archive_coordinates):
        x = [coordinate["x"] for coordinate in render]
        y = [coordinate["y"] for coordinate in render]
        
        ax.plot( 
                x, y, 
                marker=".", 
                linestyle="-", 
                label="Tent" ,
                color=colors[i],
            ) 
        ax.legend() 

    plt.show() 