user_1_score = 0
user_2_score = 0
turns = 0
while turns < 3:
    user_1 = input('user 1 turn: ')
    user_2 = input('user 2 turn: ')
    turns += 1
    if user_1 == 'r' and user_2 == 'r':
        print('it\'s a draw')
        continue
    elif user_1 == 'r' and user_2 == 'p':
        print('user 2 wins')
        user_2_score += 1
        continue
    elif user_1 == 'r' and user_2 == 's':
        print('user 1 wins')
        user_1_score += 1
        continue
    elif user_1 == 'p' and user_2 == 'r':
        print('user 1 wins')
        user_1_score += 1
        continue
    elif user_1 == 'p' and user_2 == 'p':
        print('it\'s a draw')
        continue
    elif user_1 == 'p' and user_2 == 's':
        print('user 2 wins')
        user_2_score += 1
        continue
    elif user_1 == 's' and user_2 == 'r':
        print('user 2 wins')
        user_2_score += 1
        continue
    elif user_1 == 's' and user_2 == 'p':
        print('user 1 wins')
        user_1_score += 1
        continue
    elif user_1 == 's' and user_2 == 's':
        print('it\'s a draw')
        continue
    elif user_1 or user_2 != 'r' or 'p' or 's':
        print('invalid move')
print(f'user 1 score is {user_1_score}')
print(f'user 2 score is {user_2_score}')