import task3Funcs as func

userString = input("Enter some text: ")

letterAmount = dict.fromkeys(set(userString), 0)

print(str(func.calculateLettersAmount(userString, letterAmount)))
