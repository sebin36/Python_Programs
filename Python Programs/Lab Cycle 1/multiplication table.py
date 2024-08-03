#Multiplication Table
cols = int(input('enter col: '))
rows = int(input('enter row: '))

print('   ',end=' ')

for i in range(1, rows+1):
    print(f'{i:2}', end=' ')

print('\n','  ','---' * rows)

for i in range(1, cols+1):
    print()
    print(f'{i:2}', '|', end=' ')
    for j in range(1, rows+1):
        print(f'{(i*j):2}', end=' ')


