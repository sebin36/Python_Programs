#Number Guess
import random
gues_no = random.randint(10,99)

print('''I've selected a random two-digit number between 10 and 99.
Can you guess it?''')

print('\n')

while True:
    x = int(input('Enter guess: '))
    if x in range(10,99+1):
        if gues_no == x:
            print(f'Congrats! You guessed it: {gues_no}')
            break
        elif x > gues_no:
            print('Too High')
        else:
            print('Too Low')
    else:
        print(f'Enter a number between 10 to 99.')
        continue
    
    
