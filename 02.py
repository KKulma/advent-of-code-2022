# read the inputs
with open('inputs/02.txt', 'r') as f:
    input = f.read()

# input clean up
input_list = input.split('\n')

opponent_list = [i.replace(' ', '')[0] for i in input_list]
my_list = [i.replace(' ', '')[1] for i in input_list]


### PART 1
# what symbol was used? count points
import string
both_options = string.ascii_uppercase[0:3] + string.ascii_uppercase[-3:]
symbol_points = [1, 2, 3]

# create a lookup dict
symbol_points_dict = dict(zip(both_options, symbol_points+symbol_points))
# count points
opponent_symbol_score = sum([symbol_points_dict[option] for option in opponent_list])
my_symbol_score = sum([symbol_points_dict[option] for option in my_list])


## scores
# (0 if you lost, 3 if the round was a draw, and 6 if you won))
## Rock defeats Scissors,
# Scissors defeats Paper, and
# Paper defeats Rock.
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

opponent_wins = 0
my_wins = 0
for opp, me in zip(opponent_list, my_list):
    if (opp=='A' and me=='X') or (opp=='B' and me=='Y') or (opp=='C' and me=='Z'):
        opponent_wins += 3
        my_wins +=3
    elif (opp=='A' and me=='Z') or (opp=='B' and me=='X') or (opp=='C' and me=='Y'):
        opponent_wins += 6
    else:
        my_wins += 6

my_final_score = my_wins + my_symbol_score
opponent_final_score = opponent_wins + opponent_symbol_score

## answer:
my_final_score


## PART 2

## win points
# X you lose
# Z you win
# Y a draw
win_points = [0, 3, 6]
win_points_dict = dict(zip(string.ascii_uppercase[-3:], win_points))
my_win_score = sum([win_points_dict[option] for option in my_list])


## determine the right symbol

symbol_win_dict = {
    'X': {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    },
    'Z': {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    },
    'Y': {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }
}

# create a lookup dict
symbol_points = [1, 2, 3]
my_symbol_points_dict = dict(zip(string.ascii_uppercase[-3:], symbol_points))

# deteremine strategy
my_new_symbol_points = 0
for opp, me in zip(opponent_list, my_list):
    chosen_symbol = symbol_win_dict[me][opp]
    my_new_symbol_points+= my_symbol_points_dict[chosen_symbol]

# answer
print(my_new_symbol_points + my_win_score)