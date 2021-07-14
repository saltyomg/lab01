from random import randint


user_1_score = 0
computer_score = 0
turns = 0
moves = ['r', 'p', 's']


while turns < 5:
    turns += 1
    computer = moves[randint(0, 2)]
    user_1 = input('rock, paper or scissors?')
    if user_1 == computer:
        print('it\'s a draw')
        continue
    elif user_1 == 'r':
        if computer == 'p':
            print('computer chose paper and wins')
            computer_score += 1
        else:
            print('user wins coz comps chose scissors')
            user_1_score += 1
    elif user_1 == 'p':
        if computer == 's':
            print('computer chose scissor and wins')
            computer_score += 1
        else:
            print('user wins coz comps chose rock')
            user_1_score += 1
    elif user_1 == 's':
        if computer == 'r':
            computer_score += 1
            print('computer chose rock and wins')
        else:
            print('user wins coz comps chose paper')
            user_1_score += 1
    elif user_1 or computer != 'r' or 'p' or 's':
        print('invalid move')


print(f'Your score is {user_1_score}')
print(f'computer score is {computer_score}')
if user_1_score > computer_score:
    print('YOU WON!!!!')
elif user_1_score == computer_score:
    print('IT\'S A DRAW')
else:
    print('SORRY YOU LOST')
