import math

a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of c: '))

res = (b**2) - (4*a*c)

z = math.sqrt(res)

if z > 0:
    x = (-(b) + z)/(2*a)
    y = (-(b) - z)/(2*a)
    print(f'Real roots: Root 1 = {x} Root 2 = {y}')
else:
    x = -b / (2*a)
    print(f'Real and Equal root: Root 1 = {x}')


