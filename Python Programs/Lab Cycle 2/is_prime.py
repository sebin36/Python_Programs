def is_prime(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

n = int(input('Please enter a number to check if it is prime or not: '))

if is_prime(n):
    print(f'The number {n} is a prime number.')
else:
    print('Not a prime number')
