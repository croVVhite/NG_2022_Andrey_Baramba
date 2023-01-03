def calculateLettersAmount(userString, letterAmount):
    if len(userString) == 1:
        letterAmount[userString[0]] += 1
        return letterAmount
    else:
        letterAmount[userString[0]] += 1
        return calculateLettersAmount(userString[1:], letterAmount)
