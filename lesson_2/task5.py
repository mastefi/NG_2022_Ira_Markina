array=[int(x) for x in input('enter for array: ').split(',')]

print('max character of the given array: ', max(array))
print('min character of the given array: ', min(array))
array.remove(max(array))
array.remove(min(array))

print('received list: ', array)

print("The sum of the array is equal to: ", sum(array))