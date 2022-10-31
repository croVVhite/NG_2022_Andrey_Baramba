userList = [int(x) for x in input("Enter the numbers via coma: ").split(',')]

uniqueNumbers = list(set(userList))

print(uniqueNumbers)
