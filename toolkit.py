import random

# ==================================================
# Tool 1: Simple Calculator
# Performs basic arithmetic operations on two numbers.
# Uses: Conditionals (if/elif/else), f-strings, basic arithmetic operations.
# ==================================================
def simple_calculator():
    print("\n--- Tool 1: Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print(f"Invalid operator '{operator}'. Please use +, -, *, or /.")
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")


# ==================================================
# Tool 2: Task Tracker
# Manages a dynamic list of tasks (add, view, remove).
# Uses: Lists, loops (while/for), conditionals, f-strings.
# ==================================================
def task_tracker():
    print("\n--- Tool 2: Task Tracker ---")
    tasks = []
    
    while True:
        print("\nTask Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Return to Main Menu")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                print(f"Added task: '{task}'")
            else:
                print("Task cannot be empty.")
        elif choice == '2':
            if not tasks:
                print("Your task list is empty.")
            else:
                print("\nYour Tasks:")
                for index, item in enumerate(tasks, 1):
                    print(f"{index}. {item}")
        elif choice == '3':
            if not tasks:
                print("No tasks available to remove.")
            else:
                for index, item in enumerate(tasks, 1):
                    print(f"{index}. {item}")
                try:
                    num = int(input("Enter task number to remove: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Removed task: '{removed}'")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid integer number.")
        elif choice == '4':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option! Please select a number between 1 and 4.")


# ==================================================
# Tool 3: Number Guessing Game
# Generates a random number between 1 and 20 for the user to guess.
# Uses: Random module, while loop, conditionals, f-strings.
# ==================================================
def number_guessing_game():
    print("\n--- Tool 3: Number Guessing Game ---")
    target = random.randint(1, 20)
    attempts = 0
    print("I'm thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < target:
                print("Too low! Try again.")
            elif guess > target:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target} in {attempts} attempt(s)!")
                break
        except ValueError:
            print("Please enter a valid whole number.")


# ==================================================
# Main Menu Loop
# Routes user choices and survives invalid inputs gracefully.
# ==================================================
def main():
    print("=" * 50)
    print("   Welcome to your Personal Mini-Toolkit!   ")
    print("=" * 50)

    while True:
        print("\nMain Menu:")
        print("1. Simple Calculator")
        print("2. Task Tracker (To-Do List)")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            simple_calculator()
        elif choice == '2':
            task_tracker()
        elif choice == '3':
            number_guessing_game()
        elif choice == '4':
            print("\nThank you for using Personal Mini-Toolkit! Goodbye!")
            break
        else:
            print(f"\nOops! '{choice}' is not a valid menu option. Please try entering 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()