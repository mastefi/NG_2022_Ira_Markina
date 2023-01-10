wordsList = [int(x) for x in input("Enter random numbers with using ,: ").split(',')]

newList = list(set(wordsList))

print(newList)