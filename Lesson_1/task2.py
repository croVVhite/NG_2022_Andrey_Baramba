a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operation = input("\nChoose operation (+, -, *, /, square, root): ")

if operation == "+":
    print(str(a) + " + " + str(b) + " = " + str(a + b))

elif operation == "-":
    print(str(a) + " - " + str(b) + " = " + str(a - b))

elif operation == "*":
    print(str(a) + " * " + str(b) + " = " + str(a * b))

elif operation == "/":
    print(str(a) + " / " + str(b) + " = " + str(a / b))

elif operation == "square":
    print(str(a) + " ^ " + str(b) + " = " + str(a ** b))

elif operation == "root":
    print(str(b) + "th root of " + str(a) + " = " + str(a ** (1 / b)))

else:
    print("Invalid operation value!")
