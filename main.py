import calculations


def options():
    print("What would you like to do?\n"
        "Option 1: Add\n"
        "Option 2: Subtract\n"
        "Option 3: Multiply\n"
        "Option 4: Divide\n")


def main():
    print("Welcome to the 'More than a Calculator'")

    first_input = int(input("Give me the first number: "))
    second_input = int(input("Give me the second number: "))

    # Displays the 4 options for calculation
    options()

    option = input("What would you like to do? Please enter 1-4")

    # Calling the calculation logic from the library
    add = calculations.add(first_input, second_input)
    subtract = calculations.subtract(first_input, second_input)
    multiply = calculations.multiply(first_input, second_input)
    divide = calculations.divide(first_input, second_input)

    if option == 1:
        return add
    if option == 2:
        return subtract
    if option == 3:
        return multiply
    if option == 4:
        return divide


main()

