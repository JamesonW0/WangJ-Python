import random

play = input('Do you want to play? (y/n)')
options = ['Rock', 'Paper', 'Scissor']
result = {'-2': 'You win', '-1': 'You lose', '0': 'Draw', '1': 'You win', '2': 'You lose'}

while play[0].lower() == 'y':
    user_input = int(input('Please enter a number? \n 1. ROCK \n 2. PAPER \n 3. SCISSOR \n')) - 1
    computer_choice = random.randint(0, 2)
    print("Your play is {0}. \nThe computer' play is {1}. \n{2}".format(options[user_input], options[computer_choice], result[str(user_input-computer_choice)]))
    play = input('Do you want to play? (y/n)')

print('Program ends')