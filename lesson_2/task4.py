number=int(input('enter number: '))
factorial=1
if number <0:
    print('error, number is less than zero')
elif number==0:
    print('error, the number is zero')
else:
    for i in range (1, number+1):
        factorial=factorial * i
    print("The factorial of", number, "is", factorial)
