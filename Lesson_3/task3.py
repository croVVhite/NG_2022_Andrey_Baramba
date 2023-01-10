def calculateLettersAmount(userString, letterAmount):
    if len(userString) == 1:
        letterAmount[userString[0]] += 1
        return letterAmount
    else:
        letterAmount[userString[0]] += 1
        return calculateLettersAmount(userString[1:], letterAmount)


def main():
    userString = input("Enter some text: ")

    letterAmount = dict.fromkeys(set(userString), 0)

    print(str(calculateLettersAmount(userString, letterAmount)))


main()
