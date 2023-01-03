number = int(input("Enter the number whose factorial you want to get: "))

factorial = 1

for factorialMultiplier in range(2, number + 1):
    factorial *= factorialMultiplier

print(factorial)
