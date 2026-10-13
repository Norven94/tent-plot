import matplotlib.pyplot as plt

from globals import p_coordinates, g


def render_tent() -> None:    
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