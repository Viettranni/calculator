import calculations


def options():
    print("What would you like to do?\n"
        "Option 1: Add\n"
        "Option 2: Subtract\n"
        "Option 3: Multiply\n"
        "Option 4: Divide\n")


def main():
    print("Welcome to the 'More than a Calculator'")

    first_input = input("Give me the first number: ")
    second_input = input("Give me the second number: ")

    options()

    add = add(first_input, second_input)
    print(add)

main()

