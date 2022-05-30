import random

game_options = ['R', 'P', 'S']


# Computer_logic
def computer_move():
    computer_choice = random.choice(game_options)
    if computer_choice == 'R':
        computer_choice= 'Rock'
    elif computer_choice == 'P':
        computer_choice = 'Paper'
    elif computer_choice == 'S':
        computer_choice = 'Scissors'

    return computer_choice


# Player_logic
while True:
    player_choice = input('Pick a move "R", "P", "S":  ')
    player_choice = player_choice.upper()

    if player_choice in game_options:
        if player_choice == 'R':
            player_choice= 'Rock'
        elif player_choice == 'P':
            player_choice = 'Paper'
        elif player_choice == 'S':
            player_choice = 'Scissors'
        break
        
    else:
        print('Invalid input, Please pick from the options given \n')
    




# Game prompt
print('Welcome to the Rock, Paper, Scissors game  \nThis game is Player vs CPU')
print('"R" is for "Rock"  \n"P" is for "Paper" \n"S" is for "Scissors" ')

