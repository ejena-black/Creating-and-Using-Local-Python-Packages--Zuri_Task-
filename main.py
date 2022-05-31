import random

# Game 
game_options = ['R', 'P', 'S']
game_options_moves = ['Rock', 'Paper', 'Scissors']
game = dict(zip(game_options, game_options_moves))

# Computer_logic
def computer_move():
    computer_choice = random.choice(game_options)
    if computer_choice in game:
        return game[computer_choice]


# Player_logic
def player_move():
    while True:
        player_choice = input('Pick a move "R", "P", "S":  ')
        player_choice = player_choice.upper()

        if player_choice in game:
            return game[player_choice]
            
        else:
            print('Invalid input, Please pick from the options given \n')



# Game prompt
print('Welcome to the Rock, Paper, Scissors game  \nThis game is Player vs CPU  \nYour avaliable moves are:')
print('"R" for "Rock"  \n"P" for "Paper" \n"S" for "Scissors" ')

# Main game logic
while True:
    com = computer_move()
    player = player_move()
    

    # Player and Computer move displayed
    print(f'\nPlayer ({player}) : CPU ({com}) \n')


    # Winner check
    if player == com:
            print('It\'s a tie Play again \n')

    elif player == 'Rock':
        if com == 'Paper':
            print('Computer Wins')
            break
        elif com == 'Scissors':
            print('Player Wins')
            break

    elif player == 'Paper':
        if com == 'Rock':
            print('Player Wins')
            break
        elif com == 'Scissors':
            print('Computer Wins')
            break

    elif player == 'Scissors':
        if com == 'Rock':
            print('Computer Wins')
            break
        elif com == 'Paper':
            print('Player Wins')
            break