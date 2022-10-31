number = int(input("Enter the number whose factorial you want to get: "))

factorial = 1

for i in range(2, number + 1):
    factorial *= i

print(factorial)
