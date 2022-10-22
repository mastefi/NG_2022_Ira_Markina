import math
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
    print('sqrt(a)= ', math.sqrt(a))
    print('sqrt(b)= ', math.sqrt(b))
else:
    print('You have not typed a valid operator, please run the program again.')