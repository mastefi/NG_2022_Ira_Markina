from math import sqrt

a=int(input('enter number a: '))
b=int(input('enter number b: '))
c=int(input('enter number c: '))

D=b**2-4*a*c
print('the discriminant is equal to: ', D)

if D>0:
    x1=(-b-sqrt(D))/2*a
    x2=(-b+sqrt(D))/2*a
    print('the 1st root of the equation: ',x1,'\nthe 2st root of the equation: ',x2)

elif D==0:
    x=-b/2*a
    print('the root of the equation: ', x)

else:
    print('the equation has no roots')
