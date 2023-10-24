# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys

def calculate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Division by zero is undefined"

def main():
    """Implement the calculator"""
    if len(sys.argv) != 4:
        return "Usage: python calc.py <number> <operator> <number>"

    number1 = sys.argv[1]
    operator = sys.argv[2]
    number2 = sys.argv[3]

    expression = f"{number1} {operator} {number2}"
    return calculate(expression)


if __name__ == "__main__":
    print(main())
