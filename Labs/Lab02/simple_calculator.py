
import math
# Lab 2

# Create new file named `simple_calculator.py`

# Build a command line program which prompts the user for a command.

# Write a program that calculates the circumference of a circle given a radius as an input parameter

string_radius = input("What is the radius? : ")
radius = int(string_radius)

circumference = 2 * math.pi * radius
print(f"Circumference is: {round(circumference, 2)}")