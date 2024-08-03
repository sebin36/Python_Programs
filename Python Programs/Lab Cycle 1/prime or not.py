#Prime number or not
x = int(input('Enter the limit: '))
print(f'Prime numbers upto {x}:')
for j in range(2, x+1):
    count = 0
    for i in range(1,j+1):
        if j%i == 0:
            count += 1
    if count == 2:
        print(j, end=' ')
