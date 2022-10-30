userString = input("Enter some text: ")

letterAmount = {}

# Entering data to the dictionary
for letter in userString:
    if letter not in letterAmount.keys():
        letterAmount[letter] = 1
    else:
        letterAmount[letter] += 1

# Output results of entering data
for key in letterAmount.keys():
    print("\t" + str(key) + ": " + str(letterAmount[key]))

# Dictionary with values sorted by keys (letters)
letterAmountSortedByLetters = dict(sorted(letterAmount.items(), key=lambda x: x[0]))

print("\nLetters amount sorted by letters: ")
for key in letterAmountSortedByLetters.keys():
    print("\t" + str(key) + ": " + str(letterAmountSortedByLetters[key]))

# Dictionary with values sorted by values (amounts of letters)
letterAmountSortedByNumbers = dict(sorted(letterAmount.items(), key=lambda x: x[1]))

print("\nLetters amount sorted by numbers: ")
for key in letterAmountSortedByNumbers.keys():
    print("\t" + str(key) + ": " + str(letterAmountSortedByNumbers[key]))
