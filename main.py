import calculations
import database_operations
from calculations import options
from database_operations import save_to_database, create_database


def main():
    while True:
        # Creating the database
        create_database()

        print("Welcome to the 'More than a Calculator'")
        continue_decision = input("If you wish to end the session, write 'quit' otherwise press ENTER ")

        if continue_decision in ['quit']:
            print("Thank you for joining 'More than a Calculator'! ")
            break
        else:
            first_input = int(input("Give me the first number: "))
            second_input = int(input("Give me the second number: "))

            # Displays the 4 options for calculation
            options()

            option = input("What would you like to do? Please enter 1-4: ")

            if option in ['1', '2', '3', '4']:
                if option == '1':
                    answer = calculations.add(first_input, second_input)
                    operation = 'add'
                    print(f'{first_input} + {second_input} = {answer}')
                elif option == '2':
                    answer = calculations.subtract(first_input, second_input)
                    operation = 'subtract'
                    print(f'{first_input} - {second_input} = {answer}')
                elif option == '3':
                    answer = calculations.multiply(first_input, second_input)
                    operation = 'multiply'
                    print(f'{first_input} * {second_input} = {answer}')
                elif option == '4':
                    answer = calculations.divide(first_input, second_input)
                    operation = 'divide'
                    print(f'{first_input} / {second_input} = {answer}')
            else:
                print("Please select a number within 1-4!")
                continue

            # Asks the user wether they want to save this action to the database/history
            ask = input("Do you want to save the calculation to the history? Please answer 'yes' or 'no'. ").strip().lower()

            if ask in ["yes", "no"]:
                if ask == 'yes':
                    save_to_database(first_input, second_input, operation, answer)
                    print("Calculation saved to history.")
                elif ask == 'no':
                    print("Calculation not saved.")
            else:
                print("Invalid input, please type either 'yes' or 'no'.")

            option_history = input("Do you want to see the history? yes/no ")

            if option_history in ["yes", "no"]:
                if option_history == 'yes':
                    print("Here is your requested history log. ")
                    database_operations.get_history()
                elif option_history == 'no':
                    print("You didn't want to view the history log. ")
            else:
                print("Invalid input, please type either 'yes' or 'no'.")


main()

