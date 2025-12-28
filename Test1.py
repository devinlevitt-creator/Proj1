# This function converts an angle measured in radians into degrees.
# It accepts one numeric parameter representing radians.
# The conversion uses the mathematical relationship:
# degrees = radians * (180 / pi).
# The value of pi is imported from Python's math module.
# The function returns the equivalent angle in degrees.
import math

def read_int(prompt: str):
    s = input(prompt).strip()
    try:
        return int(s)
    except ValueError:
        return None

while True:
    r = read_int("Enter the radian of your circle: ")
    if r is None:
        print("Not a valid number")
        continue
    if r >= 1:
        degrees = math.degrees(r)
        if math.degrees(r) > 360:
            print('This exceeds a maximum possible 360 degrees.')
            continue
        else:
            print(f"{r} radians = {degrees} degrees")
            continue

        
