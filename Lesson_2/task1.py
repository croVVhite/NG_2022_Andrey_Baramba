userString = input("Enter some text: ")

letterAmount = dict.fromkeys(set(userString), 0)

for letter in userString:
    if letter in letterAmount.keys():
        letterAmount[letter] += 1

print("Amount of every letter in your string: " + str(letterAmount))
print("Letters amount sorted by letters: " + str(dict(sorted(letterAmount.items(), key=lambda x: x[0]))))
print("Letters amount sorted by numbers: " + str(dict(sorted(letterAmount.items(), key=lambda x: x[1]))))
