array=[int(x) for x in input('enter for array: ').split(',')]

print('max character of the given array: ', max(array))
print('min character of the given array: ', min(array))
array.remove(max(array))
array.remove(min(array))

print('received list: ', array)
sum=0
for i in array:
    sum = sum+i

print("The sum of the array is equal to: ", sum)