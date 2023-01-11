def enterNumbers():
    return float(input("Enter number: "))

def enterOperation():
    return input("Enter operation(+, -, *, /, power, root): ")

def enterInput():
    firstNumber=enterNumbers()
    operation=enterOperation()
    secondNumber=enterNumbers()
    return firstNumber, secondNumber, operation

def add(firstNumber, secondNumber):
    return firstNumber + secondNumber

def subtract(firstNumber, secondNumber):
    return firstNumber - secondNumber

def multiplication (firstNumber, secondNumber):
    return firstNumber * secondNumber

def divide(firstNumber, secondNumber):
    return firstNumber / secondNumber

def power(firstNumber, secondNumber):
    return firstNumber**secondNumber

def root(firstNumber, secondNumber):
    return firstNumber**(1/secondNumber)

def calculate(firstNumber, operation, secondNumber):
    match operation:
        case '+':
            print('\n',firstNumber, '+', secondNumber, '=', add(firstNumber, secondNumber))
        case '-':
            print('\n',firstNumber, '-', secondNumber, '=', subtract(firstNumber, secondNumber))
        case '*':
            print('\n',firstNumber, '*', secondNumber, '=', multiplication(firstNumber, secondNumber))
        case '/':
            print('\n',firstNumber, '/', secondNumber, '=', divide(firstNumber, secondNumber))
        case 'power':
            print('\n',firstNumber, '**', secondNumber, '=', power(firstNumber, secondNumber))
        case 'root':
            print('\n',firstNumber, 'root', secondNumber, root(firstNumber, secondNumber))

def main():

    firstNumber, operation, secondNumber = enterInput()
    calculate(firstNumber, secondNumber, operation)

    next_calculation = input("\nLet's do next calculation? (y/n): ")
    if next_calculation == 'n':
        return
    elif next_calculation == 'y':
        firstNumber, operation, secondNumber = enterInput()
        calculate(firstNumber, secondNumber, operation)
    else:
        print('Invalid Input')

main()