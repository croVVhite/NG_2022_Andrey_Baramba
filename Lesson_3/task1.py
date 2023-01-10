def addition(firstNumber, secondNumber):
    return firstNumber + secondNumber


def subtraction(firstNumber, secondNumber):
    return firstNumber - secondNumber


def multiplication(firstNumber, secondNumber):
    return firstNumber * secondNumber


def division(firstNumber, secondNumber):
    return firstNumber / secondNumber


def power(firstNumber, secondNumber):
    return firstNumber ** secondNumber


def root(firstNumber, secondNumber):
    return secondNumber ** (1 / firstNumber)


def main():
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))

    operation = input("\nChoose operation (+, -, *, /, power, root): ")

    match operation:
        case "+":
            print(str(firstNumber) + " + " + str(secondNumber) + " = " + str(addition(firstNumber, secondNumber)))
        case "-":
            print(str(firstNumber) + " - " + str(secondNumber) + " = " + str(subtraction(firstNumber, secondNumber)))
        case "*":
            print(str(firstNumber) + " * " + str(secondNumber) + " = " + str(multiplication(firstNumber, secondNumber)))
        case "/":
            print(str(firstNumber) + " / " + str(secondNumber) + " = " + str(division(firstNumber, secondNumber)))
        case "power":
            print(str(firstNumber) + " ^ " + str(secondNumber) + " = " + str(power(firstNumber, secondNumber)))
        case "root":
            print(str(firstNumber) + "th root of " + str(secondNumber) + " = " + str(root(firstNumber, secondNumber)))


main()
