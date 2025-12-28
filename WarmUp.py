import math

def read_number(prompt):
    """
    Asks the user for a number.
    Returns an int if valid, otherwise returns None.
    """
    user_input = input(prompt).strip()

    try:
        return int(user_input)
    except ValueError:
        return None


def square_number(num):
    """
    Returns the square of a number.
    """
    return num * num


def circle_area(radius):
    """
    Calculates the area of a circle.
    Uses math.pi.
    """
    return math.pi * radius ** 2


def main():
    numbers = []

    while True:
        value = read_number("Enter a number (or -1 to stop): ")
        
        if value == "done":
            print("Bitch I said enter a number or -1")
            continue


        if value is None:
            print("That was not a valid number.")
            continue

        if value == -1:
            break


        numbers.append(value)

    print("\nResults:")
    for n in numbers:
        print(f"Number: {n}")
        print(f"  Square: {square_number(n)}")
        print(f"  Circle Area (radius={n}): {circle_area(n):.2f}")
        print()


main()