"""Simple command-line calculator functions."""


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ValueError("Cannot divide by zero")
    return first / second


if __name__ == "__main__":
    print("Simple Calculator")
    first_number = float(input("Enter the first number: "))
    operator = input("Choose an operation (+, -, *, /): ")
    second_number = float(input("Enter the second number: "))

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    try:
        result = operations[operator](first_number, second_number)
        print(f"Result: {result}")
    except KeyError:
        print("Invalid operation")
    except ValueError as error:
        print(error)
