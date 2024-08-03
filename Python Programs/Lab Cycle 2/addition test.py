import random

def addition():
    print('Printable Addition Test')
    print('=======================')
    for i in range(1,5+1):
        print()
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        print(f'Question {i}')
        print(num1,'+',num2,'=','___')

addition()
