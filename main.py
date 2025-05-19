"""Simple calculator with no fancy GUI"""
import sys


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_number(prompt: str) -> float:
    resp = ''
    x = float('nan')
    while True:
        try:
            resp = input(prompt)
            x = float(resp)
            break
        except ValueError:
            print(f'{resp} is not a number. Try again.')
            continue

    return x


def get_operation() -> str | None:
    while True:
        response = input('Which operation (+, -, *, /)? ')
        match response:

            case '+' | '-' | '*' | '/':
                return response

            case _:
                print('invalid operation')

    return None


def perform_operation(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2

    return None


def perform_one_calculation() -> None:
    num1 = get_number('Enter the first number:')
    num2 = get_number('Enter the second number:')
    operation = get_operation()
    result = perform_operation(num1, num2, operation)
    print(f'{num1} {operation} {num2} = {result}')


def ask_yes_no_question(question: str) -> bool:
    yn = input(question)
    if len(yn) == 0:
        return False
    if yn[:1].lower() == 'y':
        return True
    return False


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')

    keepCalculating = True
    while keepCalculating:
        perform_one_calculation()
        keepCalculating = ask_yes_no_question("Perform another calculation?")

    print('Thank you for using my calculator')
