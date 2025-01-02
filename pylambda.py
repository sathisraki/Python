#!/usr/bin/python3.12

#syntax is lambda arguments : expression
x = lambda x : x + 10
print(x(2))

#lambda can take multiple arguments
y = lambda a,b : a+10

print(y(10,"a"))
print(y(10,2))

#Use of lambda function:
def func(x):
    return lambda z : z*int(x)

mul = input("Enter multipler :")
print(f'the multipler value is {mul}')
y = func(mul) # func(mul) returns lambda z : z*int(x) to y
for i in range(1,11):
    print(f'{i}*{mul}={y(i)}')

