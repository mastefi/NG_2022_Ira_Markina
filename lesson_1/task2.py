a=int(input("enter number a: "))
b=int(input('enter number b: '))
operation=input('enter operation: +,-, *, /, ** or sqrt: ')
if operation=='+':
    print('a+b=', a + b)

elif operation=='*':
    print('a*b=', a*b)

elif operation=='-':
    print('a-b=', a-b)

elif operation=='/':
     print('a/b=', a/b)

elif operation=='**':
    n=int(input('enter power: '))
    print('a^n=', a**n)
    print('a^n=', b**n)

elif operation=='sqrt':
    print('sqrt(a)= ', a ** (1 / 2))
    print('sqrt(b)= ', b ** (1 / 2))
else:
    print('You have not typed a valid operator, please run the program again.')