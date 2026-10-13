# Filename: globals.py
# Author:   Oskar Anderberg (941201)
# Created:  2026-10-13
# Description:  Globala variabler som samtliga moduler behöver ha tillgång till utan
#               att behöva skicka med de som parametrar i funktionerna.

from tent_types import Coordinates

# Fasta variabler
g = 9.82 # m/s^2
total_spring_k = 1 # N/m
total_p_mass = 1 # kg
total_spring_length = 1 # m

# Variabler baserade på val av N
spring_k = 0
p_mass = 0
spring_length = 0

# Randvillkoren 
ry = 0
rx0 = 0
rx1 = 1

# Tält fästen 
ymax = 1
xmax1 = 1/3
xmax2 = 2/3

# Start koordinater
p_coordinates: list[Coordinates] = []

# Arkiv över koordinater för masskörning
archive_coordinates: list[list[Coordinates]] = []

# Data för maximala kraften under respektive fixpunktsiteration
max_forces: list[float] = []