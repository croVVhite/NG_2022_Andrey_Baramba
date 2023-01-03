def stringSort(string):
    symbolCodes = [ord(letter) for letter in string.replace(' ', '')]
    print([chr(letter) for letter in sorted(symbolCodes)])


def stringLen(string):
    print("In your sentence " + str(len(string)) + " elements")


def vowelsConsonantsOutput(string):
    choice = input("Vowels or consonants to remove? (0 or 1 respectively): ")
    match choice:
        case "0":
            for letter in string:
                if letter not in 'aeiouAEIOU':
                    print(letter, end='')
        case "1":
            for letter in string:
                if letter not in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                    print(letter, end='')


def wordsBackwards(string):
    print(string.split(' ')[::-1])


def chosenWordOutput(string):
    wordIndex = int(input("Enter word number you want to see: "))
    print(string.split(' ')[wordIndex - 1])
