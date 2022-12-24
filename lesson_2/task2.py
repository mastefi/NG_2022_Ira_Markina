array=[int(x) for x in input('enter for array: ').split(',')]

result = []
for i in array:
    if i not in result:
        result.append(i)

print("output list without repetitions: " + str(result))
