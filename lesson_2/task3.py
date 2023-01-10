inputSize=int(input("enter number: "))

while inputSize>0:
    outputSize=inputSize
    while outputSize>0:
        print(outputSize, end=' ')
        outputSize-=1
    inputSize-=1
    print(' ')
