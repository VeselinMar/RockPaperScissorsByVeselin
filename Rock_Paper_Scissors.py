import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')

while True:
    if player_move == 'r':
        player_move = rock
        break
    elif player_move == 'p':
        player_move = paper
        break
    elif player_move == 's':
        player_move = scissors
        break
    else:
        print('Invalid input. Try again.')
        player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')

computer_random_number = random.randint(1, 3)

computer_move = ''

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors
print(f'Computer chose: {computer_move}')

if (player_move == rock and computer_move == scissors) or \
        (player_move == scissors and computer_move == paper) or \
        (player_move == paper and computer_move == rock):
    print('You win!')
elif (player_move == rock and computer_move == rock) or \
        (player_move == scissors and computer_move == scissors) or \
        (player_move == paper and computer_move == paper):
    print('Draw!')
else:
    print('You lose!')
