from art import logo
from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def exponent(n1, n2):
    return n1 ** n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent,
}


def calculator():
    clear()

    print(logo)
    num1 = float(input("What's the first number?: "))

    for op in operations:
        print(op)
    should_continue = True
    while should_continue:
        op_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[op_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {op_symbol} {num2} = {answer}")
        choice = input(
            f"Type 'y' to continue calculation with {answer} or 'n' to start afresh or 'e' to exit out of it: ").lower()
        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            should_continue = False
            calculator()
        else:
            print("Bye Bye")
            break


calculator()
