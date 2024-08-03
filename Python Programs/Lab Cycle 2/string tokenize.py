a = str(input('Enter string 1: '))
b = str(input('Enter string 2: '))
c = str(input('Enter string 3: '))

lis1 = a.split(' ')
lis2 = b.split(':')
lis3 = c.split('/')

for i in lis1:
    print(f'Token: {i}')

print()

for i in lis2:
    print(f'Token: {i}')

print()

for i in lis3:
    print(f'Token: {i}')
