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


def main():
    string = input("Enter some text: ")

    while True:
        print("\n1. Sort sentence;\n"
              "2. Calculate number of elements in sentence;\n"
              "3. Show only vowels or only consonants from your sentence;\n"
              "4. Show words backwards;\n"
              "5. Show word by number;\n"
              "6. Show your sentence;\n"
              "7. Exit.\n")
        action = input("What do you want to do? (enter action number): ")
        match action:
            case "1":
                stringSort(string)
            case "2":
                stringLen(string)
            case "3":
                vowelsConsonantsOutput(string)
            case "4":
                wordsBackwards(string)
            case "5":
                chosenWordOutput(string)
            case "6":
                print(string)
            case "7":
                break
            case _:
                print("Error! Try again!")


main()
