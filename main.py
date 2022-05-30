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



# Game prompt
print('Welcome to the Rock, Paper, Scissors game  \nThis game is Player vs CPU  \nYour avaliable moves are:')
print('"R" for "Rock"  \n"P" for "Paper" \n"S" for "Scissors" ')

# Game loop
while True:
    com = computer_move()
    
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

    # Player and Computer move displayed
    print(f'\nPlayer ({player_choice}) : CPU ({com}) \n')


    # Winner check
    if player_choice == com:
            print('It\'s a tie Play again \n')

    elif player_choice == 'Rock':
        if com == 'Paper':
            print('Computer Wins')
            break
        elif com == 'Scissors':
            print('Player Wins')
            break

    elif player_choice == 'Paper':
        if com == 'Rock':
            print('Player Wins')
            break
        elif com == 'Scissors':
            print('Computer Wins')
            break

    elif player_choice == 'Scissors':
        if com == 'Rock':
            print('Computer Wins')
            break
        elif com == 'Paper':
            print('Player Wins')
            break