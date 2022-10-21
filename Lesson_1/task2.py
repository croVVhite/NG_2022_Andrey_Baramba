firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

operation = input("\nChoose operation (+, -, *, /, square, root): ")

if operation == "+":
    print(str(firstNumber) + " + " + str(secondNumber) + " = " + str(firstNumber + secondNumber))

elif operation == "-":
    print(str(firstNumber) + " - " + str(secondNumber) + " = " + str(firstNumber - secondNumber))

elif operation == "*":
    print(str(firstNumber) + " * " + str(secondNumber) + " = " + str(firstNumber * secondNumber))

elif operation == "/":
    print(str(firstNumber) + " / " + str(secondNumber) + " = " + str(firstNumber / secondNumber))

elif operation == "square":
    print(str(firstNumber) + " ^ " + str(secondNumber) + " = " + str(firstNumber ** secondNumber))

elif operation == "root":
    print(str(secondNumber) + "th root of " + str(firstNumber) + " = " + str(firstNumber ** (1 / secondNumber)))

else:
    print("Invalid operation value!")
