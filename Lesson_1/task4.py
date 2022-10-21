a = int(input("Enter \"a\" value: "))
b = int(input("Enter \"b\" value: "))
c = int(input("Enter \"c\" value: "))

discriminant = b ** 2 - (4 * a * c)

if discriminant > 0:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print("\nSolution: \nx1 = " + str(x1) + "\nx2 = " + str(x2))
elif discriminant == 0:
    x = -b / (2 * a)
    print("\nSolution: \nx = " + str(x))
elif discriminant < 0:
    print("\nDiscriminant is lower 0, expression have no solution")
