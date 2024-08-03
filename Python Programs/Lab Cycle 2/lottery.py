import random

lst = []

print('The lucky numbers are below. Thanks for participating.')

print()
for i in range(7):
    x = random.randint(0,9)
    lst.append(x)

for j in lst:
    print(j, end=' ')

