import random

game_options = ['R', 'P', 'S']

def computer_move():
    computer_choice = random.choice(game_options)
    if computer_choice == 'R':
        computer_choice= 'Rock'
    elif computer_choice == 'P':
        computer_choice = 'Paper'
    elif computer_choice == 'S':
        computer_choice = 'Scissors'

    return computer_choice



