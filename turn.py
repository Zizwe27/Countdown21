import random
def play_human_turn(n):
   # 1. prompt user for their move
    user_move = int(input('How many coins will you take from the table? (Between 1 and 3) '))
     # 2. output number of coins after user's move
    while user_move < 1 or user_move > 3:
        print('Error! Please enter a value between 1 and 3.')
        user_move = int(input('How many coins will you take from the table? (Between 1 and 3) '))
    n = n - user_move
    if n > 0:
        print('There are ' + str(n) + ' coins left on the table.')
        return n
    # 3. If the human wins, indicate that and return 0
    elif n == 0:
        print('Human player wins!')
        return 0
    pass

def play_computer_turn(n):
    # 1. Make computer move
    computer_move = random.randint(1, 3)
    if n % 4 == 0:
        return n - computer_move
    elif n < 20 and n > 16:
        return 16
    elif n < 16 and n > 12 :
        return 12
    elif n < 12 and n > 8:
        return 8
    elif n < 8 and n > 4:
        return 4
    elif n < 4:
        print('Computer player wins!')
        return 0
    # 2. If computer wins, indicate that and return 0
    # 3. return number of coins remaining
    else:
        return n
    pass