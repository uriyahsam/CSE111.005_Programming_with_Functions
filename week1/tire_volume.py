import math
from datetime import date

# Prompt the user for input.
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Compute the volume using the given formula.
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10_000_000_000

# Display the result.
print(f"The approximate volume is {volume:.2f} liters")

# Get the current date.
current_date = date.today()

# Open the volumes.txt file in append mode and write the data.
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")
