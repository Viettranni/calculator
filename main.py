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

    option = input("What would you like to do? Please enter 1-4: ")

    if option in ['1', '2', '3', '4']:
        if option == '1':
            print(f'{first_input} + {second_input} = {calculations.add(first_input, second_input)}')
        elif option == '2':
            print(f'{first_input} - {second_input} = {calculations.add(first_input, second_input)}')
        elif option == '3':
            return print(f'{first_input} * {second_input} = {calculations.add(first_input, second_input)}')
        elif option == '4':
            return print(f'{first_input} / {second_input} = {calculations.add(first_input, second_input)}')
    else:
        print("Please select a number within 1-4!")
        main()



main()

