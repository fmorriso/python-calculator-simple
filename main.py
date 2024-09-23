"""Simple calculator with no fancy GUI"""
import sys

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def performOneCalculation():
    pass


def askYesNoQuestion(question) -> bool:
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
