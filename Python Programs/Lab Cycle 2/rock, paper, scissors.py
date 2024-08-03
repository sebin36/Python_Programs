import random

def game():
    while True:
        print()
        print('''Let's play Rock, Paper, Scissors!''')
        
        options = {1:'rock', 2:'paper', 3:'scissors'}
        
        user_choice = input('Enter your choice (rock, paper, scissors): ').lower()

        comp_choice = options[random.randint(1,3)]

        print(f'Computer chooses: {comp_choice}')

        if user_choice == comp_choice:
            print('''It's a tie! play again.''')
        elif user_choice == 'rock' and comp_choice == 'scissors':
            print('You Won!')
        elif user_choice == 'scissors' and comp_choice == 'paper':
            print('You Won!')
        elif user_choice == 'paper' and comp_choice == 'rock':
            print('You Won!')
        else:
            print('You Lost...')

        play = input('Do you want to play again? ')
            
        if play == 'y':
            continue
        else:
            print('Done')
            break

game()
