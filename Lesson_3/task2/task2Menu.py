import task2Funcs as func

string = input("Enter some text: ")

while True:
    print("\n1. Sort sentence;\n"
          "2. Calculate number of elements in sentence;\n"
          "3. Show only vowels or only consonants from your sentence;\n"
          "4. Show words backwards;\n"
          "5. Show word by number;\n"
          "6. Show your sentence;\n"
          "7. Exit.\n")
    action = input("What to do with your sentence? (enter action number): ")
    match action:
        case "1":
            func.stringSort(string)
        case "2":
            func.stringLen(string)
        case "3":
            func.vowelsConsonantsOutput(string)
        case "4":
            func.wordsBackwards(string)
        case "5":
            func.chosenWordOutput(string)
        case "6":
            print(string)
        case "7":
            break
        case _:
            print("Error! Try again!")
