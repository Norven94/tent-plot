from tent_types import Coordinates

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