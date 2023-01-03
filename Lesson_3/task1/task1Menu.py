import task1Funcs as func

firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

operation = input("\nChoose operation (+, -, *, /, power, root): ")

match operation:
    case "+":
        print(str(firstNumber) + " + " + str(secondNumber) + " = " + str(func.addition(firstNumber, secondNumber)))
    case "-":
        print(str(firstNumber) + " - " + str(secondNumber) + " = " + str(func.subtraction(firstNumber, secondNumber)))
    case "*":
        print(str(firstNumber) + " * " + str(secondNumber) + " = " + str(func.multiplication(firstNumber, secondNumber)))
    case "/":
        print(str(firstNumber) + " / " + str(secondNumber) + " = " + str(func.division(firstNumber, secondNumber)))
    case "power":
        print(str(firstNumber) + " ^ " + str(secondNumber) + " = " + str(func.power(firstNumber, secondNumber)))
    case "root":
        print(str(secondNumber) + "th root of " + str(firstNumber) + " = " + str(func.root(firstNumber, secondNumber)))
