# import math function Python has a set of built-in math functions, including an extensive math module, that allows
# you to perform mathematical tasks on numbers.
from math import pi, tan, cos

# Setting constant to the formula
# Equal sign assigns a number to my variable (g)
g = 9.81  # Acceleration due to gravity (m/s^2)

# Given parameters
# Equal sign assigns a number to my variables.
barrel_height = 1  # Height of the barrel (m)
horizontal_distance = 0.5  # Horizontal distance travelled (m)
initial_velocity = 44  # Initial velocity (m/s)

# Adding the input for degree and converting it to theta
deg = 80  # Elevation angle in degrees
theta = deg * (pi / 180)
# Calculate projectile height
# Formula based on exercise guide.
# ** is used for power
height = barrel_height + horizontal_distance * tan(theta) - ((horizontal_distance ** 2) * g) / (
            2 * (initial_velocity * cos(theta)) ** 2)

# Print the output the result
# I added the unit by adding in a string "m"
print("Height of the projectile:", height, "m")
