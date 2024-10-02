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


def get_operation() -> str:
    while True:
        response = input('Which operation (+, -, *, /)? ')
        match response:

            case '+' | '-' | '*' | '/':
                return response

            case _:
                print('invalid operation')



def performOperation(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2


def performOneCalculation() -> None:
    num1 = get_number('Enter the first number:')
    num2 = get_number('Enter the second number:')
    operation = get_operation()
    result = performOperation(num1, num2, operation)
    print(f'{num1} {operation} {num2} = {result}')


def askYesNoQuestion(question: str) -> bool:
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
        performOneCalculation()
        keepCalculating = askYesNoQuestion("Perform another calculation?")

    print('Thank you for using my calculator')
