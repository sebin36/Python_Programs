#Fibonacci Series
n = int(input('Enter the number of terms in the Fibonacci Series: '))

i = 1
a, b = 0, 1

while i <= n:
    print(a, end=' ')
    a, b = b, a + b
    i += 1
    
