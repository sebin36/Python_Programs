#Armstrong of a number.
a = int(input('Enter start point: '))
b = int(input('Enter end point: '))

print('\n')

print(f'Armstrong Numbers from {a} to {b}:')

for x in range(a,b+1):
    lst = []
    sum = 0
    temp = x

    while temp > 0:
        z = temp % 10
        temp = temp // 10
        lst.append(z)

    lst = lst[::-1]

    count = len(lst)
                            
    for i in lst:
        prod = 1
        for j in range(count):
            prod *= int(i)
        sum += prod

    if sum == x:
        print(x, end=' ')

#Another Method
        
#a = int(input('Enter start point: '))
#b = int(input('Enter end point: '))

#print('\n')

#print(f'Armstrong Numbers from {a} to {b}:')

#for x in range(a,b+1):
#    x = str(x)
#    val = 0

#    for j in x:
#        val += (int(j) ** len(x))

#    if val == int(x):
#        print(x, end=' ')
