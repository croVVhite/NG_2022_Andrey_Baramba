size = int(input("input size: "))
outputNum = size + 1

for i in range(size):
    outputNum = size + 1
    for j in range(size):
        print(outputNum - 1, end=' ')
        outputNum -= 1
        if outputNum == 1:
            print("")
    size -= 1
